# FRESH_KY FLAT UPLOAD BUNDLE

This is a flat-folder package of the FRESH_KY canon, ready to drag-and-drop upload into a Claude project's knowledge base. 59 files, no subdirectories.

## Naming convention

Each file is prefixed with its original folder path, underscore-joined:

| Original path | Flat filename |
|---|---|
| `archive/CORRECTIONS.md` | `archive_CORRECTIONS.md` |
| `prose/NARRATOR.md` | `prose_NARRATOR.md` |
| `prose/places/phoenix_hollow.md` | `prose_places_phoenix_hollow.md` |
| `prose/voices/alex_wilson.md` | `prose_voices_alex_wilson.md` |
| `data/people.csv` | `data_people.csv` |

Cross-references inside the files still use the original slash notation (`archive/CORRECTIONS.md §C29`). Claude will retrieve the correct file — filename matching and semantic retrieval both work.

## What's here (59 files)

**Archive layer** (18 files) — `archive_*.md`
Canon, corrections, facts, identity, character/world reference.

**Artifacts layer** (4 files) — `artifacts_*.md`
Wikipedia-ceiling, public perception, voice spec, hookup tracker.

**Data layer** (10 files) — `data_*.csv`
People, places, chat memberships, relationships, calendar, discography, deals, media timeline, aliases, hookup tracker.

**Prose — top level** (6 files) — `prose_*.md`
NARRATOR, PRE_SCENE_GATE, FAILURE_MODES, CURRENT_STATE, STARTER_SCENE, VOICE_SAMPLES.

**Prose — places** (8 files) — `prose_places_*.md`
Phoenix Hollow, West 71st, Kensington, Villa Serena, The Stave NYC, Laurel Canyon, Keeneland, Glastonbury.

**Prose — setpieces** (1 file) — `prose_setpieces_solstice_party.md`

**Prose — voices** (11 files) — `prose_voices_*.md`
Alex, Rosie, Homer, Eleanor, Tommy, Circle, Sayre Boys, London Lot, Juilliard, La Terrazza, Staff Team.

## What's NOT here

- **`SETUP/` folder** — build documentation, phase reports, audit trail. Not needed for gameplay. If you want the paste-into-project-instructions text, that lives in `SETUP/PROJECT_INSTRUCTIONS_FIELD.md` in the original source folder.
- **Housekeeping indexes** (`INDEX.md`, `ARCHIVE_INDEX.md`) — the flat naming makes these redundant.

## Load order (paste into project instructions — already correct in PROJECT_INSTRUCTIONS_FIELD.md)

1. `archive_CORRECTIONS.md` — W1–W5 non-negotiables, C1–C53 corrections. **Load first.**
2. `prose_CURRENT_STATE.md` — story-present calibration
3. `prose_PRE_SCENE_GATE.md` — blocking checklist (Steps 1–5 including Companion Gate 2.5 and PH Rotation Ledger 2.6)
4. `prose_FAILURE_MODES.md` — FM-01 through FM-30
5. `archive_FACTS_LEDGER.md` — volatile constants, security, lore, languages, identity, PR
6. `data_calendar_2026.csv` — timeline

Scene-type branches load as needed per the gate.
