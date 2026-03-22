#!/usr/bin/env python3
"""Генерация S2R-view для PACK-MIM.

Сканирует frontmatter s2r_families → строит матрицу 3×3 со ссылками.

Использование: python3 scripts/generate-s2r-view.py
Результат: pack/mim/07-map/s2r-view.md
"""

import re
import sys
from datetime import datetime
from pathlib import Path

SCRIPT_DIR = Path(__file__).parent
PACK_DIR = SCRIPT_DIR.parent / "pack" / "mim"
OUTPUT = PACK_DIR / "07-map" / "s2r-view.md"

FAMILY_NAMES = {
    "F0": "Метауровень",
    "F1": "Продвижение",
    "F2": "Продукт",
    "F3": "PR/GR",
    "F4": "Видение",
    "F5": "Архитектура",
    "F6": "Операции",
    "F7": "Бизнес",
    "F8": "Платформа",
    "F9": "Команда",
}

MATRIX_ROWS = [
    ("Надсистема", ["F1", "F2", "F3"]),
    ("Целевая система", ["F4", "F5", "F6"]),
    ("Система создания", ["F7", "F8", "F9"]),
]

SKIP_FILES = {"07-map/s2r-view.md", "00-pack-manifest.md"}


def parse_frontmatter(filepath: Path) -> dict:
    """Извлекает frontmatter из .md файла."""
    result = {"s2r_families": [], "title": "", "id": ""}
    try:
        text = filepath.read_text(encoding="utf-8")
    except Exception:
        return result

    match = re.match(r"^---\n(.*?)\n---", text, re.DOTALL)
    if not match:
        return result

    fm = match.group(1)

    fam_match = re.search(r"s2r_families:\s*\[([^\]]+)\]", fm)
    if fam_match:
        families = [f.strip().strip("'\"") for f in fam_match.group(1).split(",")]
        result["s2r_families"] = families

    title_match = re.search(r"^title:\s*(.+)$", fm, re.MULTILINE)
    if title_match:
        result["title"] = title_match.group(1).strip().strip("'\"")

    id_match = re.search(r"^id:\s*(.+)$", fm, re.MULTILINE)
    if id_match:
        result["id"] = id_match.group(1).strip()

    if not result["title"]:
        h1_match = re.search(r"^#\s+(.+)$", text, re.MULTILINE)
        if h1_match:
            result["title"] = h1_match.group(1).strip()

    return result


def main():
    if not PACK_DIR.exists():
        print(f"Pack directory not found: {PACK_DIR}", file=sys.stderr)
        sys.exit(1)

    docs = []
    all_md_files = []

    for md_file in sorted(PACK_DIR.rglob("*.md")):
        rel = str(md_file.relative_to(PACK_DIR))
        all_md_files.append(rel)

        if rel in SKIP_FILES:
            continue

        fm = parse_frontmatter(md_file)
        if fm["s2r_families"]:
            docs.append((rel, fm["s2r_families"], fm["title"], fm["id"]))

    lines = []
    lines.append("---")
    lines.append("id: MIM.MAP.003")
    lines.append("name: S2R Domain View")
    lines.append("scope: full-pack")
    lines.append("generated: true")
    lines.append("---")
    lines.append("")
    lines.append("# S2R Domain View — МИМ (Мастерская интеллектуального мастерства)")
    lines.append("")
    lines.append("> Матрица 3×3: навигация по доменным знаниям Pack.")
    lines.append("> Auto-generated. Do not edit manually.")
    lines.append("> Regenerate: `python3 scripts/generate-s2r-view.py`")
    lines.append("")
    lines.append("## Матрица знаний")
    lines.append("")
    lines.append("|  | **Предприниматель** (Зачем?) | **Инженер** (Как устроено?) | **Менеджер** (Как работает?) |")
    lines.append("|---|---|---|---|")

    for row_name, families in MATRIX_ROWS:
        cells = []
        for fam in families:
            fam_name = FAMILY_NAMES[fam]
            entries = []
            for rel, fams, title, doc_id in docs:
                if fam in fams:
                    display = doc_id if doc_id else title
                    entries.append(f"[{display}]({rel})")

            if entries:
                items = " ".join(f"• {e}" for e in entries)
                cells.append(f"**{fam}: {fam_name}** {items}")
            else:
                cells.append(f"**{fam}: {fam_name}** — *(пусто)*")

        lines.append(f"| **{row_name}** | {cells[0]} | {cells[1]} | {cells[2]} |")

    # F0
    lines.append("")
    lines.append("## Метауровень (F0)")
    lines.append("")
    f0_docs = [(rel, doc_id, title) for rel, fams, title, doc_id in docs if "F0" in fams]
    if f0_docs:
        for rel, doc_id, title in f0_docs:
            display = doc_id if doc_id else title
            lines.append(f"- [{display}]({rel})")
    else:
        lines.append("*(пусто)*")

    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append(f"**Документов с S2R-тегами:** {len(docs)}")

    tagged_rels = {d[0] for d in docs}
    untagged = [
        rel for rel in all_md_files
        if rel not in tagged_rels and rel not in SKIP_FILES
    ]

    lines.append("")
    lines.append("## Без S2R-тегов")
    lines.append("")
    if untagged:
        for rel in untagged:
            lines.append(f"- `{rel}` — нет тега `s2r_families`")
    else:
        lines.append("*(все документы размечены)*")

    lines.append("")
    lines.append("---")
    lines.append(f"*Generated on {datetime.now().strftime('%Y-%m-%d %H:%M')}*")
    lines.append("")

    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text("\n".join(lines), encoding="utf-8")

    print(f"S2R view generated: {OUTPUT}")
    print(f"Documents tagged: {len(docs)}")
    if untagged:
        print(f"Untagged: {len(untagged)}")


if __name__ == "__main__":
    main()
