"""
Content structuring: converts raw text into a list of slide dicts.
Each slide dict:  {"title": str, "bullets": [str], "layout": str}
"""

import re
from typing import TypedDict


class Slide(TypedDict):
    title: str
    bullets: list[str]
    layout: str   # "title", "section", "content", "bullets"


# ── helpers ──────────────────────────────────────────────────────────────────

def _split_paragraphs(text: str) -> list[str]:
    """Split text on blank lines; keep non-empty blocks."""
    blocks = re.split(r"\n\s*\n", text)
    return [b.strip() for b in blocks if b.strip()]


def _looks_like_heading(line: str) -> bool:
    """Heuristic: short line (≤ 12 words), no trailing period → heading."""
    words = line.split()
    return 1 <= len(words) <= 12 and not line.endswith(".")


def _is_slide_marker(line: str) -> tuple[bool, str]:
    """Detect explicit slide markers like [Slide 3] or [Page 2]."""
    m = re.fullmatch(r"\[(Slide|Page)\s+\d+\]", line, re.IGNORECASE)
    return bool(m), line if m else ""


def _clean_bullet(line: str) -> str:
    return re.sub(r"^[\-\*\•\–\—]\s*", "", line).strip()


# ── main structuring logic ────────────────────────────────────────────────────

def structure_content(raw_text: str, max_bullets: int = 6) -> list[Slide]:
    """
    Parse *raw_text* into a list of Slide objects.

    Strategy
    --------
    1. If the text contains explicit [Slide N] / [Page N] markers (produced by
       the extractor), use those as section boundaries.
    2. Otherwise fall back to blank-line / heading detection.
    Always inserts a *title* slide as the first element.
    """
    slides: list[Slide] = []

    # --- pass 1: split on explicit markers ---
    marker_pattern = re.compile(r"^\[(Slide|Page)\s+\d+\]$", re.IGNORECASE | re.MULTILINE)
    sections = marker_pattern.split(raw_text)
    # sections alternates: [preamble, "Slide", text, "Slide", text …]
    # after re.split with groups the list is: [before, g1, seg1, g1, seg2 …]
    # We want pairs (marker, segment); easiest: walk the full split list
    raw_sections: list[str] = re.split(r"\[(Slide|Page)\s+\d+\]", raw_text, flags=re.IGNORECASE)
    has_markers = len(raw_sections) > 1

    if has_markers:
        # raw_sections[0] is preamble, rest are slide bodies
        segments = [s.strip() for s in raw_sections if s.strip() and not re.fullmatch(r"Slide|Page", s, re.I)]
    else:
        # Fall back: split on blank lines
        segments = _split_paragraphs(raw_text)

    # --- build title slide from first segment ---
    if segments:
        first = segments[0]
        first_lines = [l.strip() for l in first.splitlines() if l.strip()]
        title_text = first_lines[0] if first_lines else "Presentation"
        subtitle_bullets = first_lines[1:3]
        slides.append(Slide(title=title_text, bullets=subtitle_bullets, layout="title"))
        segments = segments[1:]

    # --- build content slides ---
    pending_title = ""
    pending_bullets: list[str] = []

    def _flush():
        if pending_title or pending_bullets:
            layout = "bullets" if pending_bullets else "section"
            slides.append(Slide(
                title=pending_title or "Key Points",
                bullets=pending_bullets[:max_bullets],
                layout=layout,
            ))

    for seg in segments:
        lines = [l.strip() for l in seg.splitlines() if l.strip()]
        if not lines:
            continue

        # Check first line as heading
        if _looks_like_heading(lines[0]):
            _flush()
            pending_title = lines[0]
            pending_bullets = []
            body_lines = lines[1:]
        else:
            body_lines = lines

        # Collect bullets from body
        for line in body_lines:
            cleaned = _clean_bullet(line)
            if not cleaned:
                continue
            # If the block has no heading and line looks like heading, start new slide
            if not pending_title and _looks_like_heading(line):
                _flush()
                pending_title = cleaned
                pending_bullets = []
            else:
                pending_bullets.append(cleaned)
                if len(pending_bullets) >= max_bullets:
                    _flush()
                    pending_title = pending_title + " (cont.)" if pending_title else "Continued"
                    pending_bullets = []

    _flush()

    # --- ensure minimum 3 slides (title + at least 2 content) ---
    if len(slides) == 1:
        # Split long bullets across two slides
        all_bullets = slides[0]["bullets"]
        slides.append(Slide(title="Overview", bullets=all_bullets, layout="bullets"))
        slides[0]["bullets"] = []

    # --- add a closing "Thank You" slide ---
    slides.append(Slide(title="Thank You", bullets=["Questions & Discussion"], layout="section"))

    return slides
