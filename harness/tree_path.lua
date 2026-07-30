-- tree_path.lua: passive-tree utility over PoB's TreeData
-- Run from pob/src:
--   luajit tree_path.lua find <lua-pattern>          search nodes by name
--   luajit tree_path.lua path <classId> <id,id,...>  connected allocation from class start
--   luajit tree_path.lua near <socketNodeId> [radius] keystones/notables within jewel radius
--
-- path: greedy sequential BFS (connect nearest unreached target to the
-- growing allocated set). Ascendancy targets are pathed within their own
-- subgraph from the ascendancy start (include the start node in targets).
-- Prints the nodes= attribute value for the build XML plus point counts.

local treeFile = os.getenv("TREE_FILE") or "TreeData/3_29/tree.lua"
local tree = dofile(treeFile)

local cmd = arg[1]

local function nodeKind(n)
	if n.isKeystone then return "keystone"
	elseif n.isNotable then return "notable"
	elseif n.isMastery then return "mastery"
	elseif n.isJewelSocket then return "socket"
	elseif n.classStartIndex then return "classstart"
	elseif n.isAscendancyStart then return "ascstart"
	else return "normal" end
end

-- node xy from group position + orbit
local orbitRadii = tree.constants.orbitRadii
local skillsPerOrbit = tree.constants.skillsPerOrbit
local function nodeXY(n)
	local g = tree.groups[n.group]
	if not g then return nil end
	local r = orbitRadii[(n.orbit or 0) + 1] or 0
	local perOrbit = skillsPerOrbit[(n.orbit or 0) + 1] or 1
	local angle = 2 * math.pi * (n.orbitIndex or 0) / perOrbit
	return g.x + r * math.sin(angle), g.y - r * math.cos(angle)
end

if cmd == "find" then
	local pat = arg[2]:lower()
	for id, n in pairs(tree.nodes) do
		if type(n) == "table" and n.name and n.name:lower():find(pat) then
			local tag = nodeKind(n)
			local asc = n.ascendancyName and (" [" .. n.ascendancyName .. "]") or ""
			local stats = n.stats and table.concat(n.stats, " | ") or ""
			print(string.format("%s\t%s\t%s%s\t%s", tostring(id), tag, n.name, asc, stats))
		end
	end

elseif cmd == "near" then
	local socketId = tonumber(arg[2])
	local radius = tonumber(arg[3]) or 1500
	local s = tree.nodes[socketId]
	assert(s, "no such node")
	local sx, sy = nodeXY(s)
	for id, n in pairs(tree.nodes) do
		if type(n) == "table" and n.name and not n.ascendancyName
				and (n.isKeystone or n.isNotable) then
			local x, y = nodeXY(n)
			if x then
				local d = math.sqrt((x - sx) ^ 2 + (y - sy) ^ 2)
				if d <= radius then
					print(string.format("%d\t%s\t%s\t%.0f", id, nodeKind(n), n.name, d))
				end
			end
		end
	end

elseif cmd == "path" then
	local classId = tonumber(arg[2])
	local targets = { }
	for id in arg[3]:gmatch("[^,]+") do
		targets[#targets + 1] = tonumber(id)
	end

	-- find class start node
	local startId
	for id, n in pairs(tree.nodes) do
		if type(n) == "table" and n.classStartIndex == classId then startId = id end
	end
	assert(startId, "class start not found")

	-- build undirected adjacency; separate main tree vs ascendancy subgraph
	local adj = { }
	local function addEdge(a, b)
		adj[a] = adj[a] or { }
		adj[b] = adj[b] or { }
		adj[a][b] = true
		adj[b][a] = true
	end
	local targetSet = { }
	for _, t in ipairs(targets) do targetSet[t] = true end
	local function pathable(id)
		local n = tree.nodes[id]
		if type(n) ~= "table" or not n.name then return false end
		if n.isMastery or n.isProxy then return false end
		if n.classStartIndex and n.classStartIndex ~= classId then return false end
		-- don't route through keystones or sockets unless targeted
		if (n.isKeystone or n.isJewelSocket) and not targetSet[id] then return false end
		return true
	end
	for id, n in pairs(tree.nodes) do
		if type(n) == "table" and n.out and pathable(id) then
			for _, o in ipairs(n.out) do
				local oid = tonumber(o)
				if pathable(oid) then addEdge(id, oid) end
			end
		end
	end

	-- greedy: BFS from allocated set to nearest unreached target
	local alloc = { [startId] = true }
	local remaining = { }
	for _, t in ipairs(targets) do remaining[t] = true end
	while next(remaining) do
		local prev, dist = { }, { [0] = true }
		local queue, qi = { }, 1
		local seen = { }
		for id in pairs(alloc) do
			queue[#queue + 1] = id
			seen[id] = true
		end
		local found
		while queue[qi] do
			local cur = queue[qi]; qi = qi + 1
			if remaining[cur] then found = cur; break end
			for nb in pairs(adj[cur] or { }) do
				if not seen[nb] then
					seen[nb] = true
					prev[nb] = cur
					queue[#queue + 1] = nb
				end
			end
		end
		if not found then
			local missing = { }
			for t in pairs(remaining) do missing[#missing + 1] = tostring(t) end
			error("unreachable targets: " .. table.concat(missing, ","))
		end
		local cur = found
		while cur and not alloc[cur] do
			alloc[cur] = true
			cur = prev[cur]
		end
		remaining[found] = nil
	end

	local main, asc = { }, { }
	for id in pairs(alloc) do
		local n = tree.nodes[id]
		if id ~= startId then
			if n.ascendancyName then
				if not n.isAscendancyStart then asc[#asc + 1] = id end
			else
				main[#main + 1] = id
			end
		end
	end
	table.sort(main); table.sort(asc)
	local all = { }
	for id in pairs(alloc) do if id ~= startId then all[#all + 1] = id end end
	table.sort(all)
	print("POINTS " .. #main .. " ascendancy " .. #asc)
	print("NODES " .. table.concat(all, ","))
elseif cmd == "mastery" then
	local pat = arg[2]:lower()
	for id, n in pairs(tree.nodes) do
		if type(n) == "table" and n.isMastery and n.name:lower():find(pat) then
			print(string.format("%d\t%s\tgroup=%s", id, n.name, tostring(n.group)))
			for _, eff in ipairs(n.masteryEffects or { }) do
				print(string.format("  effect=%d\t%s", eff.effect, table.concat(eff.stats, " | ")))
			end
		end
	end

else
	print("usage: tree_path.lua find|path|near|mastery ...")
end
