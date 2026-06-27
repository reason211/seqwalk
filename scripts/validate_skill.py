#!/usr/bin/env python3
"""Validate the SeqWalk skill bundle without third-party dependencies."""

from __future__ import annotations

import re
import sys
from pathlib import Path


NAME_RE = re.compile(r"^[a-z0-9][a-z0-9-]{0,63}$")


def fail(message: str) -> None:
    print(f"[FAIL] {message}")
    raise SystemExit(1)


def parse_frontmatter(text: str) -> dict[str, str]:
    if not text.startswith("---\n"):
        fail("SKILL.md must start with YAML frontmatter")
    end = text.find("\n---\n", 4)
    if end == -1:
        fail("SKILL.md frontmatter must close with ---")
    raw = text[4:end].splitlines()
    data: dict[str, str] = {}
    for line in raw:
        if not line.strip():
            continue
        if ":" not in line:
            fail(f"Invalid frontmatter line: {line}")
        key, value = line.split(":", 1)
        data[key.strip()] = value.strip().strip('"').strip("'")
    return data


def main() -> int:
    skill_dir = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("skill/seqwalk")
    if not skill_dir.exists():
        fail(f"Skill directory not found: {skill_dir}")
    skill_md = skill_dir / "SKILL.md"
    if not skill_md.exists():
        fail("Missing SKILL.md")

    text = skill_md.read_text(encoding="utf-8")
    frontmatter = parse_frontmatter(text)
    name = frontmatter.get("name", "")
    description = frontmatter.get("description", "")

    if not NAME_RE.match(name):
        fail(f"Invalid skill name: {name!r}")
    if skill_dir.name != name:
        fail(f"Skill folder name {skill_dir.name!r} must match frontmatter name {name!r}")
    if len(description.split()) < 8:
        fail("Description is too short to be a useful trigger")
    todo = "TO" + "DO"
    bracketed_todo = "[TO" + "DO"
    if todo in text or bracketed_todo in text:
        fail("SKILL.md contains unfinished placeholder markers")

    asset = skill_dir / "assets" / "strict-sequence-viewer-template.html"
    if not asset.exists():
        fail("Missing strict sequence viewer template asset")
    asset_text = asset.read_text(encoding="utf-8")
    for token in ("data-from", "data-to", "lifeline", "participant-rail"):
        if token not in asset_text:
            fail(f"Template asset is missing expected token: {token}")

    openai_yaml = skill_dir / "agents" / "openai.yaml"
    if not openai_yaml.exists():
        fail("Missing agents/openai.yaml")
    yaml_text = openai_yaml.read_text(encoding="utf-8")
    for token in ("display_name", "short_description", "default_prompt"):
        if token not in yaml_text:
            fail(f"openai.yaml missing {token}")

    print("[OK] SeqWalk skill bundle is valid")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
