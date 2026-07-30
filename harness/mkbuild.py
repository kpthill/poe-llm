#!/usr/bin/env python3
"""Assemble PoB build XMLs from Python specs.

A spec is a dict; build_xml(spec) returns the XML string. Shared chassis
pieces for the 100% MoM Hierophant live here so the three candidate builds
stay in sync when the chassis changes.
"""

CHASSIS_ITEMS = {
    "motc": """Rarity: UNIQUE
Foulborn Mind of the Council
Harlequin Mask
LevelReq: 57
Implicits: 0
250% increased Evasion and Energy Shield
+18 to maximum Energy Shield
25% increased maximum Mana
10% chance to Shock
+20% chance to be Shocked
30% of Lightning Damage is taken from Mana before Life
30% of Physical Damage is taken from Mana before Life
Attack Skills have Added Lightning Damage equal to 6% of maximum Mana
Lose 3% of Mana when you use an Attack Skill""",

    # Foulborn variant: grants Eldritch Battery (1c per Patrick)
    "aylardex": """Rarity: UNIQUE
Foulborn The Aylardex
Agate Amulet
LevelReq: 32
Implicits: 1
+20 to Strength and Intelligence
+40 to maximum Life
+60 to maximum Mana
+1 to Maximum Power Charges
10% increased Mana Regeneration Rate per Power Charge
90% increased Power Charge Duration
1% of Damage is taken from Mana before Life per Power Charge
40% reduced Critical Strike Chance per Power Charge
Eldritch Battery""",

    "font_of_thunder": """Rarity: UNIQUE
Font of Thunder
Mirrored Spiked Shield
LevelReq: 64
Implicits: 1
+5% chance to Suppress Spell Damage
450% increased Evasion and Energy Shield
30% increased Mana Regeneration Rate
+50% chance to be Shocked
40% of Cold Damage taken as Lightning Damage
40% of Fire Damage taken as Lightning Damage""",

    "watchers_eye": """Rarity: UNIQUE
Watcher's Eye
Prismatic Jewel
LevelReq: 1
Implicits: 0
6% increased maximum Energy Shield
5% increased maximum Life
5% increased maximum Mana
10% of Damage taken from Mana before Life while affected by Clarity""",

    "glorious_vanity": """Rarity: UNIQUE
Glorious Vanity
Timeless Jewel
Radius: Large
Limited to: 1 Historic
Implicits: 0
Bathed in the blood of 5000 sacrificed in the name of Xibaqua
Passives in radius are Conquered by the Vaal""",

    # Bound by Destiny: 10% ele-as-chaos needs 4 Hunter items equipped;
    # the wearer marks 4 rares as Hunter influence in their text.
    "bound_by_destiny": """Rarity: UNIQUE
Bound by Destiny
Prismatic Jewel
Limited to: 1
LevelReq: 1
Implicits: 0
10% of Elemental Damage taken as Chaos Damage if 4 Hunter Items are Equipped""",
}


def _skill_gem(g):
    attrs = f'nameSpec="{g["name"]}" enabled="{str(g.get("enabled", True)).lower()}"'
    attrs += f' level="{g.get("level", 20)}" quality="{g.get("quality", 20)}"'
    for extra in ("count", "skillStageCount", "skillPart"):
        if extra in g:
            attrs += f' {extra}="{g[extra]}"'
    return f"<Gem {attrs}/>"


def build_xml(spec):
    level = spec.get("level", 90)
    bandit = spec.get("bandit", "None")
    pantheon_major = spec.get("pantheonMajor", "Arakaali")
    pantheon_minor = spec.get("pantheonMinor", "Ralakesh")

    skills = []
    for i, grp in enumerate(spec["skills"], 1):
        gems = "\n".join(_skill_gem(g) for g in grp["gems"])
        main = f' mainActiveSkill="{grp.get("mainActiveSkill", 1)}"'
        skills.append(
            f'<Skill enabled="{str(grp.get("enabled", True)).lower()}" '
            f'label="{grp.get("label", "")}" slot="{grp.get("slot", "")}"{main}>\n{gems}\n</Skill>')
    skills_xml = "\n".join(skills)

    items_xml = []
    slots_xml = []
    sockets_xml = []
    for i, it in enumerate(spec["items"], 1):
        text = CHASSIS_ITEMS.get(it["item"], it["item"])
        items_xml.append(f'<Item id="{i}">\n{text}\n</Item>')
        if "slot" in it:
            slots_xml.append(f'<Slot name="{it["slot"]}" itemId="{i}"/>')
        if "socketNode" in it:
            sockets_xml.append(f'<Socket nodeId="{it["socketNode"]}" itemId="{i}"/>')
    items_str = "\n".join(items_xml)
    slots_str = "\n".join(slots_xml)
    sockets_str = f"<Sockets>\n{chr(10).join(sockets_xml)}\n</Sockets>" if sockets_xml else ""

    masteries = spec.get("masteries", {})
    mastery_str = ",".join(f"{{{n},{e}}}" for n, e in masteries.items())
    mastery_attr = f' masteryEffects="{mastery_str}"' if mastery_str else ""

    config_lines = []
    for name, val in spec.get("config", {}).items():
        if isinstance(val, bool):
            config_lines.append(f'<Input name="{name}" boolean="{str(val).lower()}"/>')
        elif isinstance(val, (int, float)):
            config_lines.append(f'<Input name="{name}" number="{val}"/>')
        else:
            config_lines.append(f'<Input name="{name}" string="{val}"/>')
    config_str = "\n".join(config_lines)

    nodes = ",".join(str(n) for n in spec["nodes"])

    return f"""<?xml version="1.0" encoding="UTF-8"?>
<PathOfBuilding>
<Build level="{level}" targetVersion="3_0" className="Templar" ascendClassName="Hierophant" mainSocketGroup="{spec.get("mainSocketGroup", 1)}" bandit="{bandit}" pantheonMajorGod="{pantheon_major}" pantheonMinorGod="{pantheon_minor}">
</Build>
<Skills sortGemsByDPS="false" activeSkillSet="1">
<SkillSet id="1">
{skills_xml}
</SkillSet>
</Skills>
<Tree activeSpec="1">
<Spec treeVersion="3_29" classId="5" ascendClassId="2" nodes="{nodes}"{mastery_attr}>
{sockets_str}
</Spec>
</Tree>
<Items activeItemSet="1">
{items_str}
<ItemSet id="1" useSecondWeaponSet="false">
{slots_str}
</ItemSet>
</Items>
<Config>
{config_str}
</Config>
</PathOfBuilding>
"""


if __name__ == "__main__":
    import importlib.util
    import sys
    spec_path = sys.argv[1]
    s = importlib.util.spec_from_file_location("buildspec", spec_path)
    mod = importlib.util.module_from_spec(s)
    s.loader.exec_module(mod)
    sys.stdout.write(build_xml(mod.SPEC))
