-- run_build.lua: headless PoB driver
-- Usage (cwd must be pob/src):
--   luajit /path/to/run_build.lua <build.xml> [out.json]
-- Boots the full PoB calc engine via HeadlessWrapper, loads the build XML,
-- and writes a JSON dump of the player stats table.

local xmlPath = arg and arg[1]
local outPath = arg and arg[2]
if not xmlPath then
	print("usage: luajit run_build.lua <build.xml> [out.json]")
	os.exit(1)
end

dofile("HeadlessWrapper.lua")

-- HeadlessWrapper stubs NewFileSearch/GetScriptPath, which breaks the lazy
-- timeless-jewel data loader (silently deallocating the whole passive tree
-- when a timeless jewel is socketed). Provide working implementations; the
-- .bin files must be pre-decompressed by setup.sh since Inflate is stubbed.
function GetScriptPath()
	return "."
end
function NewFileSearch(spec)
	local escaped = spec:gsub("'", "'\\''")
	local p = io.popen("ls -1 '" .. escaped .. "' 2>/dev/null || ls -1 " .. spec .. " 2>/dev/null")
	local files = { }
	if p then
		for line in p:lines() do
			files[#files + 1] = line
		end
		p:close()
	end
	if #files == 0 then
		return nil
	end
	local idx = 1
	local h = { }
	function h:GetFileName()
		return files[idx]:match("[^/]+$")
	end
	function h:GetFileModifiedTime()
		local q = io.popen('stat -c %Y "' .. files[idx] .. '" 2>/dev/null')
		local t = q and tonumber(q:read("*a"))
		if q then q:close() end
		return t or 0
	end
	function h:NextFile()
		idx = idx + 1
		return files[idx] ~= nil
	end
	return h
end

local f = assert(io.open(xmlPath, "r"), "cannot open " .. xmlPath)
local xmlText = f:read("*a")
f:close()

loadBuildFromXML(xmlText, "harness")
-- A few extra frames so deferred calc passes (e.g. Full DPS) settle
for _ = 1, 3 do
	runCallback("OnFrame")
end

local dkjson = require("dkjson")

-- mainOutput is mostly flat scalars; copy those. Nested tables are either
-- breakdowns or internal refs with cycles, so skip everything non-scalar.
local function scalars(tbl)
	local out = {}
	for k, v in pairs(tbl or {}) do
		local t = type(v)
		if t == "number" or t == "string" or t == "boolean" then
			-- JSON can't hold inf/nan; stringify them
			if t == "number" and (v ~= v or v == math.huge or v == -math.huge) then
				out[k] = tostring(v)
			else
				out[k] = v
			end
		end
	end
	return out
end

local mainOutput = build.calcsTab.mainOutput or {}

-- Curated summary of the numbers we compare builds on
local CURATED = {
	-- offense
	"TotalDPS", "TotalDot", "CombinedDPS", "FullDPS", "WithPoisonDPS",
	"AverageDamage", "Speed", "CritChance", "CritMultiplier", "HitChance",
	-- cost & sustain
	"ManaCost", "ManaPercentCost", "ManaPerSecondCost", "ManaUnreserved",
	"ManaRegenRecovery", "LifeCost", "RageCost",
	-- pools
	"Life", "LifeUnreserved", "EnergyShield", "Ward", "TotalEHP",
	"LifeRegenRecovery", "LifeLeechGainRate", "NetLifeRegen",
	-- mitigation
	"Armour", "PhysicalDamageReduction", "Evasion", "MeleeEvadeChance",
	"BlockChance", "SpellBlockChance", "SpellSuppressionChance",
	"PhysicalMaximumHitTaken", "FireMaximumHitTaken", "ColdMaximumHitTaken",
	"LightningMaximumHitTaken", "ChaosMaximumHitTaken",
	-- resists
	"FireResist", "ColdResist", "LightningResist", "ChaosResist",
	"FireResistOverCap", "ColdResistOverCap", "LightningResistOverCap",
	-- misc
	"EffectiveMovementSpeedMod",
}
local curated = {}
for _, k in ipairs(CURATED) do
	local v = mainOutput[k]
	if type(v) == "number" and (v ~= v or v == math.huge or v == -math.huge) then
		v = tostring(v)
	end
	curated[k] = v
end

-- Identify the active skill so DPS numbers are attributable
local mainGroupIdx = build.mainSocketGroup
local mainGroup = build.skillsTab and build.skillsTab.socketGroupList
	and build.skillsTab.socketGroupList[mainGroupIdx]
local mainSkill
if mainGroup then
	mainSkill = mainGroup.displayLabel or mainGroup.label
end

local result = {
	buildInfo = {
		className = build.spec and build.spec.curClassName,
		ascendName = build.spec and build.spec.curAscendClassName,
		level = build.characterLevel,
		mainSocketGroup = mainGroupIdx,
		mainSkill = mainSkill,
		passivePointsUsed = (function()
			if not (build.spec and build.spec.allocNodes) then return nil end
			local c = 0
			for _, node in pairs(build.spec.allocNodes) do
				if node.type ~= "ClassStart" and node.type ~= "AscendClassStart" then
					c = c + 1
				end
			end
			return c
		end)(),
	},
	curated = curated,
	allStats = scalars(mainOutput),
}

local json = dkjson.encode(result, { indent = true })
if outPath then
	local o = assert(io.open(outPath, "w"))
	o:write(json)
	o:close()
	print("WROTE " .. outPath)
else
	print(json)
end
os.exit(0)
