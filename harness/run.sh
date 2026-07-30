#!/bin/bash
# Run a build XML through headless PoB and print/write the stats JSON.
# Usage: harness/run.sh <build.xml> [out.json]
set -euo pipefail
REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
XML="$(realpath "$1")"
OUT="${2:-}"
[ -n "$OUT" ] && OUT="$(realpath -m "$OUT")"
cd "$REPO_ROOT/pob/src"
export LUA_PATH="./?.lua;../runtime/lua/?.lua;../runtime/lua/?/init.lua;;"
exec luajit "$REPO_ROOT/harness/run_build.lua" "$XML" $OUT
