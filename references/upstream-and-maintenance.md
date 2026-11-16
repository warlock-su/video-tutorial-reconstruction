# Skill repository maintenance and research-source comparison

## Update this skill from Git

The skill's own repository is
https://github.com/warlock-su/video-tutorial-reconstruction.
Video2GUI is research inspiration, not the source branch to merge into it.

1. Locate the actual installation and checkout before editing. In developer mode,
   `skills.external_dirs` registers the repository itself; edit that source, not
   a second copy. `skill_manage` can update a writable external skill in place,
   but its changes remain local until committed. Do not replace this with a
   symlink untested for writes: some Hermes versions read linked directories but
   omit them from skill_manage's directory traversal. Preserve other entries
   whenever editing the external-directory list through `hermes config set`.
2. Inspect `git status --short`, `git remote -v`, and `git rev-parse HEAD`. Keep
   machine-local settings and task evidence outside the repository. Preserve
   uncommitted lessons; do not use reset, clean, force-push, or stash blindly.
3. For an unmodified consumer checkout, use `git pull --ff-only`, then run
   `python3 -m unittest discover -s tests -v`. If there are local edits, stop and
   review/commit them before updating. The registered directory needs no reinstallation after a
   pull; a new Hermes session is the most portable way to refresh its skill index.
4. For a native Hub installation, use `hermes skills check` and
   `hermes skills update video-tutorial-reconstruction`. Native installs are
   copies, not Git working trees. Locally modified installs are normally skipped;
   inspect changes instead of using `--force` by default. Do not mix both modes
   in one profile, because duplicate names obscure the active source.
5. Make focused changes: always-needed gates belong in SKILL.md; conditional
   detail belongs in topical references. Preserve serial inference, full visual
   coverage, continuity, local-first compact audits, source-code parity, and
   clean-runtime/package checks.
6. Before release, run the full tests, inspect staged content for secrets/private
   data, and exercise changed scripts with disposable profiles. A successful
   structural check is not proof of a new video reconstruction. Commit/push only
   the intended files; remote publication requires authorization. Verify the
   actual remote commit/content after pushing before reporting success.

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
