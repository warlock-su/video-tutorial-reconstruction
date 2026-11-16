# Reconciling a Unity project archive with an older tutorial video

Use this when project files arrive after a video-first reconstruction has begun, especially when the archive was later opened in a newer Unity version.

## 1. Preserve and identify the source

- Keep the received archive byte-for-byte unchanged.
- Run `unzip -t <archive>` before extraction.
- Record a SHA-256 hash and verify any copy included in the deliverable has the same hash.
- Extract into a separate `original_project/` directory; never overlay it onto the reconstruction workspace.
- Read `ProjectSettings/ProjectVersion.txt` and `Packages/manifest.json` before treating source code as version-compatible.

## 2. Treat migrated projects as consistency evidence

A newer project snapshot may contain automatic API migrations, package upgrades, renamed scene assets, regenerated serialization, or later author edits. It is not automatic proof of the state shown in an older video.

Evidence precedence remains:

1. final and dense video pixels;
2. earlier/coarser video pixels;
3. narration/subtitles;
4. supplied project archive as a consistency check.

When the archive conflicts with the video, publish both states explicitly. Typical Unity examples:

- `Rigidbody.velocity` in Unity 2020 versus `Rigidbody.linearVelocity` after migration;
- changed projectile speed or other author tuning;
- newer package versions that cannot establish the old package versions;
- source files that retain an intermediate bug later fixed in serialized scene state.

## 3. Mine authoritative serialized state

Inspect these files directly:

- `*.cs` for complete author code and exact constants;
- `*.inputactions` for action names, bindings, groups, and interactions;
- `*.unity` for GameObject activity, hierarchy references, component fields, layer masks, and local transforms;
- `*.prefab` for root/child structure, colliders, Rigidbody flags, materials, and serialized script fields;
- `*.controller` for Animator layers/states where text serialization is available;
- `*.meta` to resolve GUIDs in scenes/prefabs to actual assets.

Useful reconciliation pattern:

1. Locate the serialized field or GUID in the scene/prefab.
2. Resolve referenced GUIDs through `.meta` files.
3. Compare against the exact full-resolution video frame.
4. Classify the result as video-confirmed, subtitle-supported, reconstructed/editorial, or unresolved.
5. Never let the archive silently overwrite a contradictory video-visible value.

## 4. Distinguish intermediate screenshots from final source state

A screenshot can accurately document an intermediate stage while being unsafe as a final instruction. For example, a temporary debug object may still have a Collider in the video frame while the final scene has no Collider and the object is inactive.

Keep the screenshot only when its caption explicitly says it is intermediate and the procedure clearly states the final state. Otherwise replace it with a durable final-state frame.

Never trust report attachment numbers alone. Open the actual candidate pixels, then map the published image back to its source frame by SHA-256.

## 5. Reconcile Input System details carefully

For `PlayerInput`, distinguish notification modes:

- `Send Messages` calls methods such as `OnAim(InputValue)` by action name; it does not create UnityEvent fields in the Inspector.
- `Invoke Unity Events` exposes assignable Inspector events.

Compare visible control-scheme checkboxes with the `.inputactions` JSON. If a migrated asset assigns groups that are not visibly selected in the video, state the discrepancy rather than presenting one as proof of the other. Also detect binding conflicts across actions, such as two actions sharing the same gamepad trigger.

## 6. Cross-check runtime semantics, not only syntax

Project files often expose issues a parser cannot:

- a raycast debug marker colliding with its own ray;
- a raycast miss leaving the aim target at world origin;
- VFX spawned at `transform.position` or an object pivot instead of `raycastHit.point`;
- marker scripts placed on a parent while collision code calls `other.GetComponent<T>()` on a child collider;
- duplicate colliders in a projectile compound body;
- mutually exclusive implementations declaring the same public class.

Label robust fixes as editorial/reconstructed when they differ from the literal video or supplied source.

## 7. Packaging and cleanup gate

Before deleting source video, dense frames, reports, or virtual environments:

- render the final readable artifact;
- validate every local link and image;
- verify every screenshot opens and has a source-frame hash mapping;
- extract article code blocks and compare them byte-for-byte with downloadable code files;
- parse every shipped source file;
- keep incompatible alternatives in separate directories;
- include the untouched project archive only with its version/migration warning;
- build the final ZIP and test-extract it;
- only then remove heavyweight temporary evidence.

If the exact Unity Editor is unavailable, say that syntax and serialization were checked but Unity batchmode compile/playmode was not performed.