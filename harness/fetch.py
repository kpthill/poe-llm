#!/usr/bin/env python3
"""Polite fetcher for community sites (poe.ninja, poewiki, poedb, ...).

All HTTP requests in this project MUST go through this script. It:
  - checks the target host's robots.txt (cached per host) and refuses
    disallowed paths;
  - enforces a global rate limit of one request per 5 seconds per host
    (persisted across invocations), sleeping as needed;
  - sends a honest descriptive User-Agent.

pobb.in is hard-blocked for programmatic use: its robots.txt disallows
/api/, /pob/ and the raw/json/xml endpoints, which is everything we'd want.

Usage: fetch.py URL [OUTFILE]
Prints body to stdout (or writes OUTFILE); exits 3 if robots.txt disallows.
"""
import json
import sys
import time
import urllib.robotparser
from pathlib import Path
from urllib.parse import urlsplit
from urllib.request import Request, urlopen

STATE_DIR = Path(__file__).parent / ".fetch-state"
UA = "poe-llm-build-harness/1.0 (personal project; kevin.patrick.thill@gmail.com)"
MIN_INTERVAL = 5.0
HARD_BLOCKED_HOSTS = {"pobb.in"}


def robots_for(host: str, scheme: str) -> urllib.robotparser.RobotFileParser:
    cache = STATE_DIR / f"robots_{host}.txt"
    rp = urllib.robotparser.RobotFileParser()
    if not cache.exists():
        wait_turn(host)  # robots fetch counts against the rate limit too
        try:
            req = Request(f"{scheme}://{host}/robots.txt", headers={"User-Agent": UA})
            with urlopen(req, timeout=20) as r:
                body = r.read().decode("utf-8", "replace")
        except Exception:
            body = ""  # 404/error => no restrictions
        cache.write_text(body)
        stamp(host)
    rp.parse(cache.read_text().splitlines())
    return rp


def _stamp_file(host: str) -> Path:
    return STATE_DIR / f"last_{host}.json"


def wait_turn(host: str) -> None:
    f = _stamp_file(host)
    if f.exists():
        last = json.loads(f.read_text())["t"]
        delta = time.time() - last
        if delta < MIN_INTERVAL:
            time.sleep(MIN_INTERVAL - delta)


def stamp(host: str) -> None:
    _stamp_file(host).write_text(json.dumps({"t": time.time()}))


def fetch(url: str) -> bytes:
    parts = urlsplit(url)
    host = parts.netloc.lower()
    STATE_DIR.mkdir(exist_ok=True)
    if host in HARD_BLOCKED_HOSTS:
        sys.exit(f"REFUSED: {host} robots.txt disallows programmatic access")
    rp = robots_for(host, parts.scheme)
    if not rp.can_fetch(UA, url) or not rp.can_fetch("*", url):
        sys.exit(3)
    wait_turn(host)
    req = Request(url, headers={"User-Agent": UA})
    try:
        with urlopen(req, timeout=30) as r:
            return r.read()
    finally:
        stamp(host)


def main() -> None:
    if len(sys.argv) not in (2, 3):
        sys.exit(__doc__)
    body = fetch(sys.argv[1])
    if len(sys.argv) == 3:
        Path(sys.argv[2]).write_bytes(body)
        print(f"WROTE {sys.argv[2]} ({len(body)} bytes)", file=sys.stderr)
    else:
        sys.stdout.buffer.write(body)


if __name__ == "__main__":
    main()
