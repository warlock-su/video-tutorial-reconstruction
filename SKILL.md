---
name: video-tutorial-reconstruction
description: "Use when reconstructing GUI tutorials from video."
version: 1.2.0
author: Warlock Su
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [video, tutorials, gui, reconstruction, verification]
---

# Video Tutorial Reconstruction

## When to use

Use when a user needs a standalone, reproducible procedure from a screen-recorded tutorial, especially for IDEs, game engines, creative tools, admin consoles, or other GUI software. This is distinct from transcript summarization: the visual state is the primary evidence.

## Origin and update discipline

This is an independently authored Hermes skill inspired by the methods described in [Video2GUI](https://github.com/WeiminXiong/Video2GUI). It is not the research project's package, an official port, or a one-command video converter. See [attribution](references/attribution.md) for the original work and the distinction between the projects. `video2gui` remains an informal alias; the installed skill name is `video-tutorial-reconstruction`.

Keep updates to this Git repository separate from changes to the research source. Never replace serial local-model analysis, continuity checks, or runtime-verification gates with an upstream README. Report instruction/package validation separately from a real end-to-end video run. Read `references/upstream-and-maintenance.md` before maintaining or releasing this skill.

## Prerequisites and local setup

Use an agent with filesystem, shell, and image-inspection tools, an image-capable model, and tools appropriate to the source application. Read `references/setup-and-backends.md` before the first run or on a new computer. Endpoints, model IDs, credentials, hardware, and work directories are machine-local settings, not repository content. Prefer a capable local VLM for high-volume work; if it is unavailable, agree on a remote backend and its privacy/cost implications before uploading frames. Do not silently send private footage to a cloud service.

## Core rule

Treat the video as a state-transition trace. Recover what the operator did, what changed, and what the application showed afterward. Narration and subtitles are secondary aids, never substitutes for silent clicks, hierarchy changes, Inspector values, code edits, saves, and test runs.

## Required workflow

1. Acquire the original video, metadata, and optional subtitles. Keep downloads resumable. Before large extraction, preflight the visual-analysis backend by listing models and completing one real image request; GPU idleness and API reachability are separate checks. If acquisition or preflight fails, follow `references/source-acquisition-and-preflight.md`.
2. Perform a full-duration uniform coarse visual pass and record state transitions. Process chronological windows covering no more than four minutes of source time by default, using fewer frames if the local VLM's image/context limits require it. Pass a compact carry-forward state into each next window: current scene/file, node hierarchy, confirmed settings, code dependencies, and unfinished actions with evidence timestamps. This state is navigation context, not new visual evidence. Recheck each window boundary so saves, edits, and actions spanning batches are not dropped; do not send full prior reports back into the model.
3. Identify high-risk intervals: code, values, dialogs, hierarchy, drag-and-drop, input mappings, animation settings, and final tests.
4. Re-extract those intervals more densely and at original resolution. For a short ambiguous interaction, first inspect a timestamped before/during/after triplet at t-0.5 s, t, and t+0.5 s (clamped to the video duration). Record the target UI element, visible action, and resulting state; only record exact click coordinates if directly established. If the action remains unclear or spans longer than that triplet, expand the interval and use the existing dense-transition procedure. A triplet is a targeted supplement, never a replacement for full-duration coverage.
5. Reconcile evidence with later and denser frames taking priority; retain uncertainty where the pixels do not establish a value. If code or a numeric control remains ambiguous, run a targeted dense transition pass that records partial typing, completed intermediate states, later corrections, and the last visible final state; do not infer the final code from behavior alone. Treat VLM text as OCR, not authority: models often normalize misspellings/case and confuse operators such as `-=`/`+=`. Before applying a blocker, inspect an enlarged crop of the exact glyphs and cross-check original source files or archives. Resolve names component-by-component—an official filename may preserve a typo while node names, variables, and functions use standard spelling.
6. For a local VLM backend, submit exactly one inference request at a time. Do not parallelize coarse batches, fine batches, transcript synthesis, or validation prompts against the same local GPU: concurrent requests can exhaust memory and severely reduce throughput. Make processing resumable instead—write one output per chronological batch, skip completed outputs on restart, and keep unrelated CPU/network work parallel only when it does not invoke the local model. Follow the local-first discipline below throughout analysis and audits.
7. Write an operational article with explicit UI paths, node/file parents, exact visible parameters, complete code, save steps, and expected postconditions. Preserve executable continuity: if the tutorial builds code incrementally, publish a dependency-safe intermediate listing for early test runs, add later dependencies only after their nodes/singletons/resources exist, and then provide one complete final listing. Do not paste final code early and ask readers to tolerate or comment out broken future references.
8. Audit continuity from the first empty state through the final run.
9. Verify code/project artifacts in the source application's exact version when practical.
10. Inspect every selected screenshot against its caption and validate all relative links.
11. For repeat audits, re-read the current article and artifacts immediately before writing the report: another process may have fixed earlier findings during the audit. Report only defects still present in the latest snapshot.
12. Map published screenshots back to source frames by checksum when files are copied unchanged. Then verify the actual pixels against both the caption and the procedural state at that location—not merely that the image came from the expected interval. A source report can misdescribe a frame; direct pixels take precedence.
13. Separate configuration correctness from evidence correctness. A text/code fix can be valid while a nearby screenshot still shows the unsafe or intermediate pre-fix state; flag the stale screenshot independently.
14. If an original project archive arrives during reconstruction, inspect it before finalizing: integrity-test and hash the untouched archive, read its application/project version, then compare code, serialized scenes/prefabs, input assets, and package metadata against the video. Treat a project saved in a newer application version as a migration snapshot—not automatic proof of the older video state. Video pixels retain precedence; document conflicts instead of silently blending them.
15. Before packaging, require downloadable source files to match the article’s complete code blocks byte-for-byte. Keep mutually exclusive implementations in separate directories, parse every shipped source file, and test the final archive by extracting it into a clean directory. For Godot, preserve original source assets and `*.import` descriptors with their import settings; exclude only regenerated cache appropriate to the target version (`.godot/` for Godot 4). Diagnose import errors instead of deleting metadata; run both fresh headless editor import and the deterministic smoke-test in the exact target Godot version from the extracted copy, and treat first-import errors as packaging failures even if a later smoke succeeds. Only after the final archive passes should video/frames/reports/environments be removed; if a safety gate blocks deletion, report cleanup separately rather than claiming it completed.

## Local-first evidence and context discipline

If a capable local VLM is available, it owns the entire high-volume evidence pipeline—not only frame OCR:

- coarse frame reports;
- dense transition/code reports;
- article-versus-ledger comparison;
- continuity and screenshot-caption audits;
- re-audits after edits.

Run these local requests serially and save every result to disk. Reduce reports mechanically into a compact issue table containing only severity, article location, source timestamp/frame, observed pixels, and proposed correction. The orchestrating/cloud model should read that compact table plus the exact affected snippets, not full ledgers or dozens of verbose reports.

Do **not** use cloud subagents merely to reread or summarize local VLM reports. Inspect the runtime's delegation configuration: child agents may inherit the cloud provider/model and consume the same paid budget. Use cloud delegation only when the work requires reasoning unavailable locally and the input has already been reduced. Avoid repeatedly injecting full transcripts, combined ledgers, report directories, contact-sheet narrations, or unchanged tool output into the parent context.

For a disputed blocker, inspect one enlarged source-frame crop and the relevant artifact directly. Feed the result back into the on-disk issue table; do not launch another full-ledger audit. Before context-heavy work, estimate payload size and prefer scripts that extract headings, exact matches, checksums, diffs, and failures.

## Conditional references

For local-first audit reduction and clean Godot packaging details, see `references/local-first-and-godot-packaging.md`.
For a focused re-audit checklist and reporting pattern, see `references/repeat-blocker-audits.md`.
For targeted code-transition recovery, slider-value reconciliation, screenshot repair, and deterministic package checks, see `references/code-transition-and-package-verification.md`.
For exact-timestamp screenshot audits, serialized VLM queues, large multimodal payload transport, code-fence-independent byte checks, and subtitle-429 recovery, see `references/session-evidence-and-transport-pitfalls.md`.
For reconciling a late-arriving Unity project with an older tutorial video, see `references/unity-project-archive-reconciliation.md`.
For exact-version Godot import and deterministic SceneTree smoke tests, see `references/godot-runtime-verification.md`.

## Output contract

A finished deliverable should include:

- requirements and asset acquisition paths;
- sequential numbered steps, not a recap of the video;
- final trees/hierarchies and exact case-sensitive names;
- complete copyable code;
- screenshots of durable key states;
- expected results after meaningful stages;
- a continuity checklist;
- an explicit note for values set visually but never shown numerically;
- verification evidence from a real parse/run when code is involved.

## Detailed procedure

Read `references/video-first-gui-tutorials.md` for sampling guidance, evidence precedence, executable verification, and recurring failure modes.
