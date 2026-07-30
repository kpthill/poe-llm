#!/bin/bash
# Normalize a build XML through PoB's own serializer, then emit an import code.
# Usage: harness/make_code.sh <build.xml> <out_code.txt>
set -euo pipefail
REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
IN="$(realpath "$1")"; OUT="$(realpath -m "$2")"
TMP="$(mktemp --suffix=.xml)"
cd "$REPO_ROOT/pob/src"
export LUA_PATH="./?.lua;../runtime/lua/?.lua;../runtime/lua/?/init.lua;;"
luajit "$REPO_ROOT/harness/export_xml.lua" "$IN" "$TMP" >/dev/null
python3 "$REPO_ROOT/harness/pob_codes.py" encode "$TMP" > "$OUT"
rm -f "$TMP"
echo "WROTE $OUT ($(wc -c < "$OUT") chars)"
