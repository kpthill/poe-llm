# Candidate A, budget tier (~5 div): Archmage Blade Blast + Bladefall of Trarthus
# 100% MoM: 40 keystone + 10 Divine Guidance + 10 Clarity WE + 10 Aylardex (10 PC)
#           + 30/30 Foulborn MotC
# Charges (10): 3 base + 1 Aylardex + 1 Conviction of Power + 3 tree notables
#           + 1 Void Battery + 1 MotC helmet corruption
# Conversion: DF 50 + FoT 40 + BBD 10 (4 Hunter rares)
# Shock immunity: Charge Mastery (at max power charges)

LEVEL = 88

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
NODES = [922,1031,4397,7388,7938,8302,8948,9261,10115,10490,10575,11046,11420,11455,11551,12783,12888,12913,13009,13164,14151,15064,16775,16954,17735,17749,18174,18182,18747,19635,20528,22315,22472,22637,24256,24362,25411,25651,25714,26196,26270,26960,27163,27415,27564,27656,27659,29026,29061,29199,29781,29994,30940,31703,31875,31931,32710,33479,34098,34171,34173,34906,36858,37671,37999,38176,38516,41251,41263,43000,44184,45680,46910,47251,48514,48778,49605,50826,51108,52789,53279,53456,55993,56295,57167,58402,60388,60398,60440,60472,61419,61834,62303,63447,63965,63976]

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
Implicits: 1
{tags:power_charge}+1 to Maximum Power Charges
250% increased Evasion and Energy Shield
+18 to maximum Energy Shield
25% increased maximum Mana
10% chance to Shock
+20% chance to be Shocked
30% of Lightning Damage is taken from Mana before Life
30% of Physical Damage is taken from Mana before Life
Attack Skills have Added Lightning Damage equal to 6% of maximum Mana
Lose 3% of Mana when you use an Attack Skill
Corrupted""", "slot": "Helmet"},
    {"item": "aylardex", "slot": "Amulet"},
    {"item": "font_of_thunder", "slot": "Weapon 2"},
    {"item": """Rarity: UNIQUE
Void Battery
Prophecy Wand
LevelReq: 68
Implicits: 1
38% increased Spell Damage
50% reduced Spell Damage
15% increased Cast Speed
55% increased Global Critical Strike Chance
+110 to maximum Mana
+1 to Maximum Power Charges""", "slot": "Weapon 1"},
    {"item": """Rarity: RARE
Budget Body
Vaal Regalia
Quality: 20
Sockets: B-B-B-B-B-B
LevelReq: 68
Implicits: 0
+120 to maximum Energy Shield
+90 to maximum Mana
+42% to Lightning Resistance
+38% to Fire Resistance
+35% to Cold Resistance""", "slot": "Body Armour"},
    {"item": """Rarity: RARE
Budget Gloves
Fingerless Silk Gloves
Hunter Item
LevelReq: 70
Implicits: 0
+55 to maximum Mana
+35% to Lightning Resistance
+30% to Fire Resistance
+55 to Dexterity""", "slot": "Gloves"},
    {"item": """Rarity: RARE
Budget Boots
Sorcerer Boots
Hunter Item
LevelReq: 67
Implicits: 0
30% increased Movement Speed
+50 to maximum Mana
+43 to Dexterity
+35% to Cold Resistance
+30% to Lightning Resistance""", "slot": "Boots"},
    {"item": """Rarity: RARE
Budget Belt
Crystal Belt
Hunter Item
LevelReq: 79
Implicits: 1
+70 to maximum Energy Shield
+60 to maximum Mana
+35% to Fire Resistance
+30% to Cold Resistance
20% increased Mana Regeneration Rate""", "slot": "Belt"},
    {"item": """Rarity: RARE
Budget Ring 1
Sapphire Ring
Hunter Item
LevelReq: 60
Implicits: 1
+25 to maximum Energy Shield
+65 to maximum Mana
+30% to Lightning Resistance
+25% to Fire Resistance
8% increased maximum Mana
15% increased Mana Regeneration Rate""", "slot": "Ring 1"},
    {"item": """Rarity: RARE
Budget Ring 2
Amethyst Ring
LevelReq: 60
Implicits: 1
+17% to Chaos Resistance
+60 to maximum Mana
+30% to Cold Resistance
+30% to Lightning Resistance
8% increased maximum Mana
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
    {"slot": "Body Armour", "label": "BB", "mainActiveSkill": 1, "gems": [
        {"name": "Blade Blast", "skillStageCount": 10},
        {"name": "Archmage"},
        {"name": "Added Lightning Damage"},
        {"name": "Lightning Penetration"},
        {"name": "Concentrated Effect"},
        {"name": "Inspiration"},
    ]},
    {"slot": "Helmet", "label": "Boss blades + curse", "gems": [
        {"name": "Arcanist Brand"},
        {"name": "Conductivity"},
        {"name": "Ethereal Knives of Lingering Blades"},
        {"name": "Returning Projectiles"},
    ]},
    {"slot": "Boots", "label": "BFoT + utility", "gems": [
        {"name": "Bladefall of Trarthus"},
        {"name": "Clarity", "quality": 0, "level": 1},
        {"name": "Flame Dash"},
        {"name": "Arcane Surge", "level": 6},
    ]},
    {"slot": "Weapon 1", "label": "Boss buffs", "gems": [
        {"name": "Wave of Conviction"},
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
    "conditionStationary": True,
    "brandAttachedToEnemy": True,
    "buffArcaneSurge": True,
    "conditionCritRecently": True,
    "waveOfConvictionExposureType": "Lightning",
    "sigilOfPowerStages": 4,
    "multiplierManaSpentRecently": 2000,
}

SPEC = {
    "level": LEVEL,
    "bandit": "None",
    "pantheonMajor": "TheBrineKing",
    "pantheonMinor": "Ralakesh",
    "nodes": NODES,
    "masteries": MASTERIES,
    "items": ITEMS,
    "skills": SKILLS,
    "config": CONFIG,
    "mainSocketGroup": 1,
}
