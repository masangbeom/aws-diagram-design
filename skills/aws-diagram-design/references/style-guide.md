# Style Guide

**The single source of truth for colors, typography, and tokens.** Every diagram draws from this — not from hex values inlined in other reference files. If you want to change the visual skin of Diagram Design, change this file.

**Current skin: AWS brand** — white paper, Squid-Ink text (`#232F3E`), Smile-Orange accent, Amazon Ember typography, and the official AWS Architecture Icons ([primitive-aws-icons.md](primitive-aws-icons.md)). This replaces the shipped editorial default (white-smoke / atomic-tangerine `#eb6c36`); swap these values (or run [`onboarding.md`](onboarding.md)) and every new diagram inherits the new skin without touching any type-specific logic.

---

## Tokens

### Semantic roles

Every token is referred to by **semantic role**, not by its hex value. Type references (`type-*.md`) and SKILL.md say `accent`, not `#EC7211`.

| Role | Purpose | AWS (light) | AWS (dark) |
|---|---|---|---|
| `paper` | Page background, default node fill | `#FFFFFF` (white — official AWS diagram bg) | `#161E2D` (dark squid) |
| `paper-2` | Diagram container bg, secondary fill | `#F2F3F3` | `#232F3E` (squid ink) |
| `ink` | Primary text, primary stroke | `#232F3E` (squid ink) | `#FFFFFF` |
| `muted` | Secondary text, default arrow stroke | `#545B64` | `#B6BEC9` |
| `soft` | Sublabels, boundary labels | `#687078` | `#8D99A8` |
| `rule` | Hairline borders | `rgba(35,47,62,0.12)` | `rgba(255,255,255,0.12)` |
| `rule-solid` | Stronger borders, baselines | `#D5DBDB` | `rgba(255,255,255,0.25)` |
| `accent` | Focal / 1–2 max per diagram | `#EC7211` (smile orange, dark step) | `#FF9900` (smile orange) |
| `accent-tint` | Fill for accent-bordered boxes | `rgba(255,153,0,0.10)` | `rgba(255,153,0,0.14)` |
| `link` | HTTP/API calls, external arrows | `#0972D3` (Cloudscape blue) | `#539FE5` |

> **Brand palette source:** AWS brand — `squid ink #232F3E`, `smile orange #FF9900`, white. Pure `#FF9900` reads weakly as thin strokes/text on white, so light-mode `accent` uses the darker step `#EC7211` (the orange AWS itself uses on light UI); `#FF9900` is the accent on dark and the base of `accent-tint`. `muted`/`soft`/`rule-solid`/`link` come from the AWS/Cloudscape grey-blue ramp. Category identity colors (`#ED7100`, `#8C4FFF`, …) belong to the icons and zone borders — see [primitive-aws-icons.md](primitive-aws-icons.md) — and are **not** editorial accents.

> **Note:** The example HTML files in `assets/` are drawn in this AWS skin (light, dark, and full-editorial variants) with AWS scenarios. They are the reference renders for each type; new diagrams use the tokens above.

### Contrast contract

Every token must clear the threshold for each role it plays, against the background it actually sits on, in both skins.

| Use | Minimum vs. its actual background |
|---|---|
| Regular text, including any `soft`, `link`, or `accent` used as text | 4.5:1 |
| Large text (24px+, or 18.7px+ at weight 600+) | 3:1 |
| Essential non-text marks: lines, arrows, borders, focus outlines, data points | 3:1 against the adjacent color |
| Decorative rules and translucent tints (`rule`, `rule-solid`, `paper-2`, `accent-tint`, fills at opacity) | No minimum, but never the only carrier of meaning |

- **A token used in several roles must pass each one.** `accent` is a stroke in one place and a label in another, so as text it is held to 4.5:1, not the 3:1 its strokes alone would need.
- **Translucent colors are composited first.** An `rgba()` fill or stroke is blended over `paper` before its ratio is measured. A value that clears the bar at full strength can fail at 0.5 opacity.
- **Surfaces other than `paper` cost contrast.** Inside an `accent-tint` box or on `paper-2` every ratio drops. Measure text placed there against that surface, not against `paper`.
- **Current AWS values** (WCAG 2.x, on `paper`): light `ink` 13.57:1, `muted` 6.87:1, `soft` 5.03:1, `link` 4.82:1, `accent` 3.01:1 on `#FFFFFF`; dark `muted` 8.90:1, `soft` 5.77:1, `link` 5.93:1, `accent` 7.80:1 on `#161E2D`. `soft` was darkened from `#7D8998` (3.56:1) to `#687078` so sublabels and boundary labels clear the text bar.
- **Light `accent` is a mark color, not a text color.** Smile orange `#EC7211` is kept for brand fidelity and clears the 3:1 bar for strokes, borders, markers, and fills, but not the 4.5:1 text bar. In the light skin, text below the large-text threshold never takes `accent`: wherever a type reference asks for an accent-colored label (a focal arrow label, a focal value label, a tag on an accent box), set it in `ink` — or `muted` for a tag or boundary label that would otherwise be accent at an opacity — and let the accent stroke, marker, or fill beside it carry the focal signal. Large titles and numerals (24px+, or 18.7px+ at weight 600+) may use `accent`. The dark skin's `#FF9900` reads 7.80:1, so accent text is fine there.

### Inversion rule (light → dark)

Any `rgba(35,47,62, X)` in light becomes `rgba(255,255,255, X)` in dark. Same opacities, RGB flipped. The accent brightens from `#EC7211` to pure `#FF9900` on dark paper.

### Series palette (multi-series chart types only)

For chart types that genuinely need to distinguish multiple overlapping entities (currently: **radar**), use the AWS category ramp. The "1-focal" rule still holds — `accent` is reserved for the focal series; the palette below covers the rest.

| Token | Light | Dark | Notes |
|---|---|---|---|
| `series-1` | `#8C4FFF` (purple) | `#A97FFF` | Non-focal series |
| `series-2` | `#01A88D` (teal) | `#2BC0A8` | Non-focal series |
| `series-3` | `#7AA116` (green) | `#96BE3C` | Non-focal series |
| `series-4` | `#C925D1` (magenta) | `#D95CDF` | Non-focal series |
| `series-5` | `#DD344C` (red) | `#E5626F` | Non-focal series |

Fills sit at `0.14` opacity light, `0.20` dark; strokes use the full color. **Don't backfill these tokens to non-chart types** — architecture, swimlane, etc. continue to use muted-ink variants. The series palette is opt-in for diagrams where overlapping shapes demand distinguishable color, not a license to add color elsewhere.

### Terminal skin (opt-in alternate)

A self-contained palette for the terminal-window primitive (see [primitive-terminal.md](primitive-terminal.md)) — a CLI-chrome register for dev-tool posts and technical social cards. It does not replace the default skin above and isn't affected by onboarding; it's a second, fixed skin you opt into per-diagram.

| Token | Hex | Purpose |
|---|---|---|
| `terminal-page` | `#0a0a0a` | Page background behind the window |
| `terminal-paper` | `#141414` | Window body, node fill |
| `terminal-bar` | `#1b1b1b` | Titlebar strip |
| `terminal-border` | `#2b2b2b` | Window border, hairlines |
| `terminal-ink` | `#f5f5f5` | Primary text, primary stroke |
| `terminal-muted` | `#9a9a9a` | Secondary text, sublabels, ring stroke |
| `terminal-soft` | `#5c5c5c` | Tertiary — inactive dots, spokes |
| `terminal-accent` | `#ff5a36` | The one accent — focal station, prompt sign, active dot |
| `terminal-accent-tint` | `rgba(255,90,54,0.12)` | Fill for accent-bordered boxes |

**1-accent rule still holds.** Everything that isn't `terminal-ink` or `terminal-muted`/`terminal-soft` should be `terminal-accent` — never introduce a second hue.

---

## Typography

| Role | Family | Size | Weight | Usage |
|---|---|---|---|---|
| `title` | Amazon Ember | 1.75rem | 700 | Page H1 |
| `node-name` | Amazon Ember | 12px | 600 | Human-readable labels |
| `sublabel` | Amazon Ember Mono | 9px | 400 | Port, protocol, URL, field type |
| `eyebrow` | Amazon Ember Mono | 7–8px | 500, tracked 0.18em, uppercase | Type tags, axis labels |
| `arrow-label` | Amazon Ember Mono | 8px | 400, tracked 0.06em | Arrow annotations |
| `callout` | Amazon Ember *italic* | 14px | 400 | Editorial asides only |

### Font stack

Amazon Ember is **not on Google Fonts**, but this skill **bundles it** at [`assets/fonts/`](../assets/fonts/) (woff2 webfonts + desktop TTFs, from Amazon's public typography download). Load it in this order:

1. **`local('Amazon Ember')`** — present on Amazon-managed machines, or after running `./install.sh fonts` (repo root), which installs the bundled TTFs into the OS font directory.
2. **Bundled woff2 via `@font-face`** — paste the canonical block from [`assets/fonts/README.md`](../assets/fonts/README.md) into the generated HTML, pointing `FONTS` at `<skill-dir>/assets/fonts/woff2` (relative path when the output lives near the skill; or copy the woff2 files next to the deliverable and use `./fonts/`).
3. **Fallback stack** — always declared on `font-family`; sandboxed viewers (GitHub's SVG renderer, offline tools) fall back to Helvetica/Arial.

Weight map for the bundled faces: Amazon Ember 300 Lt · 400 Rg (+italic) · 600 SBd · 700 Bd · 800 He; **Amazon Ember Mono 400/700** carries every mono role (sublabels, eyebrows, arrow labels — a 500/600 spec snaps to the nearest bundled weight, which is expected). **No font loads from an external CDN** — generated diagrams need no Google Fonts `<link>`.

```css
/* sans (names, titles, callouts) */ font-family: 'Amazon Ember', 'Helvetica Neue', Helvetica, Arial, sans-serif;
/* mono (technical content)       */ font-family: 'Amazon Ember Mono', ui-monospace, monospace;
```

Installed Ember faces: Light 300 / Regular 400 / Medium 500 / Bold 700 / Heavy 800, plus italics. If a 600 weight renders as synthesized bold in a target environment, drop node names to 500 or up to 700 — never fake-bold the Heavy face.

**Load-bearing rule:** Mono is for *technical* content (ports, commands, URLs, field types). Names, titles, and callouts go in Amazon Ember. Italic Ember is reserved for annotation callouts (see [primitive-annotation.md](primitive-annotation.md)). **Never JetBrains Mono** as a blanket "dev" font. This skin intentionally drops the editorial serif (Instrument Serif) — AWS brand typography is single-family.

### Korean labels

Amazon Ember and Amazon Ember Mono carry no Hangul. A Korean `<text>` element extends its own family — never swap the skin:

```svg
<text font-family="'Amazon Ember', 'Apple SD Gothic Neo', 'Malgun Gothic', 'Noto Sans KR', sans-serif">결제 서비스</text>
```

Hangul resolves through the viewer's installed Korean face (Apple SD Gothic Neo on macOS, Malgun Gothic on Windows, Noto Sans KR on Linux); the AWS skin loads nothing from a CDN, so there is no web Korean face to prefer. Titles use the same stack at the title weight.

**Width budget.** Measure per character, not per script: **every Unicode wide or full-width character costs 1em, every other character costs its face's Latin advance** (0.60em sans, 0.62em mono), and nonspacing/enclosing marks cost nothing. Sum over the string and multiply by the font size for the text width, then add padding and round the box up to the next multiple of 4.

Counting by script is the trap. `주문 v2.1` is two full-width syllables and five narrow characters; a formula that tallies Hangul, Latin letters, and spaces silently drops `2`, `.`, and `1` and sizes the box for four of its seven characters. Every rendered character costs something — measure per character, never per script.

Three rules follow from Hangul metrics:

- **Sublabels stay Latin.** Ports, protocols, field types, ARNs, and URLs are Latin anyway — keep Amazon Ember Mono there and don't translate them. Hangul in a 9px mono sublabel is unreadable and has no mono face to fall back to.
- **Floor of 12px.** Hangul goes muddy below 12px. If a Korean name doesn't fit at 12px, cut the name — don't shrink the type.
- **Arrow labels, eyebrows, and legend text switch register.** Those slots are 7–8px Amazon Ember Mono, uppercase and tracked, which Hangul has neither a face nor legibility for. A Korean label in one of those slots becomes 12px sans at weight 500 with no tracking and no uppercase transform, and its mask rect grows to match (16px tall, width from the budget above, still rounded to a multiple of 4). Latin labels in the same diagram keep the mono treatment.

### Chinese and Japanese labels

The same three rules apply to Han and kana, with their own stacks — Japanese fonts cover only part of the Chinese set and draw Japanese glyph variants, and Simplified and Traditional are separate stacks for the same reason:

```svg
<text font-family="'Amazon Ember', 'Hiragino Sans', 'Noto Sans JP', 'Yu Gothic', sans-serif">認証サービス</text>
<text font-family="'Amazon Ember', 'PingFang SC', 'Noto Sans SC', 'Microsoft YaHei', sans-serif">认证服务</text>
<text font-family="'Amazon Ember', 'PingFang TC', 'Noto Sans TC', 'Microsoft JhengHei', sans-serif">認證服務</text>
```

Full-width punctuation — `（）「」，。：` — is wide and costs 1em as well.

### Cyrillic labels

Amazon Ember and Amazon Ember Mono both ship Cyrillic, so names, sublabels, arrow labels, eyebrows, and legend text in Bulgarian, Russian, Ukrainian, or Serbian keep the Latin treatment: same faces, sizes, tracking, and uppercase — no register switch and no stack extension. Width follows the same per-character budget. A label the reader matches against a physical thing (a cabinet, a port map) carries the exact printed string: don't transliterate or re-case it.


---

## Stroke, radius, spacing

| Token | Value | Use |
|---|---|---|
| `stroke-thin` | `0.8` | Tag-box outlines, leaf nodes |
| `stroke-default` | `1` | Most strokes |
| `stroke-strong` | `1.2` | Emphasis strokes |
| `radius-sm` | `4` | Small tags |
| `radius-md` | `6` | Node boxes |
| `radius-lg` | `8` | Containers, rings |
| `grid` | `4` | Every coord, size, and gap is divisible by 4 (hard rule) |

---

## Node type → treatment

Semantic role combinations — reference these by name in type specs.

| Type | Fill | Stroke |
|---|---|---|
| `focal` (1–2 max) | `accent-tint` | `accent` |
| `backend` | `#ffffff` (white) | `ink` |
| `store` | `ink @ 0.05` | `muted` |
| `external` | `ink @ 0.03` | `ink @ 0.30` |
| `input` | `muted @ 0.10` | `soft` |
| `optional` | `ink @ 0.02` | `ink @ 0.20` dashed `4,3` |
| `security` | `#DD344C @ 0.05` | `#DD344C @ 0.60` dashed `4,4` — aligned to the AWS Security-Identity red |

AWS-specific node and zone treatments (service-icon nodes, VPC/subnet/account containers) are specified in [primitive-aws-icons.md](primitive-aws-icons.md); zone-border identity colors don't count against the accent budget.

---

## Customizing the skin

Three options:

1. **Run onboarding** — see [`onboarding.md`](onboarding.md). Drop a URL; the skill extracts the palette + fonts and rewrites this file.
2. **Edit by hand** — change the hex values in the tables above. Run the pre-output taste gate afterward to verify the accent still reads as "focal" against the new paper color.
3. **Brand handoff** — paste your existing design-token JSON into a new section here and map its tokens to the semantic roles above.

### Constraints (don't break these)

- **Contrast**: every text token (`ink`, `muted`, `soft`, `link`, and `accent`) must clear 4.5:1 on `paper`, in both skins. See the [contrast contract](#contrast-contract).
- **One accent**: pick one color for `accent`. Two accents erases the focal signal. (AWS icon/zone identity colors are exempt — they're identity marks, not accents.)
- **No rainbow palette**: if your brand ships 8 colors, pick 3 (paper, ink, accent). The rest become `muted` variants.
- **Typography**: at most three families. The AWS skin runs sans + mono (Ember + Amazon Ember Mono) — brand consistency outweighs the serif/sans contrast the editorial default used.
- **Paper**: the AWS skin uses pure white because official AWS architecture diagrams do. For non-AWS skins, prefer a warm-neutral (cream, bone, light grey) — pure white without a brand mandate turns the design sterile.
- **Dot pattern is optional, not default**: the 22×22 dot pattern is an opt-in "dotted paper" variant (good for long-form editorial hero diagrams). The default background is a clean `paper` fill, no pattern. When the pattern is enabled, it should sit at ~10% opacity of `ink` on `paper` — visible but quiet.
- **Container is clean by default**: the diagram sits directly on the page paper, no secondary container background or border. A framed variant (`paper-2` bg + `rule` border + 8px radius + padding) is available as an opt-in for card-heavy layouts, but don't reach for it by default — the extra chrome fights the figure.
