"""Health check script for Docker HEALTHCHECK and monitoring platforms."""

import json
import os
import sys
import urllib.request

HOST = os.environ.get("HOST", "127.0.0.1")
PORT = int(os.environ.get("PORT", "8000"))

URL = f"http://127.0.0.1:{PORT}/mcp"

INIT_PAYLOAD = json.dumps(
    {
        "jsonrpc": "2.0",
        "id": 1,
        "method": "initialize",
        "params": {
            "protocolVersion": "2025-03-26",
            "capabilities": {},
            "clientInfo": {"name": "healthcheck", "version": "1.0"},
        },
    }
).encode()


def main() -> int:
    try:
        req = urllib.request.Request(
            URL,
            data=INIT_PAYLOAD,
            headers={
                "Content-Type": "application/json",
                "Accept": "application/json, text/event-stream",
            },
        )
        with urllib.request.urlopen(req, timeout=5) as resp:
            if resp.status == 200:
                return 0
            return 1
    except Exception as exc:
        print(f"Health check failed: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
