# Source acquisition and preflight

Use this when a GUI tutorial cannot be downloaded directly or when the visual-analysis backend may be unavailable.

## Preflight before expensive extraction

1. Probe the intended VLM endpoint and list models before generating thousands of frames.
2. Confirm the exact multimodal model is loaded and accepts one small image request. For base64 image payloads, write the JSON body to a protected temporary file and send it with `curl --data-binary @payload.json`; putting the full payload in a process argument can exceed `ARG_MAX` before the request reaches the model.
3. Record video metadata and preserve resumable intermediate files.
4. Only then begin coarse extraction and sequential VLM batches.

A claim that the GPU is idle does not prove the API is reachable. Verify both separately: transport/list-models first, then a real one-image completion.

## YouTube acquisition fallback ladder

1. Use `yt-dlp` normally and preserve `.part` files so retries resume.
2. If the user already has an authorized, working VPN/interface, `yt-dlp --source-address <VPN-IP>` can select its source address. Interface and routing behavior are OS-specific. Do not add policy routes, alter a VPN, or change host networking without explicit approval; prefer an existing supported route.
3. If the user already has an authorized proxy, supply its actual URL with `yt-dlp --proxy <PROXY_URL>`. A local SOCKS proxy may use `socks5h://127.0.0.1:9050`, but that is only an example, not an assumed service. Starting a Tor daemon, installing helpers, or changing proxy/VPN routing requires separate approval and a cleanup plan. A lawful local video file is a valid alternative to network recovery.
4. Download subtitles and metadata in the same successful authenticated/network path; do not assume a transcript helper uses the same route.
   - If `yt-dlp --write-auto-subs` obtains metadata but aborts on subtitle HTTP 429, retry the video without subtitles so acquisition can finish.
   - Then read the desired `automatic_captions` entry from the saved `.info.json` and download its `vtt` URL directly with the same working interface/proxy (`curl --interface <vpn-interface> ...`). Validate non-zero bytes and cue count before use.
   - This avoids repeating the expensive video request and keeps subtitles optional/navigation-only.
5. If subtitles remain unavailable, inspect the tutorial creator’s own site for an official transcript or project-file page. Treat transcript text as navigation evidence only; visuals remain authoritative.

## Resumability and cleanup

- Keep `yt-dlp` output names stable across retries so partial downloads resume.
- Verify the merged file with `ffprobe` before deleting source fragments.
- Record every temporary route, proxy service, package, and daemon introduced during recovery.
- At delivery, undo only the temporary policy rules and helpers introduced for this task, with the required approval. Do not stop, uninstall, or reconfigure the user's pre-existing network services. Report blocked cleanup separately.

## Pitfalls

- Do not interpret “LM Studio is doing nothing” as proof that its HTTP API is healthy; the user may only mean no inference job is running.
- Do not start a large frame-extraction/VLM queue before a one-image request succeeds.
- Do not turn a transient provider challenge into a permanent claim that YouTube or a tool is broken.
- Do not use transcript prose to invent exact Inspector values, axes, hierarchy, or code.