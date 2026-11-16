# Evidence and transport pitfalls from long GUI-video reconstructions

## Screenshot evidence must be audited after extraction

1. Extract every article placeholder at its exact timestamp.
2. Build contact sheets that include timestamp, target filename, and proposed caption.
3. Inspect the actual pixels against both the caption and the procedural state.
4. Classify each candidate as `MATCH`, `STALE-INTERMEDIATE`, or `WRONG`.
5. Remove a screenshot when no clean source state exists; do not crop away visible parser/runtime errors merely to make the evidence look clean.
6. A static frame cannot prove two temporal states. Use two separately captioned images or a labeled side-by-side composite for before/after, foreground/background, enabled/disabled, or pass/fail claims.
7. If one Inspector instance proves only one of two similarly configured nodes, make the caption singular and say the other node is configured analogously.

## Code-block/package comparison

Compare source-file bytes against the article block contents independently of Markdown fence language. A shader may use `glsl` while GDScript uses `gdscript`; checking for a hard-coded fence label can create a false mismatch. Parse fenced blocks or search for the exact file contents, then report the fence language separately.

## Resumable serialized VLM pipeline

- Write one report per chronological batch and skip reports that already exist and exceed a small sanity threshold.
- Keep coarse and fine passes in separate processes, but gate fine startup on coarse process completion and an exact expected report count.
- Never let the queued fine pass overlap the coarse pass on a single-GPU endpoint.
- Keep transcript/article work on CPU or remote agents while the local VLM is busy.

## Large multimodal payloads

Base64 image payloads can exceed the OS argument-size limit when passed inline to `curl --data-binary <json>`. Write JSON to a temporary file and use `curl --data-binary @payload.json`; delete the temporary file automatically afterward. Keep credentials in headers loaded from protected environment/config files and never serialize them into saved payloads or logs.

## YouTube subtitle 429 fallback

When video download succeeds but subtitle download returns HTTP 429:

1. Save `--write-info-json` during the successful metadata/video request.
2. Read the exact `automatic_captions[language]` URL for `vtt` or `json3` from the info JSON.
3. Fetch that URL through the same working network interface or proxy used for the video.
4. Validate non-zero bytes and cue count before continuing.

This is a fallback, not proof that transcript helpers are generally broken. Pixels remain the primary evidence.