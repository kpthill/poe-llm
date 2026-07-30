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
		passivePointsUsed = build.spec and build.spec.allocatedNodeCount,
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
