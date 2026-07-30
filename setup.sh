#!/bin/bash
# Bootstrap the headless Path of Building environment from a clean Ubuntu box.
set -euo pipefail
cd "$(dirname "$0")"

apt-get install -y luajit libluajit-5.1-dev luarocks
luarocks --lua-version 5.1 install luautf8

if [ ! -d pob ]; then
    git clone --depth 1 --branch dev \
        https://github.com/PathOfBuildingCommunity/PathOfBuilding.git pob
fi

# Pre-decompress timeless-jewel lookup tables: HeadlessWrapper stubs Inflate,
# so the harness needs the .bin files on disk (they are raw zlib streams).
python3 - <<'PYEOF'
import zlib, glob
d = "pob/src/Data/TimelessJewelData/"
parts = sorted(glob.glob(d + "GloriousVanity.zip.part*"))
if parts:
    open(d + "GloriousVanity.bin", "wb").write(
        zlib.decompress(b"".join(open(p, "rb").read() for p in parts)))
for z in glob.glob(d + "*.zip"):
    open(z[:-4] + ".bin", "wb").write(zlib.decompress(open(z, "rb").read()))
PYEOF

echo "Smoke test:"
harness/run.sh builds/smoke_test.xml | tail -1
