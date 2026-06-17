"""MCP server exposing the v2 Azure calculator tool layer (stdio).

Register with Claude Code:
  claude mcp add azure-calc -- uv run --directory <repo> mcp_server.py

Everything real lives in tools.py; this file only adapts it to MCP.
"""
from mcp.server.fastmcp import FastMCP
from starlette.responses import JSONResponse

import tools
from auth import build_auth

INSTRUCTIONS = """\
Azure quotation tools built on a learned map of the Azure Pricing Calculator
(152 services). You select services and author estimate configs; prices are
NEVER computed by you — ballparks come from quick_price, official numbers
from a calculator build.

Recommended workflow:
1. search_catalog / list_services to pick services.
2. get_config_guide once, then get_service_doc(slug) for each chosen service
   to learn its exact field keys, options and dependencies.
3. Author the estimate config JSON and call validate_config. Fix every error
   it reports (the messages say exactly which gating field to set) and
   re-validate until ok.
4. quick_price for an instant ballpark while the user decides.
5. build_estimate to produce the official xlsx (takes minutes, runs in the
   background) and check_build to poll until the xlsx path appears.
"""

# When FUSIONAUTH_* env vars are set, run as an OAuth Resource Server that
# validates FusionAuth JWTs; otherwise (local stdio) run unauthenticated.
_token_verifier, _auth_settings = build_auth()
mcp = FastMCP(
    "azure-calc",
    instructions=INSTRUCTIONS,
    token_verifier=_token_verifier,
    auth=_auth_settings,
)


@mcp.custom_route("/healthz", methods=["GET"])
async def healthz(_request):
    """Unauthenticated liveness probe for VM/load-balancer health checks."""
    return JSONResponse({"status": "ok"})


@mcp.tool()
def list_services() -> list[dict]:
    """List all 152 supported Azure services (product, slug, category, field count)."""
    return tools.list_services()


@mcp.tool()
def search_catalog(query: str, limit: int = 12) -> list[dict]:
    """Search supported services by name, category, field, or option text
    (e.g. 'virtual machine', 'premium ssd', 'kubernetes'). Returns ranked
    matches with the slug to use in configs and with get_service_doc."""
    return tools.search_catalog(query, limit=limit)


@mcp.tool()
def get_service_doc(slug: str) -> str:
    """Full reference for one service: every config field key, its options,
    and state dependencies (fields that only exist when another field is set).
    ALWAYS read this before authoring a component for a service."""
    return tools.get_service_doc(slug)


@mcp.tool()
def get_config_guide() -> str:
    """How to write estimate configs: JSON format, field-matching rules,
    radio groups, dependent fields. Read once before your first config."""
    return tools.get_config_guide()


@mcp.tool()
def validate_config(config: dict) -> dict:
    """Validate an estimate config offline (instant, no browser). Returns
    errors/warnings; error messages state exactly which field or gating
    value to fix. Iterate until ok=true before building."""
    return tools.validate_config(config)


@mcp.tool()
def build_estimate(config: dict, export: bool = True, force: bool = False) -> dict:
    """Build the estimate in the real Azure Pricing Calculator (headless
    Chrome) and export the official xlsx. Asynchronous: returns a job_id
    immediately; poll check_build. Validates first and refuses on errors
    unless force=true. Takes roughly 1-3 minutes per component."""
    return tools.start_build(config, export=export, force=force)


@mcp.tool()
def check_build(job_id: str) -> dict:
    """Status of a build job: running / succeeded / failed, the exported
    xlsx path when done, and the last lines of the build log."""
    return tools.check_build(job_id)


@mcp.tool()
def list_builds(limit: int = 10) -> list[dict]:
    """Recent build jobs, newest first (use to recover a lost job_id)."""
    return tools.list_builds(limit=limit)


@mcp.tool()
def quick_price(service_name: str = "", region: str = "",
                sku_contains: str = "", product_contains: str = "",
                price_type: str = "Consumption", top: int = 10) -> dict:
    """Live list prices from the Azure Retail Prices API for instant
    ballparks (NOT the official quote). region is the ARM name, e.g.
    'southeastasia'. price_type: 'Consumption' or 'Reservation'. Use
    service_name like 'Virtual Machines' plus sku_contains like 'D4s v5'."""
    return tools.quick_price(
        service_name=service_name or None,
        region=region or None,
        sku_contains=sku_contains or None,
        product_contains=product_contains or None,
        price_type=price_type or None,
        top=top,
    )


if __name__ == "__main__":
    import argparse

    ap = argparse.ArgumentParser(description="azure-calc MCP server")
    ap.add_argument(
        "--http", action="store_true",
        help="serve over HTTP (streamable-http) instead of stdio — use this for "
             "remote clients or AI hosts that connect to a URL rather than "
             "launching the process themselves. Endpoint: http://<host>:<port>/mcp",
    )
    ap.add_argument("--host", default="127.0.0.1",
                    help="bind address for --http (use 0.0.0.0 to accept LAN/tunnel)")
    ap.add_argument("--port", type=int, default=8000, help="port for --http")
    ap.add_argument(
        "--no-auth", action="store_true",
        help="DANGER: serve --http unauthenticated (only when FusionAuth env vars are "
             "absent). Use only on a trusted private network, never on a public address.",
    )
    args = ap.parse_args()

    if not args.http:
        mcp.run()  # stdio (default; how Claude Code launches it via .mcp.json)
    else:
        if _auth_settings is None and not args.no_auth:
            ap.error(
                "--http requires FusionAuth: set FUSIONAUTH_BASE_URL and MCP_RESOURCE_URL "
                "(see auth.py for all vars), or pass --no-auth to run unauthenticated on a "
                "trusted network."
            )
        if _auth_settings is not None:
            print(f"[auth] FusionAuth enabled (issuer {_auth_settings.issuer_url}, "
                  f"resource {_auth_settings.resource_server_url})")
        else:
            print("[WARN] Serving with NO authentication (--no-auth). Do not expose publicly.")
        mcp.settings.host = args.host
        mcp.settings.port = args.port
        mcp.run(transport="streamable-http")
