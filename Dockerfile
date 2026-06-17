# azure-calc MCP server — streamable-HTTP, headless Chromium, FusionAuth (OIDC) auth.
#
# Build:  docker build -t azure-calc-mcp .
# Run:    docker run -d --name azure-calc -p 8000:8000 \
#           -e FUSIONAUTH_BASE_URL="https://auth.acme.com" \
#           -e MCP_RESOURCE_URL="https://mcp.acme.com" \
#           -e FUSIONAUTH_AUDIENCE="<fusionauth-application-client-id>" \
#           -v "$PWD/Azure_Estimates:/app/Azure_Estimates" \
#           azure-calc-mcp
# Tokens are validated against FusionAuth's JWKS; the server advertises itself as
# an OAuth protected resource at /.well-known/oauth-protected-resource.
# Endpoint: http://<vm-ip>:8000/mcp   (health: GET /healthz, no auth)
FROM python:3.12-slim-bookworm

# Debian's chromium + matching chromium-driver: no runtime download, versions stay in sync.
RUN apt-get update && apt-get install -y --no-install-recommends \
        chromium \
        chromium-driver \
        ca-certificates \
        fonts-liberation \
    && rm -rf /var/lib/apt/lists/*

# uv for dependency resolution from the committed lockfile.
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

ENV CHROME_BIN=/usr/bin/chromium \
    CHROMEDRIVER_PATH=/usr/bin/chromedriver \
    CHROME_NO_SANDBOX=1 \
    UV_LINK_MODE=copy \
    UV_PROJECT_ENVIRONMENT=/app/.venv \
    PYTHONUNBUFFERED=1

WORKDIR /app

# Install deps first (cached) using only the manifest + lockfile.
COPY pyproject.toml uv.lock ./
RUN uv sync --frozen --no-dev

# App code.
COPY . .

# Where exported xlsx land; mount a volume here to keep them.
RUN mkdir -p /app/Azure_Estimates
EXPOSE 8000

# FusionAuth env vars (FUSIONAUTH_BASE_URL, MCP_RESOURCE_URL, ...) must be
# supplied at `docker run` time; without them --http refuses to start.
CMD ["uv", "run", "--no-sync", "mcp_server.py", \
     "--http", "--host", "0.0.0.0", "--port", "8000"]
