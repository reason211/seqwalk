#!/usr/bin/env python3
"""Validate the interactive SeqWalk example HTML."""

from __future__ import annotations

import sys
from pathlib import Path


def fail(message: str) -> None:
    print(f"[FAIL] {message}")
    raise SystemExit(1)


def main() -> int:
    html_path = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("examples/ecommerce-order-flow.html")
    if not html_path.exists():
        fail(f"Example HTML not found: {html_path}")

    text = html_path.read_text(encoding="utf-8")
    for token in (
        'id="sectionNav"',
        'id="storeToggle"',
        'id="clearLockButton"',
        "dataset.targetSection",
        'data-card-id="C1"',
        "function updateSectionNav()",
        "function updateActiveFromViewport()",
    ):
        if token not in text:
            fail(f"Example HTML is missing expected token: {token}")

    if "function isNearPageBottom(" not in text:
        fail("Example HTML must guard bottom-of-page section and step highlighting")
    if "sections[sections.length - 1]" not in text:
        fail("Section navigation must prefer the last section at page bottom")
    if "visible[visible.length - 1]" not in text:
        fail("Scroll highlighting must prefer the last visible step at page bottom")
    if 'step.closest(".sequence-section") === activeSection' not in text:
        fail("Scroll highlighting must prefer steps from the active section")

    print("[OK] SeqWalk example HTML is valid")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
