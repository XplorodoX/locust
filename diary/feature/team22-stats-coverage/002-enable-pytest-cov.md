# 002 — Enable pytest-cov for test commands

**Date**: 2026-04-13
**Tool**: GitHub Copilot
**Model**: GPT-5.4 mini
**Iterations**: 2

## Prompt

**2026-04-13 00:00**

The `uv run pytest ... --cov=...` command fails with `unrecognized arguments` because `pytest-cov` is not installed. Please fix the project configuration so the coverage flags work in the test environment.

**2026-04-13 00:00**

Verified the test environment with:

`uv run pytest locust/test/test_stats.py locust/test/test_html_filename.py --cov=locust/stats --cov=locust/html --cov-report=term-missing -q`

The tests passed, and `pytest-cov` is available now. The remaining coverage warnings are caused by the slash-separated module names in the command, which coverage does not recognize as importable module paths.