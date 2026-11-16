# Godot exact-version runtime verification

Use this after reconstructing a Godot tutorial project from video. A clean editor import is necessary but not sufficient: broken NodePaths, missing imported animations, autoload ordering, and `_ready()` failures may appear only after scene startup.

## 1. Pin the source version

Read the exact version/commit from visible editor pixels or logs. Obtain the matching official release for the current OS and architecture, verify its provenance/checksum, and set `GODOT_BIN` to that executable. These are POSIX-shell examples; adapt invocation syntax for PowerShell without changing the version or checks:

```bash
"$GODOT_BIN" --version
```

Do not silently validate an old tutorial only in a newer migrated editor.

## 2. Import and parse

```bash
"$GODOT_BIN" --headless --editor --path /path/to/project --quit --verbose > godot_import.log 2>&1
```

Require exit code 0, then inspect the log for real `SCRIPT ERROR`, parse errors, missing resources, and invalid NodePaths. Verbose logs may contain enum names such as `ERR_PARSE_ERROR`; an enum name alone is not a project failure.

## 3. Use a deterministic SceneTree smoke test

A normal game run may not support a reliable timeout flag in older Godot versions. Ship a small `tests/smoke_test.gd` that extends `SceneTree`, loads the main `PackedScene`, adds it to `root`, waits two `process_frame`s, checks critical node paths/resources/animations, prints a stable success marker, and calls `quit(0)`. On any failed check, print a precise `SMOKE_FAIL:` message and `quit(1)`.

Minimal **Godot 4** pattern (replace the scene and node paths with those established by the tutorial). For Godot 3, adapt the API and launch flags to that exact version; do not run this listing unchanged or migrate the tutorial merely to make the test pass:

```gdscript
extends SceneTree

func _initialize():
    call_deferred("run_test")

func run_test():
    var packed = load("res://scenes/main.tscn")
    if packed == null:
        printerr("SMOKE_FAIL: main scene did not load")
        quit(1)
        return

    var scene = packed.instantiate()
    root.add_child(scene)
    await process_frame
    await process_frame

    for path in ["player/camera_point", "camera_rig/base_camera"]:
        if scene.get_node_or_null(path) == null:
            printerr("SMOKE_FAIL: missing node path: " + path)
            quit(1)
            return

    print("SMOKE_OK: main scene started")
    quit(0)
```

Run it with the exact binary:

```bash
"$GODOT_BIN" --headless --path /path/to/project --script res://tests/smoke_test.gd
```

## 4. Verify imported animation contracts

When code calls `AnimationPlayer.play()`, assert that every named animation exists with `has_animation()`. This catches a project that parses but imported a different model or hierarchy.

## 5. Preserve evidence

Save the exact version output, import log, smoke-test log, and test script in the verification report/package. State separately whether graphical rendering was visually tested; a headless runtime smoke test proves startup and contracts, not final pixels.
