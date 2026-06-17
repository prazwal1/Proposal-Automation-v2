"""FusionAuth (OIDC) bearer-JWT validation for the MCP server's HTTP transport.

The MCP server acts as an OAuth 2.0 Resource Server: FusionAuth issues the
access tokens, and here we verify each token's signature against FusionAuth's
JWKS and check its issuer / audience / expiry / scopes. FastMCP then advertises
itself as a protected resource (RFC 9728) pointing at FusionAuth, so OAuth-aware
clients (e.g. claude.ai connectors) can discover the auth server and log in.

Auth is enabled only when the FUSIONAUTH_* env vars are present, so local stdio
runs (Claude Code via .mcp.json) stay unauthenticated.

Env vars:
  FUSIONAUTH_BASE_URL   (required) FusionAuth base URL, e.g. https://auth.acme.com
  MCP_RESOURCE_URL      (required) public URL of THIS server, e.g. https://mcp.acme.com
  FUSIONAUTH_AUDIENCE   (recommended) expected `aud` = the FusionAuth application/client id
  FUSIONAUTH_JWT_ISSUER (optional) expected `iss`; defaults to FUSIONAUTH_BASE_URL
  FUSIONAUTH_JWKS_URI   (optional) override; defaults to <base>/.well-known/jwks.json
  MCP_REQUIRED_SCOPES   (optional) space/comma-separated scopes a token must carry
"""
import asyncio
import os

import jwt
from jwt import PyJWKClient

from mcp.server.auth.provider import AccessToken, TokenVerifier
from mcp.server.auth.settings import AuthSettings


class FusionAuthVerifier(TokenVerifier):
    """Verifies FusionAuth-issued JWTs against the tenant's JWKS."""

    def __init__(self, *, jwks_uri: str, issuer: str,
                 audience: str | None = None, algorithms=("RS256",)):
        self._issuer = issuer
        self._audience = audience
        self._algorithms = list(algorithms)
        # PyJWKClient caches signing keys and refreshes on unknown kid (key rotation).
        self._jwks = PyJWKClient(jwks_uri, cache_keys=True)

    async def verify_token(self, token: str) -> AccessToken | None:
        # jwt + JWKS lookup are blocking; keep the event loop free.
        try:
            return await asyncio.to_thread(self._decode, token)
        except Exception:
            return None  # any failure (bad sig, expired, wrong aud/iss) → unauthorized

    def _decode(self, token: str) -> AccessToken:
        signing_key = self._jwks.get_signing_key_from_jwt(token)
        claims = jwt.decode(
            token,
            signing_key.key,
            algorithms=self._algorithms,
            issuer=self._issuer,
            audience=self._audience,
            options={"require": ["exp", "iss"],
                     "verify_aud": self._audience is not None},
        )
        raw = claims.get("scope") or claims.get("scp") or []
        scopes = raw.split() if isinstance(raw, str) else list(raw)
        aud = claims.get("aud")
        client_id = (aud[0] if isinstance(aud, list) and aud else aud) \
            or claims.get("client_id") or ""
        return AccessToken(
            token=token,
            client_id=client_id,
            scopes=scopes,
            expires_at=claims.get("exp"),
            subject=claims.get("sub"),
            claims=claims,
        )


def build_auth() -> tuple[FusionAuthVerifier | None, AuthSettings | None]:
    """Build (token_verifier, AuthSettings) from env, or (None, None) if FusionAuth
    is not configured (e.g. local stdio dev)."""
    base = os.environ.get("FUSIONAUTH_BASE_URL")
    resource = os.environ.get("MCP_RESOURCE_URL")
    if not base or not resource:
        return None, None

    base = base.rstrip("/")
    issuer = os.environ.get("FUSIONAUTH_JWT_ISSUER", base)
    jwks_uri = os.environ.get("FUSIONAUTH_JWKS_URI", f"{base}/.well-known/jwks.json")
    audience = os.environ.get("FUSIONAUTH_AUDIENCE") or None
    scopes = os.environ.get("MCP_REQUIRED_SCOPES", "").replace(",", " ").split()

    verifier = FusionAuthVerifier(jwks_uri=jwks_uri, issuer=issuer, audience=audience)
    settings = AuthSettings(
        issuer_url=base,
        resource_server_url=resource,
        required_scopes=scopes or None,
    )
    return verifier, settings
