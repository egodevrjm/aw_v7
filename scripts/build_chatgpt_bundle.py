#!/usr/bin/env python3
from __future__ import annotations

import csv
import re
import shutil
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUT_DIR = ROOT / "ChatGPT"
ASSETS_DIR = OUT_DIR / "assets"


TEXT_OUTPUTS: list[str] = [
    "00_START_HERE.md",
    "01_RUNTIME_RULES.md",
    "02_ALEX_AND_HOUSEHOLD.md",
    "03_SOCIAL_CIRCLES_AND_VOICES.md",
    "04_PLACES_AND_SETPIECES.md",
    "05_ENTERPRISE_AND_OPERATIONS.md",
    "06_PUBLIC_LAYER_AND_MUSIC.md",
    "07_STRUCTURED_REGISTRIES.md",
    "08_TIMELINE_AND_FORWARD_STATE.md",
    "09_VISUAL_REFERENCE.md",
]


OUTPUT_TITLES = {
    "00_START_HERE.md": "Start Here",
    "01_RUNTIME_RULES.md": "Runtime Rules",
    "02_ALEX_AND_HOUSEHOLD.md": "Alex and Household",
    "03_SOCIAL_CIRCLES_AND_VOICES.md": "Social Circles and Voices",
    "04_PLACES_AND_SETPIECES.md": "Places and Setpieces",
    "05_ENTERPRISE_AND_OPERATIONS.md": "Enterprise and Operations",
    "06_PUBLIC_LAYER_AND_MUSIC.md": "Public Layer and Music",
    "07_STRUCTURED_REGISTRIES.md": "Structured Registries",
    "08_TIMELINE_AND_FORWARD_STATE.md": "Timeline and Forward State",
    "09_VISUAL_REFERENCE.md": "Visual Reference",
}


TEXT_MAPPING: dict[str, list[str]] = {
    "01_RUNTIME_RULES.md": [
        "prose_CURRENT_STATE.md",
        "prose_PRE_SCENE_GATE.md",
        "prose_NARRATOR.md",
        "prose_FAILURE_MODES.md",
        "prose_STARTER_SCENE.md",
        "archive_CORRECTIONS.md",
        "archive_SESSION_CORRECTIONS.md",
    ],
    "02_ALEX_AND_HOUSEHOLD.md": [
        "archive_BRIEFING_NOTE.md",
        "archive_ALEX_STYLE.md",
        "archive_ALEX_COCKTAILS.md",
        "archive_AW_COLLECTION.md",
        "prose_voices_alex_wilson.md",
        "prose_voices_rosie_walker.md",
        "prose_voices_homer_wilson.md",
        "prose_voices_eleanor_vance.md",
        "prose_voices_tommy_crawford.md",
        "prose_voices_staff_team.md",
    ],
    "03_SOCIAL_CIRCLES_AND_VOICES.md": [
        "prose_VOICE_SAMPLES.md",
        "prose_voices_circle.md",
        "prose_voices_sayre_boys.md",
        "prose_voices_london_lot.md",
        "prose_voices_juilliard.md",
        "prose_voices_la_terrazza.md",
        "archive_CIRCLE.md",
        "archive_LONDON_LOT.md",
        "archive_NEW_YORK_LOT.md",
        "archive_SAYRE_BOYS.md",
        "archive_WESTMINSTER_YEARS.md",
    ],
    "04_PLACES_AND_SETPIECES.md": [
        "prose_places_phoenix_hollow.md",
        "prose_places_west_71st_nyc.md",
        "prose_places_kensington.md",
        "prose_places_villa_serena.md",
        "prose_places_the_stave_nyc.md",
        "prose_places_laurel_canyon.md",
        "prose_places_keeneland.md",
        "prose_places_glastonbury.md",
        "prose_setpieces_solstice_party.md",
    ],
    "05_ENTERPRISE_AND_OPERATIONS.md": [
        "archive_WALKER_HOLDINGS.md",
        "archive_AW_HOLDINGS.md",
        "archive_HATFIELD_LICENSING.md",
        "archive_HATFIELD_LIMESTONE.md",
        "archive_COLLINS_IDENTITY.md",
    ],
    "06_PUBLIC_LAYER_AND_MUSIC.md": [
        "archive_FACTS_LEDGER.md",
        "archive_FACT_SHEET.md",
        "archive_DISCOGRAPHY.md",
        "artifacts_WIKIPEDIA.md",
        "artifacts_PUBLIC_PERCEPTION.md",
        "artifacts_VOICE_SPEC.md",
        "artifacts_WILSON_HOOKUP_TRACKER.md",
    ],
    "07_STRUCTURED_REGISTRIES.md": [
        "data_people.csv",
        "data_places.csv",
        "data_relationships.csv",
        "data_chat_memberships.csv",
        "data_aliases.csv",
        "data_business_deals.csv",
    ],
    "08_TIMELINE_AND_FORWARD_STATE.md": [
        "data_calendar_2025_background.csv",
        "data_calendar_2026.csv",
        "data_discography.csv",
        "data_media_coverage_timeline.csv",
        "data_wilson_hookup_tracker.csv",
        "archive_FORWARD_STATE.md",
    ],
}


IMAGE_FILES = [
    "alex_bedroom_ph - 01.png",
    "alex_pool_ph - 01.png",
    "alex_rooms_ph - 01.png",
    "kensington_townhouse - 01.png",
    "ny_townhouse - 01.png",
    "phoenix_hollow - 01.png",
    "villa_serena.png",
    "villa_serena_sheet.png",
]


IMAGE_NOTES = {
    "alex_bedroom_ph - 01.png": "Alex bedroom visual reference. Cross-reference with household, wardrobe, and compound material.",
    "alex_pool_ph - 01.png": "Pool-side visual reference for Phoenix Hollow domestic life.",
    "alex_rooms_ph - 01.png": "Additional Phoenix Hollow room sheet for interior calibration.",
    "kensington_townhouse - 01.png": "Kensington townhouse visual reference. Pair with place details for London scenes.",
    "ny_townhouse - 01.png": "West 71st townhouse visual reference for NYC home scenes.",
    "phoenix_hollow - 01.png": "Phoenix Hollow visual reference and atmosphere anchor.",
    "villa_serena.png": "Villa Serena exterior visual reference for Sardinia scenes.",
    "villa_serena_sheet.png": "Villa Serena sheet-style reference with broader layout cues.",
}


LEGACY_PATHS = {
    "00_INDEX.md": "00_START_HERE.md",
    "00_README.md": "00_START_HERE.md",
    "README.md": "00_START_HERE.md",
    "PROJECT_INSTRUCTIONS_FIELD.md": "00_START_HERE.md",
}

for output_name, sources in TEXT_MAPPING.items():
    for source in sources:
        LEGACY_PATHS[source] = output_name


LEGACY_SLASH_PATHS = {
    "archive/CORRECTIONS.md": "01_RUNTIME_RULES.md",
    "archive/SESSION_CORRECTIONS.md": "01_RUNTIME_RULES.md",
    "prose/CURRENT_STATE.md": "01_RUNTIME_RULES.md",
    "prose/PRE_SCENE_GATE.md": "01_RUNTIME_RULES.md",
    "prose/NARRATOR.md": "01_RUNTIME_RULES.md",
    "prose/FAILURE_MODES.md": "01_RUNTIME_RULES.md",
    "prose/STARTER_SCENE.md": "01_RUNTIME_RULES.md",
    "archive/BRIEFING_NOTE.md": "02_ALEX_AND_HOUSEHOLD.md",
    "archive/ALEX_CORE.md": "02_ALEX_AND_HOUSEHOLD.md",
    "archive/ALEX_STYLE.md": "02_ALEX_AND_HOUSEHOLD.md",
    "archive/ALEX_COCKTAILS.md": "02_ALEX_AND_HOUSEHOLD.md",
    "archive/AW_COLLECTION.md": "02_ALEX_AND_HOUSEHOLD.md",
    "archive/ALEX_MUSIC.md": "06_PUBLIC_LAYER_AND_MUSIC.md",
    "prose/VOICE_SAMPLES.md": "03_SOCIAL_CIRCLES_AND_VOICES.md",
    "prose/voices/": "03_SOCIAL_CIRCLES_AND_VOICES.md",
    "/FRESH/prose/voices/": "03_SOCIAL_CIRCLES_AND_VOICES.md",
    "GROUP_CHAT_ARCHITECTURE.md": "03_SOCIAL_CIRCLES_AND_VOICES.md",
    "prose/voices/GROUP_CHAT_ARCHITECTURE.md": "03_SOCIAL_CIRCLES_AND_VOICES.md",
    "prose/voices/alex_wilson.md": "02_ALEX_AND_HOUSEHOLD.md",
    "prose/voices/rosie_walker.md": "02_ALEX_AND_HOUSEHOLD.md",
    "prose/voices/homer_wilson.md": "02_ALEX_AND_HOUSEHOLD.md",
    "prose/voices/eleanor_vance.md": "02_ALEX_AND_HOUSEHOLD.md",
    "prose/voices/tommy_crawford.md": "02_ALEX_AND_HOUSEHOLD.md",
    "prose/voices/staff_team.md": "02_ALEX_AND_HOUSEHOLD.md",
    "prose/voices/circle.md": "03_SOCIAL_CIRCLES_AND_VOICES.md",
    "prose/voices/sayre_boys.md": "03_SOCIAL_CIRCLES_AND_VOICES.md",
    "prose/voices/london_lot.md": "03_SOCIAL_CIRCLES_AND_VOICES.md",
    "prose/voices/juilliard.md": "03_SOCIAL_CIRCLES_AND_VOICES.md",
    "prose/voices/la_terrazza.md": "03_SOCIAL_CIRCLES_AND_VOICES.md",
    "archive/CIRCLE.md": "03_SOCIAL_CIRCLES_AND_VOICES.md",
    "archive/LONDON_LOT.md": "03_SOCIAL_CIRCLES_AND_VOICES.md",
    "archive/NEW_YORK_LOT.md": "03_SOCIAL_CIRCLES_AND_VOICES.md",
    "archive/SAYRE_BOYS.md": "03_SOCIAL_CIRCLES_AND_VOICES.md",
    "archive/WESTMINSTER_YEARS.md": "03_SOCIAL_CIRCLES_AND_VOICES.md",
    "prose/places/phoenix_hollow.md": "04_PLACES_AND_SETPIECES.md",
    "prose/places/west_71st_nyc.md": "04_PLACES_AND_SETPIECES.md",
    "prose/places/kensington.md": "04_PLACES_AND_SETPIECES.md",
    "prose/places/villa_serena.md": "04_PLACES_AND_SETPIECES.md",
    "prose/places/the_stave_nyc.md": "04_PLACES_AND_SETPIECES.md",
    "prose/places/laurel_canyon.md": "04_PLACES_AND_SETPIECES.md",
    "prose/places/keeneland.md": "04_PLACES_AND_SETPIECES.md",
    "prose/places/glastonbury.md": "04_PLACES_AND_SETPIECES.md",
    "prose/setpieces/solstice_party.md": "04_PLACES_AND_SETPIECES.md",
    "archive/WALKER_HOLDINGS.md": "05_ENTERPRISE_AND_OPERATIONS.md",
    "archive/AW_HOLDINGS.md": "05_ENTERPRISE_AND_OPERATIONS.md",
    "archive/HATFIELD_LICENSING.md": "05_ENTERPRISE_AND_OPERATIONS.md",
    "archive/HATFIELD_LIMESTONE.md": "05_ENTERPRISE_AND_OPERATIONS.md",
    "archive/COLLINS_IDENTITY.md": "05_ENTERPRISE_AND_OPERATIONS.md",
    "archive/FACTS_LEDGER.md": "06_PUBLIC_LAYER_AND_MUSIC.md",
    "archive/FACT_SHEET.md": "06_PUBLIC_LAYER_AND_MUSIC.md",
    "archive/DISCOGRAPHY.md": "06_PUBLIC_LAYER_AND_MUSIC.md",
    "artifacts/WIKIPEDIA.md": "06_PUBLIC_LAYER_AND_MUSIC.md",
    "artifacts/PUBLIC_PERCEPTION.md": "06_PUBLIC_LAYER_AND_MUSIC.md",
    "artifacts/VOICE_SPEC.md": "06_PUBLIC_LAYER_AND_MUSIC.md",
    "artifacts/WILSON_HOOKUP_TRACKER.md": "06_PUBLIC_LAYER_AND_MUSIC.md",
    "data/people.csv": "07_STRUCTURED_REGISTRIES.md",
    "data/places.csv": "07_STRUCTURED_REGISTRIES.md",
    "data/relationships.csv": "07_STRUCTURED_REGISTRIES.md",
    "data/chat_memberships.csv": "07_STRUCTURED_REGISTRIES.md",
    "data/aliases.csv": "07_STRUCTURED_REGISTRIES.md",
    "data/business_deals.csv": "07_STRUCTURED_REGISTRIES.md",
    "data/calendar_2025_background.csv": "08_TIMELINE_AND_FORWARD_STATE.md",
    "data/calendar_2026.csv": "08_TIMELINE_AND_FORWARD_STATE.md",
    "data/discography.csv": "08_TIMELINE_AND_FORWARD_STATE.md",
    "data/media_coverage_timeline.csv": "08_TIMELINE_AND_FORWARD_STATE.md",
    "data/wilson_hookup_tracker.csv": "08_TIMELINE_AND_FORWARD_STATE.md",
    "archive/FORWARD_STATE.md": "08_TIMELINE_AND_FORWARD_STATE.md",
}


@dataclass(frozen=True)
class SourceRecord:
    source: str
    target: str
    kind: str


def slugify(name: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", name.lower()).strip("-")


def replace_legacy_refs(text: str) -> str:
    replacements = []
    for source, target in LEGACY_PATHS.items():
        replacements.append((source, target))
    for source, target in LEGACY_SLASH_PATHS.items():
        replacements.append((source, target))

    # Replace longer strings first to avoid partial substitutions.
    for source, target in sorted(replacements, key=lambda item: len(item[0]), reverse=True):
        text = text.replace(source, target)
    return text


def read_text(relative_path: str) -> str:
    return (ROOT / relative_path).read_text(encoding="utf-8").rstrip() + "\n"


def render_text_bundle(output_name: str, sources: list[str]) -> str:
    parts = [
        f"# {OUTPUT_TITLES[output_name]}",
        "",
        "This file is part of the ChatGPT-optimized bundle generated from the current `aw_v7` source files.",
        "",
        "## Included Sources",
        "",
    ]
    for source in sources:
        parts.append(f"- `{source}`")
    parts.append("")

    for source in sources:
        body = replace_legacy_refs(read_text(source)).rstrip()
        section_id = slugify(source)
        parts.extend(
            [
                "---",
                "",
                f"## Source: `{source}` {{#{section_id}}}",
                "",
                f"Original source file preserved below. Legacy references now point to the consolidated ChatGPT bundle when possible.",
                "",
                body,
                "",
            ]
        )
    return "\n".join(parts).rstrip() + "\n"


def render_csv_section(source: str) -> str:
    path = ROOT / source
    with path.open(newline="", encoding="utf-8") as handle:
        reader = list(csv.reader(handle))

    header = reader[0]
    rows = reader[1:]
    preview_rows = rows[:8]
    section_id = slugify(source)

    parts = [
        "---",
        "",
        f"## Source: `{source}` {{#{section_id}}}",
        "",
        "### Columns",
        "",
        "| Column |",
        "|---|",
    ]
    parts.extend([f"| `{column}` |" for column in header])
    parts.extend(
        [
            "",
            "### Preview",
            "",
            _render_markdown_table(header, preview_rows),
            "",
            "### Full CSV",
            "",
            "```csv",
            path.read_text(encoding="utf-8").rstrip(),
            "```",
            "",
        ]
    )
    return "\n".join(parts)


def _render_markdown_table(header: list[str], rows: list[list[str]]) -> str:
    widths = [len(col) for col in header]
    for row in rows:
        for idx, value in enumerate(row):
            widths[idx] = max(widths[idx], len(value))

    def fmt_row(row: list[str]) -> str:
        return "| " + " | ".join(value.replace("\n", " ") for value in row) + " |"

    lines = [fmt_row(header), "| " + " | ".join("---" for _ in header) + " |"]
    lines.extend(fmt_row(row) for row in rows)
    return "\n".join(lines)


def render_registry_bundle() -> str:
    sources = TEXT_MAPPING["07_STRUCTURED_REGISTRIES.md"]
    parts = [
        "# Structured Registries",
        "",
        "This file preserves the structured CSV layers that support the narrative canon. Each source includes a column list, a short preview, and the full CSV payload.",
        "",
        "## Included Sources",
        "",
    ]
    for source in sources:
        parts.append(f"- `{source}`")
    parts.append("")
    for source in sources:
        parts.append(render_csv_section(source))
    return "\n".join(parts).rstrip() + "\n"


def render_timeline_bundle() -> str:
    sources = TEXT_MAPPING["08_TIMELINE_AND_FORWARD_STATE.md"]
    parts = [
        "# Timeline and Forward State",
        "",
        "This file groups the timeline-heavy CSV datasets with the narrative forward-state document so future triggers and background chronology live in one place.",
        "",
        "## Included Sources",
        "",
    ]
    for source in sources:
        parts.append(f"- `{source}`")
    parts.append("")

    for source in sources:
        if source.endswith(".csv"):
            parts.append(render_csv_section(source))
        else:
            body = replace_legacy_refs(read_text(source)).rstrip()
            section_id = slugify(source)
            parts.extend(
                [
                    "---",
                    "",
                    f"## Source: `{source}` {{#{section_id}}}",
                    "",
                    body,
                    "",
                ]
            )
    return "\n".join(parts).rstrip() + "\n"


def render_visual_reference() -> str:
    parts = [
        "# Visual Reference",
        "",
        "The original PNG assets are copied into `ChatGPT/assets/` unchanged. Use this file as the asset manifest when assembling a ChatGPT Project.",
        "",
        "## Included Assets",
        "",
        "| Asset | Notes | Related Bundle File |",
        "|---|---|---|",
    ]
    related_map = {
        "alex_bedroom_ph - 01.png": "02_ALEX_AND_HOUSEHOLD.md",
        "alex_pool_ph - 01.png": "04_PLACES_AND_SETPIECES.md",
        "alex_rooms_ph - 01.png": "04_PLACES_AND_SETPIECES.md",
        "kensington_townhouse - 01.png": "04_PLACES_AND_SETPIECES.md",
        "ny_townhouse - 01.png": "04_PLACES_AND_SETPIECES.md",
        "phoenix_hollow - 01.png": "04_PLACES_AND_SETPIECES.md",
        "villa_serena.png": "04_PLACES_AND_SETPIECES.md",
        "villa_serena_sheet.png": "04_PLACES_AND_SETPIECES.md",
    }
    for image_name in IMAGE_FILES:
        parts.append(
            f"| `assets/{image_name}` | {IMAGE_NOTES[image_name]} | `{related_map[image_name]}` |"
        )
    parts.append("")
    return "\n".join(parts).rstrip() + "\n"


def render_start_here(records: list[SourceRecord]) -> str:
    orientation_sources = ["00_INDEX.md", "00_README.md", "README.md", "PROJECT_INSTRUCTIONS_FIELD.md"]
    grouped_records: dict[str, list[str]] = {name: [] for name in TEXT_OUTPUTS}
    image_records: list[str] = []
    for record in records:
        if record.kind == "image":
            image_records.append(record.source)
        elif record.target in grouped_records:
            grouped_records[record.target].append(record.source)

    parts = [
        "# ChatGPT Bundle for `aw_v7`",
        "",
        "This folder is an additive, ChatGPT-oriented packaging layer for the live `aw_v7` repository. It preserves the existing root bundle and reorganizes the source material into 10 long Markdown files plus copied image assets.",
        "",
        "## Recommended Session Open",
        "",
        "Read these files first in this order for a fresh story session:",
        "",
        "1. `00_START_HERE.md`",
        "2. `01_RUNTIME_RULES.md`",
        "3. `02_ALEX_AND_HOUSEHOLD.md`",
        "4. `03_SOCIAL_CIRCLES_AND_VOICES.md`",
        "5. `04_PLACES_AND_SETPIECES.md`",
        "6. `06_PUBLIC_LAYER_AND_MUSIC.md`",
        "7. `08_TIMELINE_AND_FORWARD_STATE.md`",
        "",
        "Use `05_ENTERPRISE_AND_OPERATIONS.md`, `07_STRUCTURED_REGISTRIES.md`, and `09_VISUAL_REFERENCE.md` when the scene or research path needs them.",
        "",
        "## Bundle Contents",
        "",
    ]

    for output_name in TEXT_OUTPUTS[1:]:
        parts.append(f"### `{output_name}`")
        parts.append("")
        if grouped_records[output_name]:
            for source in grouped_records[output_name]:
                parts.append(f"- `{source}`")
        elif output_name == "09_VISUAL_REFERENCE.md":
            parts.append("- Asset manifest for files copied into `ChatGPT/assets/`")
        parts.append("")

    parts.extend(
        [
            "### `ChatGPT/assets/`",
            "",
        ]
    )
    for image_name in image_records:
        parts.append(f"- `{image_name}`")
    parts.extend(
        [
            "",
            "## Source-to-Target Map",
            "",
            "| Source | Target | Kind |",
            "|---|---|---|",
        ]
    )

    for record in sorted(records, key=lambda item: (item.target, item.source)):
        display_target = f"assets/{record.target}" if record.kind == "image" else record.target
        parts.append(f"| `{record.source}` | `{display_target}` | {record.kind} |")

    parts.extend(
        [
            "",
            "## Notes",
            "",
            "- The original root-level files remain the source of truth and are untouched.",
            "- This bundle prefers fewer long documents over many small files to better match ChatGPT Project retrieval behavior.",
            "- Legacy internal references have been redirected to the consolidated files where a direct mapping exists.",
            "",
        ]
    )

    parts.extend(
        [
            "## Original Orientation Sources",
            "",
            "These source files are preserved here so the ChatGPT bundle remains self-contained.",
            "",
        ]
    )
    for source in orientation_sources:
        body = replace_legacy_refs(read_text(source)).rstrip()
        parts.extend(
            [
                "---",
                "",
                f"## Source: `{source}` {{#{slugify(source)}}}",
                "",
                body,
                "",
            ]
        )
    return "\n".join(parts).rstrip() + "\n"


def build() -> None:
    if OUT_DIR.exists():
        shutil.rmtree(OUT_DIR)
    OUT_DIR.mkdir()
    ASSETS_DIR.mkdir()

    records: list[SourceRecord] = []

    for output_name in TEXT_OUTPUTS[1:]:
        if output_name == "07_STRUCTURED_REGISTRIES.md":
            content = render_registry_bundle()
        elif output_name == "08_TIMELINE_AND_FORWARD_STATE.md":
            content = render_timeline_bundle()
        elif output_name == "09_VISUAL_REFERENCE.md":
            content = render_visual_reference()
        else:
            content = render_text_bundle(output_name, TEXT_MAPPING[output_name])
        (OUT_DIR / output_name).write_text(content, encoding="utf-8")
        if output_name in TEXT_MAPPING:
            for source in TEXT_MAPPING[output_name]:
                records.append(SourceRecord(source=source, target=output_name, kind="text"))

    for image_name in IMAGE_FILES:
        shutil.copy2(ROOT / image_name, ASSETS_DIR / image_name)
        records.append(SourceRecord(source=image_name, target=image_name, kind="image"))

    # Legacy repo-orientation docs map into the start file.
    for source in ["00_INDEX.md", "00_README.md", "README.md", "PROJECT_INSTRUCTIONS_FIELD.md"]:
        records.append(SourceRecord(source=source, target="00_START_HERE.md", kind="text"))

    start_here = render_start_here(records)
    (OUT_DIR / "00_START_HERE.md").write_text(start_here, encoding="utf-8")


if __name__ == "__main__":
    build()
