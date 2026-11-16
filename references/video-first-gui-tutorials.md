# Video-first reconstruction of GUI tutorials

## Evidence hierarchy

1. Final visible application state and later frames.
2. Dense, full-resolution visual pass over the relevant interval.
3. Uniform coarse visual pass over the whole video.
4. Speech/transcript only for navigation and terminology.
5. External examples or recreated projects only as consistency checks.

If sources conflict, do not silently blend them. Prefer later/finer visual evidence and explicitly resolve the discrepancy. Never invent exact numeric transforms when the video only uses a gizmo without displaying a numeric readout.

## Coarse-to-fine sampling

1. Preserve the original video locally and record duration, resolution, and visible application version.
2. Sample the full duration uniformly. For a 20–40 minute GUI tutorial, one frame every 6–10 seconds is a useful starting point. Add scene-change frames where brief dialogs or menus may be missed.
3. Batch frames chronologically. Encode timestamps with fixed-width numeric fields; naive lexicographic ordering of unpadded timestamps can scramble the timeline.
4. For every transition, capture:
   - state before;
   - visible action;
   - state after;
   - selected item and hierarchy;
   - Inspector/property values;
   - code additions/deletions;
   - save/run/test events;
   - unresolved ambiguity.
5. Build a chronological action ledger and flag high-risk intervals: code editing, short dialogs, drag-and-drop, hierarchy changes, numeric values, input bindings, animation settings, and final test runs.
6. Re-extract high-risk intervals at original resolution and 2–4 second spacing. Use sub-second to 2-second spacing around brief clicks, autocomplete, error correction, or typed values.
7. When dense extraction yields thousands of near-duplicates, select a bounded chronological set per interval using both:
   - uniform temporal coverage, so quiet but important final states survive;
   - the largest adjacent visual changes, so dialogs, code scrolls, Inspector edits, and mode switches survive.
   Keep the full-resolution selected frames and a manifest with exact source timestamps. Do not use change score alone: typed code or a one-field value edit may have low pixel difference.
8. Validate every model-generated interval before feeding it to extraction. Check that start/end timestamps are within the video duration, start precedes end, and the parser has not confused `HH:MM:SS` with `MM:SS:frames` (for example, `03:20:00` instead of `00:03:20`). Normalize timestamps deterministically rather than trusting a machine-readable section merely because its syntax is valid.
9. Reconcile fine outputs against the full timeline. A fine batch may end before an action is completed; absence in that slice is not evidence that it never happens later.

## Screenshot selection

Select screenshots only after reconstructing the procedure. Verify each image against its caption. Replace frames captured during typing, stale parser errors, splash screens, or transient dialogs unless that transient state is specifically being documented.

Useful screenshot states include:

- final hierarchy after node/file creation;
- Inspector with the changed property visible;
- final code block after parser errors clear;
- input-action table after bindings are assigned;
- gameplay/application result after a successful run.

## Continuity audit

Before delivery, verify:

- Every asset has an acquisition URL and exact destination path.
- Every child node has an explicit parent; infer hierarchy from indentation, not proximity.
- Final trees agree with earlier creation and instancing steps.
- Code paths agree with exact case-sensitive node names.
- Input actions, animation names, and Inspector values agree with the final code.
- Save and main-scene selection steps occur before the first relevant run.
- Each test states an observable expected result.
- Visually positioned parameters are labeled as visual, not assigned fabricated numbers.
- All local screenshot links resolve.
- The complete article code matches the tested standalone file byte-for-byte.

## Executable verification

When the output includes code or a project:

1. Use the exact application/runtime version visible in the source when practical.
2. Put the final code into a minimal validation project containing the reconstructed node paths.
3. Use the real referenced asset when it carries required children or animation names.
4. Run headless editor import/parse, then launch the main scene briefly.
5. Search logs for parser errors, missing nodes, invalid resources, and missing animations.
6. Distinguish expected headless warnings (for example unavailable mouse/display) from application errors.

A clean parse alone is insufficient: runtime node-path and animation errors often appear only after scene startup.

## Common failure modes

- A single frame captures an intermediate typo rather than final code.
- VLMs may misread `-=` as `+=`, omit `@`, or confuse similarly indented nodes. Re-check high-resolution frames and execute the code.
- Sparse sampling can mistake viewport orbiting for node movement. Require a gizmo readout, Inspector change, or before/after camera preview.
- Imported scenes may require **Make Local** before their children or AnimationPlayer can be edited.
- Dragging a texture onto geometry may create a material in `Geometry > Material Override` while the primitive's top-level `Material` remains empty.
- A late timestamp is not proof of a final state; inspect the pixels.
- Independent recreations or source repositories are useful for candidate values, but cannot override the actual video.
