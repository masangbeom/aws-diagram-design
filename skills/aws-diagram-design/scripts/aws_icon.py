#!/usr/bin/env python3
"""Find and inline official AWS Architecture Icons, with no third-party deps.

Ships inside the skill so an agent drawing an AWS diagram never hand-copies SVG:

    python3 <skill-dir>/scripts/aws_icon.py find lambda
    python3 <skill-dir>/scripts/aws_icon.py service/Compute/Arch_AWS-Lambda_48.svg 112 64 24
    python3 <skill-dir>/scripts/aws_icon.py service/Compute/Arch_AWS-Lambda_48.svg 112 64 24 --bake

The inline form follows references/primitive-aws-icons.md § Inlining an icon: the
icon's inner markup without its XML declaration, outer <svg>, <title>, or ids,
wrapped in `<g transform="translate(x,y) scale(s)" aria-hidden="true">` so it
renders at `px` pixels with its top-left corner at (x, y).

`--bake` writes the same geometry into absolute coordinates with no transform
attribute, for grammars whose verifier rejects transforms on the canvas
(architecture delta). Icons that carry their own internal transforms cannot be
baked and are refused; pick another icon or use the plain form.
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

ICONS = Path(__file__).resolve().parent.parent / "assets" / "aws-icons"
NUM = r"[-+]?(?:\d+\.?\d*|\.\d+)(?:[eE][-+]?\d+)?"


def fmt(value: float) -> str:
    return ("%.3f" % value).rstrip("0").rstrip(".") or "0"


def inner_markup(path: Path) -> tuple[str, float]:
    """Return the icon body (ids, title, wrapper stripped) and its viewBox width."""
    src = path.read_text(encoding="utf-8")
    box = re.search(r'viewBox="([\d.\s-]+)"', src)
    width = float(box.group(1).split()[2]) if box else 64.0
    body = re.sub(r"<\?xml[^>]*>|<!--.*?-->", "", src, flags=re.S)
    body = re.sub(r"^.*?<svg\b[^>]*>", "", body, count=1, flags=re.S)
    body = re.sub(r"</svg>\s*$", "", body.strip())
    body = re.sub(r"<title>.*?</title>|<desc>.*?</desc>", "", body, flags=re.S)
    body = re.sub(r'\s(?:id|xmlns(?::\w+)?)="[^"]*"', "", body)
    return re.sub(r"\s+", " ", body).strip(), width


def bake_path(d: str, tx: float, ty: float, s: float) -> str:
    out = []
    for cmd, args in re.findall(r"([MmLlHhVvCcSsQqTtAaZz])([^MmLlHhVvCcSsQqTtAaZz]*)", d):
        nums = [float(n) for n in re.findall(NUM, args)]
        rel, upper = cmd.islower(), cmd.upper()
        if upper == "Z":
            out.append(cmd)
            continue
        res: list[float] = []
        if upper == "H":
            res = [n * s + (0 if rel else tx) for n in nums]
        elif upper == "V":
            res = [n * s + (0 if rel else ty) for n in nums]
        elif upper == "A":
            for i in range(0, len(nums), 7):
                rx, ry, rot, large, sweep, x, y = nums[i:i + 7]
                res += [rx * s, ry * s, rot, large, sweep,
                        x * s + (0 if rel else tx), y * s + (0 if rel else ty)]
        else:
            res = [n * s + (0 if rel else (tx if i % 2 == 0 else ty)) for i, n in enumerate(nums)]
        out.append(cmd + " ".join(fmt(v) for v in res))
    return " ".join(out)


def bake(body: str, x: float, y: float, s: float) -> str:
    if "transform=" in body or re.search(r"<(?!/?(?:g|rect|path)\b)[a-zA-Z]", body):
        raise ValueError("icon uses internal transforms or shapes other than g/rect/path; it cannot be baked")

    def rect(match: re.Match[str]) -> str:
        tag = match.group(0)

        def get(key: str) -> float:
            found = re.search(r'\b%s="(%s)"' % (key, NUM), tag)
            return float(found.group(1)) if found else 0.0

        rx, ry, w, h = get("x"), get("y"), get("width"), get("height")
        tag = re.sub(r'\s(?:x|y|width|height)="[^"]*"', "", tag)
        return tag.replace("<rect", '<rect x="%s" y="%s" width="%s" height="%s"'
                           % (fmt(rx * s + x), fmt(ry * s + y), fmt(w * s), fmt(h * s)), 1)

    body = re.sub(r"<rect\b[^>]*>", rect, body)
    body = re.sub(r'\sd="([^"]*)"', lambda m: ' d="%s"' % bake_path(m.group(1), x, y, s), body)
    return '<g aria-hidden="true">' + body + "</g>"


def find(term: str) -> list[str]:
    words = term.lower().split()
    return sorted(
        str(p.relative_to(ICONS)) for p in ICONS.rglob("*.svg")
        if all(w in p.name.lower().replace("-", " ") or w in p.name.lower() for w in words)
    )


def main(argv: list[str] | None = None) -> int:
    argv = sys.argv[1:] if argv is None else argv
    if argv[:1] == ["find"]:
        if len(argv) < 2:
            print("usage: aws_icon.py find <term…>", file=sys.stderr)
            return 2
        hits = find(" ".join(argv[1:]))
        print("\n".join(hits) if hits else "no icon matches; see assets/aws-icons/INDEX.md")
        return 0 if hits else 1
    parser = argparse.ArgumentParser(description="Inline an official AWS icon at (x, y), px pixels square.")
    parser.add_argument("icon", help="path under assets/aws-icons/, e.g. service/Compute/Arch_AWS-Lambda_48.svg")
    parser.add_argument("x", type=float)
    parser.add_argument("y", type=float)
    parser.add_argument("px", type=float, help="rendered size; 16 minimum, 24-32 inside nodes")
    parser.add_argument("--bake", action="store_true", help="absolute coordinates, no transform attribute")
    args = parser.parse_args(argv)
    path = ICONS / args.icon
    if not path.is_file():
        print(f"error: no icon at assets/aws-icons/{args.icon}; try `aws_icon.py find <name>`", file=sys.stderr)
        return 2
    if args.px < 16:
        print("error: AWS icons render at 16px minimum (primitive-aws-icons.md rule 2)", file=sys.stderr)
        return 2
    body, width = inner_markup(path)
    scale = round(args.px / width, 4)
    try:
        print(bake(body, args.x, args.y, scale) if args.bake else
              f'<g transform="translate({fmt(args.x)},{fmt(args.y)}) scale({fmt(scale)})" aria-hidden="true">{body}</g>')
    except ValueError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main())
