# Candidate C, FINAL tier (~100 div): Archmage Ball Lightning of Orbiting
# Volatiled MotC 36/36 -> only 4 Aylardex charges needed for 100%; we run 8
# (3 base + 3 tree + 1 CoP + 1 Aylardex) = 104% MoM: 4-charge loss tolerance,
# frees wand slot (real caster wand) and both corrupt slots.
# Volatiled FoT 45/45 + DF 50 + BBD 10 = 105% conversion (res-pen safe).
# Ralakesh Power variant: charges never drop (100% MoM + shock immunity locked).
# 100% MoM: 40 keystone + 10 Divine Guidance + 10 Clarity WE + 10 Aylardex (10 PC)
#           + 30/30 Foulborn MotC
# Charges (10): 3 base + 1 Aylardex + 1 Conviction of Power + 3 tree notables
#           + 1 Void Battery + 1 MotC helmet corruption
# Conversion: DF 50 + FoT 40 + BBD 10 (4 Hunter rares)
# Shock immunity: Charge Mastery (at max power charges)

LEVEL = 97

# Tree targets (see harness/tree_path.lua find):
# chassis: MoM 34098, CI 11455, Pain Attunement 31703 (-> Divine Flesh via GV),
#          GV socket 41263, EO 22088
# ascendancy: 30940 start, 922 Divine Guidance, 25651 Conviction of Power,
#          29026 Sanctuary of Thought
# mana:    38516 Righteous Decree, 51108 Arcane Capacitor, 24362 Deep Thoughts,
#          27163 Arcane Will, 10115 Prodigal Perfection, 18174 Mystic Bulwark
# charges: 20528 Instability, 34173 Overcharge, 25411 Infused,
#          9261 Disciple of the Forbidden
TREE_TARGETS = "34098,11455,31703,41263,22088,38516,51108,24362,27163,10115,18174,20528,34173,25411,9261,30940,922,25651,29026"

# filled in after running tree_path.lua path 5 <TREE_TARGETS>
NODES = [922,1031,4397,7388,7938,8302,9261,10115,10490,10575,11046,11420,11455,11551,12783,12888,12913,13009,13164,14151,15405,16954,17735,17749,18174,18182,18747,19635,20528,21262,22315,22472,22637,23027,24256,24362,25411,25651,25714,26196,26270,26960,27163,27415,27564,27656,29026,29061,29199,29353,29994,30940,31703,31875,32245,32345,32710,33435,33631,33740,34098,34171,34173,34906,36634,36678,36858,37671,37999,38176,38516,39841,41251,41263,41635,42760,43000,44202,45680,46340,46726,46910,47251,48514,48778,49605,49651,50422,50570,50826,50862,51108,52789,53279,53456,54694,55993,56029,56295,57167,58402,58453,60388,60398,60440,60472,61419,61834,63447,63965]

MASTERIES = {
    34723: 14100,  # Charge Mastery: Cannot be Shocked while at maximum Power Charges
    13862: 59064,  # Mana Mastery (Prodigal Perfection group): 10% of Damage taken Recouped as Mana
    44948: 12119,  # Mana Mastery (Arcane Capacitor group): 15% increased Mana Cost Efficiency
}

ITEMS = [
    {"item": """Rarity: UNIQUE
Foulborn Mind of the Council
Harlequin Mask
LevelReq: 57
Implicits: 0
260% increased Evasion and Energy Shield
+20 to maximum Energy Shield
30% increased maximum Mana
10% chance to Shock
+20% chance to be Shocked
36% of Lightning Damage is taken from Mana before Life
36% of Physical Damage is taken from Mana before Life
Attack Skills have Added Lightning Damage equal to 6% of maximum Mana
Lose 3% of Mana when you use an Attack Skill
Corrupted""", "slot": "Helmet"},
    {"item": "aylardex", "slot": "Amulet"},
    {"item": "font_of_thunder", "slot": "Weapon 2"},
    {"item": """Rarity: RARE
Endgame Caster Wand
Profane Wand
Quality: 20
LevelReq: 68
Implicits: 1
14% increased Spell Damage
+1 to Level of all Lightning Spell Skill Gems
75% increased Spell Damage
+100 to maximum Mana
20% increased Cast Speed
Gain 8% of Lightning Damage as Extra Chaos Damage""", "slot": "Weapon 1"},
    {"item": """Rarity: UNIQUE
Lightning Coil
Desert Brigandine
Quality: 20
Sockets: B-B-B-B-B-B
LevelReq: 68
Implicits: 0
Adds 1 to 25 Lightning Damage to Attacks
110% increased Armour and Evasion
+70 to maximum Life
-60% to Lightning Resistance
50% of Physical Damage from Hits taken as Lightning Damage""", "slot": "Body Armour"},
    {"item": """Rarity: RARE
Budget Gloves
Fingerless Silk Gloves
Hunter Item
LevelReq: 70
Implicits: 0
+90 to maximum Mana
+45% to Lightning Resistance
+55 to Intelligence
+55 to Dexterity""", "slot": "Gloves"},
    {"item": """Rarity: UNIQUE
Ralakesh's Impatience
Riveted Boots
LevelReq: 36
Implicits: 0
+20% to Cold Resistance
+20% to Chaos Resistance
20% increased Movement Speed
Corrupted Blood cannot be inflicted on you
Count as having maximum number of Power Charges""", "slot": "Boots"},
    {"item": """Rarity: RARE
Budget Belt
Crystal Belt
Hunter Item
LevelReq: 79
Implicits: 1
+80 to maximum Energy Shield
+90 to maximum Mana
+55 to Intelligence
+40% to Lightning Resistance
25% increased Mana Regeneration Rate""", "slot": "Belt"},
    {"item": """Rarity: RARE
Budget Ring 1
Sapphire Ring
Hunter Item
LevelReq: 60
Implicits: 1
+100 to maximum Mana
10% increased maximum Mana
+45% to Lightning Resistance
+30 to Dexterity
8% reduced Mana Cost of Skills""", "slot": "Ring 1"},
    {"item": """Rarity: RARE
Budget Ring 2
Amethyst Ring
Hunter Item
LevelReq: 60
Implicits: 1
+17% to Chaos Resistance
+100 to maximum Mana
10% increased maximum Mana
+50 to Intelligence
+45% to Lightning Resistance
+40 to Dexterity""", "slot": "Ring 2"},
    {"item": "watchers_eye", "socketNode": 61419},
    {"item": "glorious_vanity", "socketNode": 41263},
    {"item": "bound_by_destiny", "socketNode": 26196},
    {"item": """Rarity: UNIQUE
Healthy Mind
Cobalt Jewel
Radius: Medium
LevelReq: 1
Implicits: 0
18% increased maximum Mana
Increases and Reductions to Life in Radius are Transformed to apply to Mana at 200% of their value""", "socketNode": 61834},
    {"item": """Rarity: RARE
Mind Gem
Cobalt Jewel
LevelReq: 1
Implicits: 0
8% increased maximum Mana
10% increased Lightning Damage
+16 to Dexterity
+12% to Cold Resistance""", "socketNode": 36634},
    {"item": """Rarity: RARE
Mind Gem Two
Cobalt Jewel
LevelReq: 1
Implicits: 0
10% increased maximum Mana
12% increased Lightning Damage
14% increased Mana Regeneration Rate""", "socketNode": 33631},
    {"item": """Rarity: MAGIC
Enduring Eternal Mana Flask of the Mage
Eternal Mana Flask
Quality: 20
LevelReq: 65
Implicits: 0
Flask Effect is not removed at Full Mana
8% reduced Mana Cost of Skills during Effect""", "slot": "Flask 1"},
    {"item": """Rarity: MAGIC
Granite Flask of Iron Skin
Granite Flask
Quality: 20
LevelReq: 27
Implicits: 0
60% increased Armour during Flask effect""", "slot": "Flask 2"},
    {"item": """Rarity: MAGIC
Quicksilver Flask of Adrenaline
Quicksilver Flask
Quality: 20
LevelReq: 12
Implicits: 0
25% increased Movement Speed during Flask effect""", "slot": "Flask 3"},
]

SKILLS = [
    {"slot": "Body Armour", "label": "BLoO", "mainActiveSkill": 1, "gems": [
        {"name": "Ball Lightning of Orbiting", "level": 21, "skillPart": 3},
        {"name": "Archmage", "level": 21},
        {"name": "Awakened Added Lightning Damage", "level": 5},
        {"name": "Awakened Lightning Penetration", "level": 5},
        {"name": "Concentrated Effect"},
        {"name": "Inspiration"},
    ]},
    {"slot": "Helmet", "label": "Brand: curse + exposure", "gems": [
        {"name": "Arcanist Brand"},
        {"name": "Conductivity"},
        {"name": "Wave of Conviction"},
        {"name": "Increased Duration"},
    ]},
    {"slot": "Boots", "label": "BFoT + utility", "gems": [
        {"name": "Frostblink"},
        {"name": "Clarity", "quality": 0, "level": 1},
        {"name": "Flame Dash"},
        {"name": "Arcane Surge", "level": 6},
    ]},
    {"slot": "Weapon 1", "label": "Sigil", "gems": [
        {"name": "Sigil of Power"},
        {"name": "Increased Duration"},
    ]},
    {"slot": "Gloves", "label": "Guard + EO trigger", "gems": [
        {"name": "Arcane Cloak"},
        {"name": "Increased Duration"},
        {"name": "Orb of Storms"},
        {"name": "Increased Critical Strikes"},
    ]},
]

CONFIG = {
    "enemyIsBoss": "Uber",
    "usePowerCharges": True,
    "useEnduranceCharges": True,
    "overrideEnduranceCharges": 1,
    "conditionStationary": True,
    "brandAttachedToEnemy": True,
    "buffArcaneSurge": True,
    "conditionCritRecently": True,
    "waveOfConvictionExposureType": "Lightning",
    "sigilOfPowerStages": 6,
    "multiplierManaSpentRecently": 2000,
}

OVERRIDES = {32345: "Journey Tattoo of the Mind", 56029: "Journey Tattoo of the Mind", 32245: "Journey Tattoo of the Mind", 1031: "Tattoo of the Valako Stormrider", 4397: "Tattoo of the Valako Stormrider", 7388: "Tattoo of the Hinekora Shaman", 7938: "Tattoo of the Hinekora Shaman", 10490: "Tattoo of the Hinekora Shaman", 10575: "Tattoo of the Hinekora Shaman", 11551: "Tattoo of the Hinekora Shaman", 14151: "Tattoo of the Hinekora Shaman", 17735: "Tattoo of the Hinekora Shaman", 18182: "Tattoo of the Hinekora Shaman", 19635: "Tattoo of the Hinekora Shaman", 26270: "Tattoo of the Hinekora Shaman", 27415: "Tattoo of the Valako Warrior", 27564: "Tattoo of the Valako Warrior", 27656: "Tattoo of the Valako Warrior", 29199: "Tattoo of the Valako Warrior", 32710: "Tattoo of the Valako Warrior", 36678: "Tattoo of the Valako Warrior", 36858: "Tattoo of the Valako Warrior", 37671: "Tattoo of the Valako Warrior", 37999: "Tattoo of the Valako Warrior", 38176: "Tattoo of the Valako Warrior"}

SPEC = {
    "level": LEVEL,
    "bandit": "None",
    "pantheonMajor": "TheBrineKing",
    "pantheonMinor": "Ralakesh",
    "nodes": NODES,
    "overrides": OVERRIDES,
    "masteries": MASTERIES,
    "items": ITEMS,
    "skills": SKILLS,
    "config": CONFIG,
    "mainSocketGroup": 1,
}
