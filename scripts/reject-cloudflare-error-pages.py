#!/usr/bin/env python3
"""Make Upptime record HTTP-200 Cloudflare tunnel error pages as down."""

from pathlib import Path
import re
import urllib.request

config_path = Path(".upptimerc.yml")
config = config_path.read_text()
patterns = re.compile(
    rb"cloudflare tunnel error|error code:\s*(?:502|1033)|cf-error-details|"
    rb"unable to reach the origin service",
    re.IGNORECASE,
)

for url in re.findall(r"^\s+url:\s+(https://\S+)\s*$", config, re.MULTILINE):
    try:
        request = urllib.request.Request(url, headers={"User-Agent": "Gelaxiz-Upptime-Origin-Check"})
        with urllib.request.urlopen(request, timeout=20) as response:
            body = response.read(512_000)
    except Exception:
        continue  # Upptime handles ordinary HTTP/network failures itself.

    if patterns.search(body):
        replacement = "http://127.0.0.1:1/cloudflare-origin-down"
        config = re.sub(
            rf"(^\s+url:\s+){re.escape(url)}(\s*$)",
            rf"\g<1>{replacement}\g<2>",
            config,
            flags=re.MULTILINE,
        )
        print(f"Cloudflare error page detected: {url}")

config_path.write_text(config)
