# Nested Containment

**Best for:** hierarchy through containment — scope boundaries, trust zones, folder nesting, blast radius. Outer = broader, inner = more specific.

## Layout conventions
- 3–5 rounded rectangles (`rx=8`), nested with consistent inset padding (24–32px horizontal, 32–36px vertical recommended).
- Each level labeled at the top-left in the `eyebrow` role (7–8px, letter-spacing 0.14em). Labels sit on a paper-colored mask rect over the ring's top border.
- Stroke hierarchy: outer rings faint (`rgba(..,0.30–0.45)`), progressing to muted, to ink, to coral at the innermost focal.
- Fills step up in opacity from outer to inner: `rgba(..,0.015)` → `rgba(..,0.025)` → accent-tint on the innermost.
- Optional file-icon glyph (folded-corner rect) inside each level hints at scope content.
- Italic `callout`-role asides (see `references/primitive-annotation.md`) — 1–2 max.

## On AWS

- The canonical AWS nesting is policy and network scope: Organization → OU → account → Region → VPC → subnet. Use it to show what an SCP, permission boundary, or network ACL covers. Badge each level with its official group icon where one exists (AWS account, Region, VPC, subnet) and label it with its identifier.
- Keep it to the levels the policy actually crosses; an SCP story rarely needs subnets.

## Anti-patterns
- More than 6 levels (information disappears inward).
- Irregular padding between levels — unaligned nesting looks accidental.
- Content inside rings that isn't part of the hierarchy — use a sibling diagram.
- Coral on multiple levels — hierarchy collapses.

## Examples
- `assets/example-nested.html` — minimal light
- `assets/example-nested-dark.html` — minimal dark
- `assets/example-nested-full.html` — full editorial
