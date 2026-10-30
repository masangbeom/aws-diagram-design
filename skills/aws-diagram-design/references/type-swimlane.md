# Swimlane

**Best for:** cross-functional processes, RACI-style flows, vendor handoffs, multi-team shipping workflows.

**Not this type:** what the customer sees vs what stays hidden, on one shared stage grid → **Service blueprint** (`type-service-blueprint.md`). A blueprint has no arrows; stage order is the sequence.

## Layout conventions
- Horizontal lanes (or vertical columns) — one per actor/team. Label each lane in the left margin (or top) with an `eyebrow`-role label.
- Lane dividers: 1px hairlines.
- Process steps are rectangles placed inside the lane of the actor performing them; arrows show flow.
- Handoffs (arrows crossing lane boundaries) are the most important edges — consider coral on the handoff that introduces the most coupling or latency.
- Don't force equal step count per lane; a lane with one step is fine.

## On AWS

- Lanes are the parties that own the step: teams, AWS accounts, or an AWS-managed actor (`AWS Support`, `Pipeline`). Don't make one lane per service; a service is a step in its owner's lane, with its icon.
- Common AWS swimlanes: a CodePipeline release with manual approval, an incident through AWS Support, an account-vending request through Control Tower.

## Anti-patterns
- Lanes without labels.
- A step drawn across two lanes (pick one owner).
- Arrows that snake back and forth — reorder steps so the flow is mostly straight.

## Examples
- `assets/example-swimlane.html` — minimal light
- `assets/example-swimlane-dark.html` — minimal dark
- `assets/example-swimlane-full.html` — full editorial
