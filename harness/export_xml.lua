-- export_xml.lua: load a build XML into PoB, then write back PoB's OWN
-- serialization (build:SaveDB("code") - what the desktop "Generate Code"
-- button uses). Import sites like pobb.in parse this shape strictly, so
-- hand-built XML must be normalized through here before encoding.
-- Usage (cwd pob/src): luajit export_xml.lua <in.xml> <out.xml>

local inPath, outPath = arg[1], arg[2]
assert(inPath and outPath, "usage: export_xml.lua <in.xml> <out.xml>")

dofile("HeadlessWrapper.lua")

function GetScriptPath()
	return "."
end
function NewFileSearch(spec)
	local escaped = spec:gsub("'", "'\\''")
	local p = io.popen("ls -1 '" .. escaped .. "' 2>/dev/null || ls -1 " .. spec .. " 2>/dev/null")
	local files = { }
	if p then
		for line in p:lines() do files[#files + 1] = line end
		p:close()
	end
	if #files == 0 then return nil end
	local idx = 1
	local h = { }
	function h:GetFileName() return files[idx]:match("[^/]+$") end
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

local f = assert(io.open(inPath, "r"))
local xmlText = f:read("*a")
f:close()

loadBuildFromXML(xmlText, "export")
for _ = 1, 3 do
	runCallback("OnFrame")
end

local outText = build:SaveDB("code")
assert(outText and #outText > 0, "SaveDB returned nothing")
local o = assert(io.open(outPath, "w"))
o:write(outText)
o:close()
print("EXPORTED " .. outPath .. " (" .. #outText .. " bytes)")
os.exit(0)
