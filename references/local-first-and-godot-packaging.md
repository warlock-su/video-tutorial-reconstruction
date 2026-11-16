# Local-first audit and clean Godot packaging

## Local-first evidence pipeline

When a local VLM is available, keep high-volume multimodal work local through the re-audit stage:

1. Write one coarse/fine report per chronological batch.
2. Ask the local model to compare the current article against those on-disk reports.
3. Mechanically reduce findings to: severity, article location, frame/timestamp, observed pixels, correction.
4. Give the orchestrating model only that issue table and affected snippets.
5. For conflicts, inspect one enlarged source crop and update the issue table; do not rerun full cloud audits.

Cloud delegation is not a free local-model substitute: inspect the runtime's configuration, because child agents may inherit the cloud model and consume the same paid budget.

## Godot release packaging

Distinguish project import configuration from regenerated cache:

- Keep original source assets and `*.import` descriptors with their import settings. These descriptors are important project metadata, even when they reference `.godot/imported/`.
- Exclude only regenerated cache appropriate to the exact target version: `.godot/` for Godot 4. Do not infer or perform a version migration during packaging.

The official Godot [Import process — Files generated](https://docs.godotengine.org/en/stable/tutorials/assets_pipeline/import_process.html#files-generated) documentation says `<asset>.import` contains import configuration and should be committed as important metadata; imported cache is regenerated automatically, so committing `.godot/` is not recommended. The [official documentation source](https://raw.githubusercontent.com/godotengine/godot-docs/master/tutorials/assets_pipeline/import_process.rst) provides the same distinction.

Diagnose first-import errors such as `Cannot open file res://.godot/imported/...` by checking original assets, descriptor paths/settings, and the exact editor version. Fix the cause rather than deleting import metadata or dismissing errors because a later run succeeds.

Verification sequence:

1. Build the release with original source assets and retained `*.import` descriptors/settings. Omit only version-appropriate regenerated Godot cache (`.godot/` for Godot 4); also leave out source video, frame ledgers, and local environments.
2. Create the archive and run the archive integrity test.
3. Extract into a genuinely clean directory.
4. Run the exact target Godot version with `--headless --editor --path <project> --quit`.
5. Scan the import log for `ERROR`, `SCRIPT ERROR`, `Parse Error`, `Node not found`, and `Animation not found`.
6. Run a deterministic SceneTree smoke-test from the extracted copy.
7. Rebuild and repeat if either import or smoke emits a real error; a later successful smoke does not erase a first-import packaging error.
8. Record archive SHA-256 only after the final rebuild.

Do not report temporary-data cleanup as complete if a safety gate blocked deletion. The artifact may still be complete; state cleanup separately.
