# Video Tutorial Reconstruction

A visual-first skill for turning screen-recorded GUI tutorials into reproducible
instructions, complete code, and checked project artifacts.

[Русская версия](README.ru.md) · [Skill](SKILL.md) ·
[Setup and backends](references/setup-and-backends.md) ·
[Attribution](references/attribution.md) · [MIT license](LICENSE)

## What it does

- Follows the entire video chronologically, then revisits ambiguous actions at
  higher density and resolution. Pixels take priority over subtitles and OCR.
- Preserves evidence and compact state between batches so work can resume.
- Uses a capable local VLM for high-volume analysis, one request at a time.
- Produces dependency-safe intermediate code and complete final listings.
- Checks screenshot provenance, article/source parity, clean project import,
  and runtime behavior where the target application is available.
- Separates verified results, unresolved ambiguity, and checks not run.

**This is an instructional skill, not a one-command video converter.** It needs
an agent with filesystem, shell, and image-inspection tools, a vision model, and
media/application tools appropriate to the tutorial. Installation does not
install a model or a processing pipeline. See [setup](references/setup-and-backends.md).

## Install and use

Ask your agent harness to install the skill from this repository. The entry point
is [SKILL.md](SKILL.md); other files are supporting references. Harness-specific
tool calls may need adaptation outside Hermes.

For Hermes:

```bash
hermes skills install warlock-su/video-tutorial-reconstruction/
```

Keep the trailing `/` for this repository-root skill. Hermes may report CAUTION
for explanatory references about encoded image payloads or proxy URLs; review
the actual findings before choosing `--force`.

```text
/video-tutorial-reconstruction Reconstruct this tutorial: <video URL or local file>
```

Before the first run, configure your backend and verify one real image request.
Private footage is not sent to a remote model without consent.

To update a Hermes-managed installation:

```bash
hermes skills update video-tutorial-reconstruction
```

For a working checkout, Hermes supports
[`skills.external_dirs`](https://hermes-agent.nousresearch.com/docs/user-guide/features/skills).
This lets the harness use the repository files directly, without another copy.
Installation and updates in other harnesses follow their own skill mechanism.

## Checks

Python 3.10+, standard library only:

```bash
python3 -m unittest discover -s tests -v
```

Tests and CI validate the skill bundle, reference links, portability, and retained
quality gates. They do not run a video, a VLM, Godot, or Unity. Runtime and visual
verification belong to each reconstructed tutorial.

## Inspiration and license

Inspired by [Video2GUI](https://github.com/WeiminXiong/Video2GUI), by Weimin Xiong
and co-authors. This is an independently authored skill, not a fork or official
port. No upstream source code, website assets, datasets, or weights are bundled.
The original project retains its Apache-2.0 license; our instructions and tests
are MIT. See [attribution](references/attribution.md) for full credit and citation.

This license does not grant redistribution rights to third-party tutorial videos,
screenshots, code, or assets.
