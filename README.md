# Video Tutorial Reconstruction

A visual-first [Hermes Agent](https://hermes-agent.nousresearch.com/docs/)
skill for turning screen-recorded tutorials into reproducible instructions,
complete code, and checked project artifacts.

[Русская версия](README.ru.md) · [Skill](SKILL.md) ·
[Setup and backends](references/setup-and-backends.md) ·
[Attribution](references/attribution.md) · [MIT license](LICENSE)

**This is an instructional skill, not a one-command video converter.** It teaches
an agent how to inspect the video and verify a reconstruction using tools and a
vision model you supply. Installing it does not download a model or install a
media-processing engine. No tutorial footage, project archives, credentials, or
private backend configuration are included.

## What it does differently

- Inspect the entire video chronologically, then revisit risky moments at higher
  density/resolution. Pixels take priority over subtitles and normalized OCR.
- Carry compact state between batches; preserve evidence and resume interrupted
  work rather than starting over.
- Use a capable local VLM for high-volume analysis and audits, with **one request
  at a time** per local backend/GPU. Do not silently upload private frames.
- Write dependency-safe intermediate code, not final code that references nodes
  and resources the reader has not created yet.
- Check screenshot captions/provenance, source-code parity, clean archive import,
  and actual runtime behavior where the target application is available.
- Distinguish verified results, unresolved visual ambiguity, and checks not run.

Useful for game engines, IDEs, creative applications, and other GUI tutorials.
It is not a transcript summarizer, an autonomous mouse-control agent, or a
reproduction of the Video2GUI research pipeline.

## Install for use (native Hermes lifecycle)

With a current Hermes installation:

```bash
hermes skills install warlock-su/video-tutorial-reconstruction/
```

Keep the trailing `/`: it selects the repository root, where SKILL.md lives.
The current Hermes identifier parser requires that explicit root path.

Review the community-skill security scan and any confirmation prompt. Some
Hermes scanner versions mark this repository **CAUTION** for documented clone
commands, subprocess-based Git-update tests, or prose about encoded image
payloads and credential handling. Read the actual findings: those categories
are not permission to ignore a real credential or network-exfiltration issue.
If you have reviewed the current bundle and accept the reported cautions, rerun
with `hermes skills install warlock-su/video-tutorial-reconstruction/ --force`.
Never override an unknown finding blindly; a dangerous verdict remains blocked.
Open a new Hermes session if the skill index has not refreshed, then invoke:

```text
/video-tutorial-reconstruction Reconstruct this tutorial: <video URL or local file>
```

Before the first video, complete [backend setup](references/setup-and-backends.md):
check source access, required media tools, and one real image-model request.

To receive published updates:

```bash
hermes skills check
hermes skills update video-tutorial-reconstruction
```

Native installation downloads a copy; it is **not** a Git checkout. Hermes
normally preserves local modifications by skipping them during updates. Review
and save your changes instead of forcing replacement. If the skill is already
installed locally, choose one mode below rather than creating duplicate names.

## Install for development (one Git source of truth)

Choose this mode when you want the installed skill and a working Git tree to be
the **same files**, including lessons written by the agent. Use Hermes' supported
external-directory feature, not a copied skill or a filesystem link:

```bash
git clone https://github.com/warlock-su/video-tutorial-reconstruction.git   ~/projects/video-tutorial-reconstruction
cd ~/projects/video-tutorial-reconstruction
hermes config get skills.external_dirs --json
```

If the result is `[]`, register this checkout in the active profile:

```bash
hermes config set skills.external_dirs '["~/projects/video-tutorial-reconstruction"]'
```

**If the list is not empty, preserve every existing entry and append this path**
to the JSON array instead of replacing the list with the example above. Hermes
resolves the active profile from its normal profile selection/`HERMES_HOME`.
No installer, symlink privileges, dependency installation, or service is needed.
The agent can edit writable external skills; this is intentional, not read-only.

**Migrating an existing skill:** first inspect and back up its directory outside
any scanned `skills/` tree. Review/merge local lessons, then move the old directory
out of the way: a profile-local copy takes precedence over external directories.
Do not delete it or force replacement just to make migration pass. Do not mix
native-copy and external-checkout installs in one profile. Open a new session and
verify which directory `skill_view` loads. Shell examples here use POSIX quoting;
on Windows use the corresponding shell syntax and `python` where appropriate.

**Why no symlink helper?** Some Hermes versions index and read symlinked skill
directories but do not traverse them for `skill_manage` writes. External
directories support both operations. Do not assume a successful read proves
that future lessons can be saved.

### Pull published updates

Only pull with a clean working tree. Stop and review local edits first:

```bash
git -C ~/projects/video-tutorial-reconstruction status --short
git -C ~/projects/video-tutorial-reconstruction pull --ff-only
python3 -m unittest discover -s ~/projects/video-tutorial-reconstruction/tests -v
```

The registered directory sees new files immediately; no reinstall is needed. A new Hermes
session refreshes the skill index. If `--ff-only` fails, do not reset or overwrite
local edits: inspect the divergence. Agent-written lessons change this checkout
but remain **local** until explicitly reviewed, committed, and pushed.

### Publish reviewed changes

Use a branch/PR when collaborating. Run the tests and inspect the complete
staged diff for private material before pushing. Stage only intended paths;
keep per-video evidence and machine-local backend settings elsewhere. See
[maintenance](references/upstream-and-maintenance.md) for the release gates.

## Repository layout

```text
SKILL.md            Agent instructions and quality gates
references/         Conditional procedures, setup, and attribution
tests/              Bundle and Git-update regression checks
LICENSE             MIT license for this implementation
```

## Verification and limitations

```bash
python3 -m unittest discover -s tests -v
```

The tests cover Git updates and the skill bundle's structural/portability
gates. CI runs those checks; it does **not** run an actual tutorial, a VLM, Godot,
or Unity. The Godot smoke-test listing is a replaceable Godot 4 example, not a
ready-made verifier for arbitrary projects. Visual/rendering checks and exact
application-version runtime tests must be reported for each reconstructed video.

## Inspiration and license

Inspired by [Video2GUI](https://github.com/WeiminXiong/Video2GUI), by Weimin Xiong
and co-authors. This is a standalone, independently authored skill, not a fork,
port, or official release. No upstream source code, website assets, datasets,
or model weights are bundled. The research project retains its Apache-2.0 terms;
our own instructions and tests are MIT. Full credit and citation are in
[attribution](references/attribution.md).

The MIT license does not grant rights to redistribute someone else's tutorial,
screenshots, code, or assets. Check those separately before publishing outputs.
