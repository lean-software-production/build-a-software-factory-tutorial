#!/usr/bin/env python3
"""Validate the tutorial's static Reveal.js deck without network access."""

from __future__ import annotations

import re
import sys
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlparse

ROOT = Path(__file__).resolve().parents[4]
DECK = ROOT / "docs" / "slides" / "index.html"
ITERATIONS = ROOT / "docs" / "iterations"


class DeckParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.errors: list[str] = []
        self.sections: list[dict[str, object]] = []
        self.references: list[tuple[str, str]] = []
        self.links: list[str] = []
        self._section_depth = 0
        self._current: dict[str, object] | None = None
        self.reveal_div = False
        self.slides_div = False
        self.h1_count = 0

    @staticmethod
    def _classes(attributes: dict[str, str | None]) -> set[str]:
        return set((attributes.get("class") or "").split())

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        attributes = dict(attrs)
        classes = self._classes(attributes)

        if tag == "div":
            self.reveal_div |= "reveal" in classes
            self.slides_div |= "slides" in classes

        if tag == "section":
            if self._section_depth == 0:
                self._current = {"attrs": attributes, "text": []}
                self.sections.append(self._current)
            self._section_depth += 1

        if tag == "h1":
            self.h1_count += 1

        if tag == "img" and "alt" not in attributes:
            self.errors.append(f"image is missing alt text: {attributes.get('src', '<unknown>')}")

        for attribute in ("href", "src"):
            value = attributes.get(attribute)
            if value:
                self.references.append((attribute, value))
                if tag == "a" and attribute == "href":
                    self.links.append(value)

    def handle_endtag(self, tag: str) -> None:
        if tag == "section" and self._section_depth:
            self._section_depth -= 1
            if self._section_depth == 0:
                self._current = None

    def handle_data(self, data: str) -> None:
        if self._current is not None:
            text = self._current["text"]
            assert isinstance(text, list)
            text.append(data)


def iteration_specs() -> dict[str, str]:
    specs: dict[str, str] = {}
    for path in sorted(ITERATIONS.glob("[0-9][0-9][0-9]*-*")):
        match = re.match(r"(\d{3}[a-z]?)-(.+)", path.name)
        if not match or not path.is_dir():
            continue
        readme = path / "README.md"
        heading = ""
        if readme.is_file():
            heading_match = re.search(
                r"^#\s+Homework\s+\d+[a-z]?\s+[—-]\s+(.+?)\s*$",
                readme.read_text(encoding="utf-8"),
                re.MULTILINE,
            )
            if heading_match:
                heading = heading_match.group(1)
        specs[match.group(1)] = heading or match.group(2).replace("-", " ")
    return specs


def normalized(value: str) -> str:
    return " ".join(value.casefold().split())


def local_path(reference: str) -> Path | None:
    parsed = urlparse(reference)
    if parsed.scheme or parsed.netloc or reference.startswith(("#", "data:", "mailto:")):
        return None
    relative = unquote(parsed.path)
    if not relative:
        return None
    candidate = (DECK.parent / relative).resolve()
    try:
        candidate.relative_to(ROOT.resolve())
    except ValueError:
        return Path("/__outside_repository__")
    return candidate


def main() -> int:
    errors: list[str] = []
    if not DECK.is_file():
        print(f"FAIL: missing {DECK.relative_to(ROOT)}", file=sys.stderr)
        return 1

    source = DECK.read_text(encoding="utf-8")
    parser = DeckParser()
    parser.feed(source)
    errors.extend(parser.errors)

    if not parser.reveal_div or not parser.slides_div:
        errors.append("deck must contain .reveal and .slides containers")
    if len(parser.sections) < 12:
        errors.append(f"deck has only {len(parser.sections)} slides; expected a full orientation deck")
    if parser.h1_count != 1:
        errors.append(f"deck must have one h1; found {parser.h1_count}")

    required_snippets = {
        "Reveal.js stylesheet": "reveal.js@5.1.0/dist/reveal.css",
        "Reveal.js script": "reveal.js@5.1.0/dist/reveal.js",
        "Sketchbook stylesheet": "brand/kit/sketchbook.css",
        "Sketchbook script": "brand/kit/sketchbook.js",
        "starter repository": "lean-software-production/capstone-project-starter",
        "fork instruction": "Fork the starter",
        "clone command": "git clone https://github.com/YOUR-NAME/YOUR-CAPSTONE.git",
        "Codespace instruction": "Create codespace",
        "Codex extension sign-in": "Sign in with ChatGPT",
        "Pi sign-in": "OpenAI Codex (legacy)",
        "environment check": "bin/doctor",
        "factory source directory": "factory/",
        "first iteration request": "fetch iteration",
        "coaching request": "coach me",
        "factory launcher": "bin/factory",
        "Tetris seed argument": "--seed tetris/spec.md",
        "first generation target": "--target tetris/tetris-001",
        "complete factory run": "--target tetris/tetris-001 --all",
        "Tetris start command": "tetris/tetris-001 start",
    }
    for label, snippet in required_snippets.items():
        if snippet not in source:
            errors.append(f"missing {label}: {snippet}")

    expected = iteration_specs()
    seen: dict[str, list[dict[str, object]]] = {}
    for section in parser.sections:
        attrs = section["attrs"]
        assert isinstance(attrs, dict)
        number = attrs.get("data-iteration")
        if number:
            seen.setdefault(number, []).append(section)

    for number, name in expected.items():
        matching_sections = seen.get(number, [])
        count = len(matching_sections)
        if count != 1:
            errors.append(f"iteration {number} ({name}) must have one slide; found {count}")
            continue
        text_parts = matching_sections[0]["text"]
        assert isinstance(text_parts, list)
        if normalized(name) not in normalized(" ".join(text_parts)):
            errors.append(f"iteration {number} slide is missing its source title: {name}")
    for number in sorted(set(seen) - set(expected)):
        errors.append(f"deck describes unknown iteration {number}")

    for attribute, reference in parser.references:
        path = local_path(reference)
        if path is not None and not path.exists():
            errors.append(f"broken local {attribute}: {reference}")

    if not (ROOT / "docs" / "slides" / "tutorial.css").is_file():
        errors.append("missing docs/slides/tutorial.css")
    if not (ROOT / "docs" / "index.html").is_file():
        errors.append("missing docs/index.html Pages entry point")
    if not (ROOT / "docs" / ".nojekyll").is_file():
        errors.append("missing docs/.nojekyll")

    if errors:
        for error in errors:
            print(f"FAIL: {error}", file=sys.stderr)
        return 1

    print(
        f"PASS: {len(parser.sections)} slides cover {len(expected)} iterations; "
        "Reveal, brand, setup and local links are present."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
