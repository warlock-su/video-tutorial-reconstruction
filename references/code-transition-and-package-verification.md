# Dense code transitions and deterministic package verification

Use this when a coarse/fine pass still leaves uncertainty about final code, numeric GUI values, screenshot suitability, or package integrity.

## Targeted dense code pass

1. Narrow the unresolved edit to the smallest interval using transcript cues and existing reports.
2. Extract full-resolution frames at `0.5 s` spacing by default; use `0.1–0.25 s` only around very fast corrections.
3. Keep timestamped filenames and send frames chronologically. Split long sequences into bounded batches so VLM output does not truncate.
4. Ask for a state machine, not a guessed final listing:
   - line before editing;
   - partial typing/autocomplete;
   - completed intermediate line;
   - deletion/replacement;
   - last completed state before the editor scrolls away.
5. Treat an intermediate completed line as temporary if later frames delete or correct it. In particular, distinguish direct writes from a later target-variable-plus-interpolation implementation.
6. If adjacent batches overlap, reconcile by absolute video timestamp, not batch-relative indices. A model may report `t = 4.5 s` relative to a batch; convert it back to the source timestamp before publishing evidence.
7. Preserve contradictory intermediate states in evidence notes, but publish only the latest confirmed state. This prevents copying a typo that was visibly corrected seconds later.

## OCR normalization and mixed naming

A VLM report is a reading aid, not a transcription oracle. Common false blockers include:

- silently correcting a source typo (`forground` → `foreground`);
- changing case in a case-sensitive path (`visuals/player` → `Visuals/Player`);
- confusing adjacent operator glyphs (`-=` ↔ `+=`, `!=` ↔ `=`);
- extending one typo globally even though it occurs only in a filename, not in nodes/functions.

When an audit proposes a broad rename or code-semantic change:

1. Do not patch from the prose report alone.
2. Crop the exact code/UI region from the original-resolution frame and enlarge it with nearest-neighbor scaling so glyph edges remain inspectable.
3. Compare several later stable frames, especially the saved state immediately before a successful run.
4. Cross-check untouched source assets/repository files, but keep namespaces separate: filename, node name, variable name, function name, and serialized path can legitimately use different spellings.
5. Verify the resulting artifact in the target application. A successful runtime test proves internal consistency, not that every spelling is video-exact; retain the pixel/source provenance for that claim.

## Dependency-safe evolving listings

A final script can be correct yet break an earlier tutorial step when it references a node, Autoload/singleton, resource, or input action that has not been created yet. For an executable reconstruction:

1. At the first test, publish the coherent script state that existed at that point, without future dependencies.
2. When each dependency is created, show the exact insertion (`@onready`, singleton call, resource path) and save step.
3. After the last dependency exists, provide one complete final copyable listing and byte-check it against the shipped file.
4. Do not instruct readers to endure parser/runtime errors or temporarily comment out final lines merely because the article pasted the final script too early.

## Numeric controls and narration

- Narration such as “about 0.7” is approximate. Inspect the numeric field at the end of the drag and the first frame after selection moves away. Publish the last visible value (for example `0.665`) and mention the spoken approximation separately.
- A late frame with a default value is not automatically final. Follow the control through the actual edit transition.

## Screenshot audit and repair

1. Audit caption accuracy, procedural timing, and nearby article claims independently.
2. If a multi-image audit truncates, continue with smaller ordered chunks; do not treat missing audit output as PASS.
3. Replace frames that show menus mid-click, autocomplete, temporary errors, or pre-correction values unless documenting that transient state.
4. Cropping is acceptable when it removes unrelated video overlays while preserving the complete UI/code evidence. Record the source timestamp and disclose the crop in the screenshot manifest.
5. Re-audit replacement frames directly; do not inherit the verdict of the replaced image.

## Continuity QA

- Give the QA reviewer source-specific facts that generic domain knowledge may misclassify. For example, a menu location visible in an older application version overrides expectations from newer versions.
- Require `BLOCKERS`, `MAJOR`, `MINOR`, and `PASS/FAIL` so fixes can be prioritized.
- Re-run QA after fixes. A PASS with only minor editorial notes is acceptable only after link/code/package checks also pass.

## Deterministic package verification

Before archiving, run a verifier that checks:

- every local Markdown link resolves;
- every image reference exists and is unique;
- expected screenshot count equals actual files;
- generated HTML references the same images;
- required operational strings/steps are present;
- every shipped source file parses with the appropriate language parser;
- common secret/token patterns are absent;
- the final archive opens, passes an integrity test, and contains required files.

Generate the archive only after verification, then integrity-test the archive itself. Compute a checksum and report it. Remove source video, dense frames, model reports, temporary environments, and temporary routing rules only after the verified archive exists.

## Delayed process notifications

A delayed failure notification may describe an earlier superseded attempt. Before restarting work or reporting failure, inspect current artifacts and live state. Prefer verified files and current probes over stale background output.
