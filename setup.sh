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

echo "Smoke test:"
harness/run.sh builds/smoke_test.xml | tail -1
