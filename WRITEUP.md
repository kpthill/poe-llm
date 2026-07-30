# 100% Mind over Matter Hierophant — Allflame (3.29) SC Trade

Archmage Blade Blast Hierophant with **100% of damage taken from mana before
life**, Chaos Inoculation, and Divine Flesh. Every number below was computed by
the real Path of Building engine (dev branch, 3.29 tree) running headless in
this repo; build XMLs and import codes live in `builds/`.

## The defensive core (all versions)

| Layer | Source |
|---|---|
| 40% MoM | Mind over Matter keystone |
| 10% | Hierophant: Divine Guidance |
| 10% | Watcher's Eye (Clarity: damage taken from mana) — lvl-1 Clarity suffices |
| 30→36% lightning + phys | **Foulborn Mind of the Council** (volatiled at final tier) |
| 1%/power charge | The Aylardex (Foulborn variant also grants Eldritch Battery) |
| Chaos immunity | CI (1 life; mana is the only real pool) |
| 50% ele → chaos | Divine Flesh via Glorious Vanity (Xibaqua) socketed by Pain Attunement |
| 40→41% cold/fire → lightning | Font of Thunder (volatiled 41 at final = exactly 101% conversion) |
| 10% ele → chaos | Bound by Destiny + 4 Hunter-influenced rares |
| Shock immunity | Charge Mastery: "Cannot be Shocked while at maximum Power Charges" (mandatory: MotC+FoT add +70% chance to be shocked) |
| Phys mitigation (final) | Lightning Coil: 50% of phys hits taken as lightning → absorbed by mana at 75% res |
| Bleed/CB | Power-Ralakesh gives Corrupted Blood immunity; bleed via jewel corrupt or flask craft |
| DoTs | Pantheon: Arakaali optional; regen 1–3.4k/s outpaces common boss DoTs |

**The 99% cliff is real and the engine reproduces it**: at 9 charges the phys
max hit is literally 99 damage (1% of every hit reaches the 1-life pool). Never
drop below the charge requirement. The final tier runs 36/36 volatiled MotC
with 8 charges = 104% MoM — a 4-charge safety buffer — and Power-variant
Ralakesh means charges never drop at all.

**Conversion must be ≥101%, not 100** (rounding leak, confirmed in-engine):
50 DF + 41 volatiled FoT + 10 BBD = 101. Budget runs exactly 100 (40 FoT) —
keep cold/fire res positive and expect rare edge-case leaks vs heavy
res-penetration (guide-documented; engine confirms full seal otherwise).

## Why Blade Blast won (candidate comparison, all Uber-pinnacle config)

| | Budget (~5 div, lvl 88) | Final (~100 div, lvl 97) |
|---|---|---|
| **A: Archmage Blade Blast + Bladefall of Trarthus** | **156k** | **337k** |
| C: Archmage Ball Lightning of Orbiting | 137k sustained (215k mana-negative) | ~185k sustained (283k burst) |
| B: KBoC / Power Siphon wander | ~40–60k | not built |

- **Blade Blast's DPS = per-hit damage × blades consumed/sec, independent of
  cast rate.** Bladefall of Trarthus volleys faster with more max mana
  (+2%/100 mana): ~15 blades/s at 6k mana, ~42/s at 24k, plus ~10/s from
  Arcanist-Brand-triggered EK of Lingering Blades + Returning Projectiles on
  bosses. You cast BB at a lazy ~2/s and the DPS is the same — which also
  caps Archmage's cost (5% of unreserved per cast). BLoO pays full cost for
  every DPS-cast, so at 24k mana it can only sustain ~2.5 of its 3.3 casts/s.
- **The wander scales off 6–15% of mana as flat attack damage but pays
  accuracy, crit and a 3%-max-mana loss per attack; Archmage grants 14–15.4%
  plus spell multipliers.** PoB also confirms Power Siphon of the Archmage is
  a clear skill (one projectile per enemy — only one hits a boss); the real
  wander boss tech is point-blank KB cluster overlap, quoted at ~5–6 of 8
  clusters hitting. It trails the casters everywhere.
- **Crit beats Elemental Overload on this chassis** (measured): 10 power
  charges give +500% inc crit vs Aylardex's −400% reduced, netting 25–37%
  chance, and the charge-wheel smalls add multi. EO's 40% more exactly
  cancels giving up crit (Δ +1.8%) and scales worse.

## Config assumptions behind every DPS number

Uber Pinnacle boss; power charges at max (10 budget / 8 final); endurance
charges overridden to 1 (only Conviction of Power's minimum is guaranteed);
stationary; brand attached; Conductivity (curse-effect-reduced on uber);
lightning exposure from Wave of Conviction; Sigil of Power stage 4–6; Arcane
Surge up; crit-recently (trivially true at 25%+ crit, 2+ casts/s); **no** Vaal
skills, no Arcane Cloak uptime, no shock on enemy, no flask damage mods.
Blade Blast stage count = sustainable blade generation (8/cast budget;
29/s via part-2 blade-rate model at final), never the 50-blade UI cap.

## Mapping / bossing loop

Mapping is one button + movement: Bladefall of Trarthus re-upped every 6s
rains blades around you passively; Blade Blast chains detonations across the
screen (its AoE grows per blade detonated). Flame Dash + Quicksilver for
movement. Bossing adds: drop Arcanist Brand (auto-casts Conductivity + EK
lingering blades near the boss), Wave of Conviction for exposure, Sigil of
Power, then spam BB.

## Budget version (~5 div, level 85–90)

Enablers: Foulborn MotC 5c + Foulborn Aylardex 1c + Font of Thunder 15c +
Clarity-MoM Watcher's Eye 50–100c + Bound by Destiny 2–3 div + Glorious
Vanity (Xibaqua) + Void Battery 5–10c. Charges (10): 3 base + 3 tree wheels +
Conviction of Power + Aylardex + Void Battery + **+1 power charge MotC
corrupt** (5c base — buy several and vaal them; alternatives: Foulborn
Romira's +1 PC ring at 1c if you run zero crit, or Doedre's Elixir rotations).
Rest: rare 6L ES body, Hunter-influenced mana/res rares (gloves/boots/belt/
ring), Healthy Mind jewel next to the Circle of Life wheel (life nodes → mana
at 200% under CI), Enduring Eternal Mana Flask.

Result: 156k uber DPS, 6.3k mana, ~1k regen +flask, 121k ele max hits, 16k
phys max hit, 63k EHP. Phys is the budget weak point (as the archetype guide
warns) — the Lightning Coil upgrade is the fix.

**Earliest possible switch: ~level 80** (gear caps at FoT's 64 req, but the
tree needs ~85 points for MoM+CI+Pain Attunement+charge wheels+jewel sockets).
Level 88 quoted.

## Final version (~100 div, level 97)

Upgrades in priority order (each independently testable in PoB):
1. **Journey Tattoos of the Mind ×3** on Alacrity/Agility/Expertise — the
   tattoo can ONLY replace "+30 to Dexterity" NOTABLES, of which the whole
   tree has four (the 4th, Proficiency, needs an Impossible Escape (The
   Impaler) jewel and is roughly break-even vs a rare mana jewel in the
   same socket). 3 allocated = 270 flat mana. Int travel smalls take the
   legal small-int tattoos instead: Hinekora Shaman (8% mana regen),
   Valako Stormrider (+6% lightning res), Valako Warrior (5% lightning
   damage).
2. **Volatiled MotC 36/36** → drops the charge requirement to 8 with buffer;
   frees the wand slot for a rare +1-lightning-gems caster wand and removes
   the corrupt dependency.
3. **Lightning Coil** (transforms phys max hit) — only lightning res needs
   re-capping after its -60%; fire/cold stay uncapped (see below).
4. **Power-variant Ralakesh's Impatience** (~45 div): charges never drop —
   100% MoM and shock immunity become unconditional.
5. Volatiled FoT 41+ (101% conversion), Awakened Added Lightning/Lightning
   Pen, BB 21, Archmage 21, second rare mana jewel.

Result: **337k uber DPS, 8.0k mana, 1.3k regen/s, 157k elemental max
hits, 31.7k phys max hit (comfortably tanks a Shaper slam), 127.5k EHP,
lightning res 75, chaos immune, shock immune.** Casting cadence ~2/s keeps
Archmage cost inside recovery; DPS is blade-limited (~29 blades/s at this
mana). Further scaling paths beyond this snapshot: The Adorned + magic
mana jewels, a large cluster jewel with Scintillating Idea, Impossible
Escape + Proficiency, and gem-quality/corruption min-maxing — the league
ceiling per the archetype guide is ~10k+ mana.

**Fire/cold resistance is deliberately uncapped at final tier**: at 101%
conversion nothing you take is ever fire or cold (the taken-as lines are
generic, so ground DoTs convert too), and the ~12 tattoo slots that would
cap them are worth ~4x more as Journey Tattoos. At budget (exactly 100%),
keep fire/cold positive and above enemy penetration after map mods
(~50-60 uncapped is comfortable) because of the documented rounding leak.
Freeze/chill still comes from cold *hits dealt*, so take Brine King
pantheon or a cannot-be-frozen source.

Beyond 100 div: Mageblood (res frees tattoo slots → all Journey tattoos →
~30k mana), +1% max lightning res tattoos ("of the Makanga"), double-corrupt
MotC, cluster jewels (Scintillating Idea), awakened Conc/Empower, Foulborn
Choir of the Storm experiments (mana per overcapped lightning res).

## Leveling (RF Hierophant, per preference)

1–12 generic (Rolling Magma/Freezing Pulse), 12+ **Righteous Fire** the moment
you can sustain it with Inexorable/Pious Path style regen — standard RF hiero:
life+regen tree down the Templar/Marauder wheels, Pantheon Arakaali.
Uniques that carry: Goldrim, Tabula, Wanderlust, Praxis (mana), Ashes/Leer
Cast, Cloak of Flame. Take **Divine Guidance last** of the four ascendancy
nodes (RF wants Pious Path/Sanctuary of Thought earlier; respec 2 asc points
at the switch). At maps, farm the ~5-div enabler list, then respec (gold) into
the budget tree in one sitting — the switch is binary: do NOT walk around at
95% MoM. Check each piece in PoB (`builds/bb_budget.xml`) before committing
the respec.

## Files

- `builds/codes/*.pobcode.txt` — paste into PoB "Import from code"
- `builds/specs/*.py` — regenerate XMLs via `python3 harness/mkbuild.py`
- `harness/` — headless PoB eval pipeline (see README)

Known modeling caveats: budget rare rolls are deliberately mid-tier;
tattoo prices unverified in Allflame (flag if Journey of the Mind is
expensive — build works without, at ~40% less DPS/EHP); PoB's part-2
blade-rate model assumes you keep BFoT active and stand in brand range on
bosses; Incandescent Heart volatiled and Foulborn Choir variants unexplored.
