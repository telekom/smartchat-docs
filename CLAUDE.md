# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project

**telekom/smartchat-docs** — public mirror and GitHub Pages host for the SmartChat product documentation, sourced from an internal Deutsche Telekom GitLab repo. The live site is served at `https://docs.smartchat.ai.t-systems.net` from the `gh-pages` branch.

- **Owner:** [`telekom`](https://github.com/telekom) organization (public repository).
- **Upstream source:** `gitlab.devops.telekom.de/ai/genai/ai-foundation-services/smartchat/docs` (private; access via deploy token secrets).
- **License:** Apache License 2.0. No `LICENSE` file is currently committed — if you intend to enforce this, add a standard Apache-2.0 `LICENSE` file at the repo root.

## What this repository is

This repo is a **publishing shell**, not the docs source. The actual SmartChat documentation lives in GitLab at `gitlab.devops.telekom.de/ai/genai/ai-foundation-services/smartchat/docs` (Astro + Bun + d2). This repo's only job is to periodically clone that GitLab source, build it with `BUILD_TARGET=external` to strip internal-only pages, and publish the result to GitHub Pages at `docs.smartchat.ai.t-systems.net`.

There is no local build, test, or lint — the only meaningful change you can make here is to the workflow. Do not try to `bun install` / `bun run build` locally; the source code those commands need is not in this repo.

## Branch layout

- `main` — contains the workflow and a placeholder `index.html`. The placeholder is **not** what users see; GitHub Pages is served from `gh-pages`.
- `gh-pages` — auto-generated, force-pushed by the workflow. Never commit here by hand. Contains the built static site plus two state files:
  - `.source-sha` — commit SHA of the last successfully built `main` branch of the GitLab repo
  - `.source-sha-next` — same, for the optional `next` branch
  - `CNAME` and `.nojekyll` — required for the custom domain and to keep underscore-prefixed directories (Astro output).

## How the sync works (`.github/workflows/sync-docs.yml`)

1. Clones GitLab `main` (always) and `next` (if it exists) using `GITLAB_DEPLOY_TOKEN_USER` + `GITLAB_DEPLOY_TOKEN` secrets via HTTP basic auth.
2. Compares the freshly cloned SHAs against `.source-sha` / `.source-sha-next` fetched from the live `gh-pages` branch via `raw.githubusercontent.com`. If neither has moved and `force` is not set, the job exits without rebuilding.
3. Builds `main` with `BUILD_TARGET=external RELEASE_SCOPE=current`, then (if present) builds `next` with `BUILD_TARGET=external BASE_PATH=/next RELEASE_SCOPE=''` and moves its `dist/` into `source/dist/next`.
4. After each build, `rm -rf dist/internal` — defense in depth in case the build target flag fails to filter something.
5. Force-pushes the combined `source/dist` to `gh-pages` as a fresh single-commit history.

Triggers: cron `0 6,8,10,12,14,16,18 * * 1-5` (hourly-ish during German business hours) and `workflow_dispatch` with a `force` boolean to rebuild even when SHAs match.

## Conventions and gotchas

- **Build output is suppressed** (`> /dev/null 2>&1`) intentionally — earlier versions leaked internal page names into Action logs. Keep it suppressed when editing the build steps.
- **Node 22 + Bun** are both set up because the GitLab project pins Astro 6, which requires Node 22 at install time even though Bun runs the build.
- **d2 v0.7.1** is downloaded directly from the GitHub release; bump the version in two places (URL and extracted directory `d2-v0.7.1`) if upgrading.
- The deploy step builds a brand-new git history (`git init -b gh-pages` → force-push). Don't try to preserve history on `gh-pages`; it will be overwritten on the next run.
- `index.html` on `main` is a placeholder shown only if `gh-pages` is missing or unconfigured. Don't invest effort in styling it.

## Working on this repo

- Workflow changes: edit `.github/workflows/sync-docs.yml`, then test via the Actions tab using **Run workflow → force: true** to trigger a full rebuild end-to-end. There is no way to dry-run locally without the GitLab secrets.
- If the cron stops producing updates, first check whether the SHA-comparison step thinks nothing changed (look at the `Check if source has changed` step output) before assuming a build failure.
