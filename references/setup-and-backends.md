# Setup, dependencies, and backend contract

## What is installed

This repository contains an instructional skill and its regression tests,
not a downloader, frame extractor, VLM server, or automatic article generator.
Installing the skill does not install those tools or start a model. The agent
selects and exercises suitable tools for each tutorial.

## Prerequisites

- Hermes Agent with filesystem, terminal, and image-inspection tools. Other
  agents may use the Markdown methodology, but Hermes-specific tool calls and
  installation instructions need equivalents.
- An image-capable model that can inspect the source resolution and enough
  frames per request. A local Qwen-family VLM, LM Studio, or another compatible
  local server is an option, not a required model or product.
- FFmpeg/ffprobe for media probing and timestamped frame extraction; verify the
  executable versions before a run.
- A local video file or an authorized source. `yt-dlp` is optional for supported
  network sources. Optional subtitles never replace visual evidence.
- Python 3.10+ for the bundle checks, using only the standard library.
  Git is needed only when working from a checkout. `curl` is optional when
  another HTTP client is available.
- Image crop/inspection, archive-integrity, and SHA-256 tools, provided by the
  agent's tools, Python libraries, or suitable system utilities.
- The exact target editor/runtime when executable verification is required.
  Godot/Unity, source parsers, and ZIP tools are task-dependent, not global
  dependencies. Installation of the skill does not validate those applications.

Shell examples in references use POSIX syntax. On Windows, use the native
Hermes skill installer or register the checkout with `skills.external_dirs`,
adapting shell quoting as needed. Do not claim OS-specific commands
were tested merely because the Markdown is platform-neutral.

## Per-machine backend contract

Agree on and record these settings in a private task/environment configuration
outside this repository:

1. Backend type and base URL; model identifier; authentication source, if any.
2. Actual image-input support, image-count/pixel limits, and context limits.
3. Allowed work directory and evidence retention policy.
4. Whether any private frames may leave the machine; remote inference cost and
   consent when a suitable local backend is unavailable.
5. Transport requirements, if already configured: interface/proxy, timeout,
   and retry behavior. Do not change networking to meet these without approval.

This is a contract, not a config file parsed by shipped pipeline code. There
is no mandatory environment-variable schema and no hard-coded model tuning.
Use the model provider's supported API and the user's existing settings; do not
invent overrides. Keep secrets in a secret store or a protected local environment,
not in a shared document, URL, command literal, Git remote, or committed `.env`.
Do not copy another machine's private addresses or model identifiers blindly.

## Preflight acceptance

Before full extraction, list available models (where the backend supports it)
and complete one real image request through the intended network route. Confirm
that the response describes the supplied image, not just that HTTP returned 200.
Probe the video with ffprobe, save the actual source duration, and plan full
chronological coverage. Exactly one inference request may be active against a
local backend/GPU at a time, including retries and audits. Queue work and save
one report per batch so interruption does not force a full restart.

Use `references/source-acquisition-and-preflight.md` for acquisition failures.

## Keep source and evidence separate

Put downloads, frames, ledgers, generated articles, application projects, and
archives in a separate task work directory, not in this skill's Git checkout.
The checkout is only the reusable skill and its tests/docs. Private footage,
credentials, and machine-local settings are not part of the shared package.
