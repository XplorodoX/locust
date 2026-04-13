# 001 — Onboarding and Exploration

**Date**: 2026-04-13
**Tool**: GitHub Copilot
**Model**: GPT-5.3-Codex
**Iterations**: 8

## Prompt

**2026-04-13 10:00**

I ran locust and opened localhost:8089, but I see a raw/broken page instead of the dashboard. How do I fix this?

**2026-04-13 10:04**

What is the high-level architecture of this project?

**2026-04-13 10:12**

Create your team’s feature branch, create your diary subfolder, add 001-onboarding.md from template, and commit with:
git commit -m "[diary] 001 — Onboarding and exploration"

**2026-04-13 10:14**

Push den branch / mach das mit einem forken.

## What I Learned

- Key architectural insights:
	- Locust startup path is `main.py -> Environment -> Runner -> Users` with event-driven stats collection.
	- Web UI is Flask backend (`locust/web.py`) + React frontend (`locust/webui`) served from built assets.
	- Request flow is task -> client call -> `events.request` -> `RequestStats` -> `/api/stats` for UI.
- What the AI got right vs wrong:
	- Correctly identified missing `locust/webui/dist` as root cause of broken raw page.
	- Correctly handled missing Yarn by setting up Corepack/Yarn and building frontend in `locust/webui`.
	- Correctly diagnosed that missing GitHub visibility was due to branch not being pushable to upstream (`403`).
- Setup issues encountered and how they were solved:
	- `localhost:8089` looked broken because frontend build artifacts were missing. Solved with `cd locust/webui && yarn install && yarn build`.
	- `yarn` command was missing. Solved by installing/enabling Corepack and activating Yarn 4.12.0.
	- Push to upstream failed (`Permission denied`). Solved by pushing branch to personal fork (`XplorodoX/locust`) and setting upstream to `fork/feature/team22-stats-coverage`.
