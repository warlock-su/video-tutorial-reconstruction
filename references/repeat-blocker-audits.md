# Repeat blocker audits for video-derived tutorials

Use this checklist when auditing a revised article after earlier findings have already been addressed.

## Scope discipline

1. Re-read the current article, standalone code artifacts, and screenshot directory; do not audit a cached earlier version.
2. Convert the user's named concerns into a short blocker matrix.
3. For each concern, classify the latest state as:
   - **still blocking** — current text/code/pixels conflict or prevent reproduction;
   - **fixed, evidence stale** — implementation is corrected but a screenshot/caption still depicts the old state;
   - **cleared** — current implementation and evidence agree;
   - **source-underdetermined** — pixels do not establish a final value, so the article must retain uncertainty.
4. Report only current blockers as findings; keep cleared items in a compact verification section so old defects are not accidentally re-raised.

## Screenshot provenance and validation

When article images appear copied from extracted frames:

1. Hash every article screenshot and every candidate source frame.
2. Map exact hash matches to interval and timestamp.
3. Validate each image on three independent axes:
   - **caption accuracy** — does the image literally show what the caption claims?
   - **procedural timing** — is it a final state, or an intermediate/dirty/typing state?
   - **local consistency** — does it agree with the instructions immediately around it?
4. Read the pixels even when a fine report describes the same filename. If the report and pixels conflict, record the discrepancy and prefer the pixels.
5. A screenshot may be valid evidence of an original unsafe state but invalid as evidence of the article's editorially corrected final state. Caption it explicitly as “before correction” or replace it.

## Code and behavior checks

- Trace sentinel/default values through both hit and miss branches. A variable initialized to a world origin or null can affect aim, spawning, and VFX after a raycast miss.
- Distinguish `raycastHit.point` from an object's `Transform.position`; do not call an object pivot the hit point.
- Keep editorial repairs visibly labeled and apply them consistently in:
  - the procedural snippet;
  - every complete listing;
  - standalone code artifacts;
  - troubleshooting and continuity sections.
- For parallel implementations such as projectile and hitscan, audit each independently. Do not let a complete primary variant hide an unsupported alternative.

## Evidence-only reporting

- Do not fill missing Inspector values from conventions or modern defaults.
- Do not infer checked control schemes when the boxes are visibly unchecked or unreadable.
- State exactly what a final gameplay frame proves. Aim pose plus crosshair does not prove projectile flight or hit VFX unless those pixels are present.
- If no source frame shows an editorially corrected Inspector, say so; do not present the pre-fix frame as final.

## Report structure

1. One-paragraph verdict with blocker count.
2. One section per remaining blocker:
   - current article claim;
   - pixel/fine-report evidence;
   - why it blocks reproduction;
   - evidence-safe resolution.
3. Compact “cleared checks” section.
4. Priority-ordered fix list.
5. Save the report first, then re-read it fully to verify it was not truncated.
