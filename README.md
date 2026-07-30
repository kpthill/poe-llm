# poe-llm: PoE1 build crafting with headless Path of Building

A harness for evaluating Path of Exile 1 builds with the real
[Path of Building Community](https://github.com/PathOfBuildingCommunity/PathOfBuilding)
calculation engine, run headless under LuaJIT.

## Layout

- `setup.sh` — bootstrap: installs LuaJIT + luautf8 and clones PoB (dev branch)
  into `pob/` (gitignored).
- `harness/run.sh <build.xml> [out.json]` — evaluate a build XML through the
  full PoB calc engine; emits JSON with a curated stat summary (DPS, EHP, max
  hits, resists, sustain) plus every scalar in PoB's main output table.
- `harness/run_build.lua` — the Lua driver loaded on top of PoB's official
  `HeadlessWrapper.lua`.
- `harness/pob_codes.py encode|decode` — convert between build XML and PoB
  import codes (`base64url(zlib(xml))`); the headless wrapper stubs out
  Deflate/Inflate so this lives in Python.
- `builds/` — build XMLs under iteration.

## Notes

- PoB dev branch, tree version 3.29.
- Quivers and shields go in the `Weapon 2` slot in the XML.
- Ranger `ascendClassId`: 1 = Warden, 2 = Deadeye, 3 = Pathfinder (alternate
  ascendancies shifted ids; verify per class via `buildInfo.ascendName` in the
  harness output).
- DPS output is config-sensitive: config flags (boss type, flask/buff uptime,
  exposure, etc.) live in the `<Config>` section of the build XML.
