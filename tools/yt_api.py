#!/usr/bin/env python3
"""Thin YouTube Data API v3 client for the Tubeyou research build.

Reads the API key from the `Instructions.` file in the repo root (Guardrail 8)
so the secret never appears on a command line. Results are printed as JSON and
optionally cached under research/raw/ for the source log.

Usage:
  python3 tools/yt_api.py <endpoint> key=value [key=value ...] [--save research/raw/name.json]

Examples:
  python3 tools/yt_api.py channels forHandle=@oversimplified part=snippet,statistics
  python3 tools/yt_api.py search q="roman engineering" part=snippet type=video maxResults=10
  python3 tools/yt_api.py videos id=abc123 part=snippet,statistics,contentDetails
"""
import json
import re
import sys
import urllib.parse
import urllib.request
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
BASE = "https://www.googleapis.com/youtube/v3/"


def api_key() -> str:
    text = (REPO / "Instructions.").read_text()
    m = re.search(r"key=([A-Za-z0-9_\-]+)", text)
    if not m:
        sys.exit("API key not found in Instructions.")
    return m.group(1)


def call(endpoint: str, params: dict) -> dict:
    params = dict(params)
    params["key"] = api_key()
    url = BASE + endpoint + "?" + urllib.parse.urlencode(params)
    req = urllib.request.Request(url, headers={"Accept": "application/json"})
    with urllib.request.urlopen(req, timeout=30) as resp:
        return json.load(resp)


def main() -> None:
    args = sys.argv[1:]
    if not args:
        sys.exit(__doc__)
    endpoint = args[0]
    save = None
    params = {}
    rest = iter(args[1:])
    for a in rest:
        if a == "--save":
            save = next(rest)
        elif "=" in a:
            k, v = a.split("=", 1)
            params[k] = v
    try:
        data = call(endpoint, params)
    except urllib.error.HTTPError as e:
        body = e.read().decode()
        print(json.dumps({"http_error": e.code, "body": body[:2000]}))
        sys.exit(1)
    out = json.dumps(data, indent=1)
    if save:
        path = REPO / save
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(out)
        print(f"saved {len(out)} bytes to {save}")
        # print a compact preview
        print(json.dumps(data, separators=(",", ":"))[:1500])
    else:
        print(out)


if __name__ == "__main__":
    main()
