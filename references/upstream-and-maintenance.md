# Skill maintenance and research-source comparison

## Maintain this skill

Repository: https://github.com/warlock-su/video-tutorial-reconstruction.
Video2GUI is research inspiration, not this skill's source branch.

- Edit the source actually loaded by the harness. Hermes can use a writable
  checkout through `skills.external_dirs`; a native installation is a separate
  managed copy. Use the harness's own installation and update mechanism.
- Keep machine-local settings, credentials, and per-video evidence outside the
  reusable skill package.
- Keep always-needed gates in SKILL.md and conditional detail in topical
  references. Preserve serial inference, full visual coverage, continuity,
  compact local-first audits, source-code parity, and clean-runtime checks.
- Run the bundle checks after edits. Structural validation is not a new video
  reconstruction; report actual model/application runs separately.
- Keep public documentation focused on installation, use, dependencies, and
  skill-specific behavior, not generic Git practices. Publish changes only when
  requested.

## Compare Video2GUI only when requested

1. Distinguish this skill, the research repository, dependency packages, and
   executable extraction scripts. Updating one is not proof that others changed.
2. Use https://github.com/WeiminXiong/Video2GUI as the research source. Recover a
   previously used revision from actual Git output; do not infer it from dates
   or assume an old working directory still exists.
3. If a source clone exists, inspect its status, remotes, and HEAD before fetching;
   preserve local modifications. Otherwise clone into the active scratch space
   without executing downloaded code.
4. Discover its current default branch with `git ls-remote --symref origin HEAD`,
   fetch, and compare full hashes with the recovered baseline. Inspect
   `git log --oneline <baseline>..<head>`, `git diff --stat <baseline> <head>`, and
   focused diffs. If no baseline is recoverable, report only the current revision.
5. Inspect `git ls-tree -r --name-only <head>` before describing executable
   availability. README wording is not evidence of a shipped pipeline or skill;
   an earlier absence does not establish permanent absence.
6. If the revision is unchanged, say so. Adopt relevant methods deliberately,
   without replacing this skill's purpose with dataset generation. Keep original
   notices/licenses for any copied material; this project's MIT license does not
   override third-party terms. See `references/attribution.md`.
7. Report separately: verified research-source delta, actual skill changes,
   executed checks, and work not run. Do not manufacture release notes or make
   unrelated changes merely to claim an upstream update.
