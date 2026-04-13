# 003 - Add exception handler coverage

**Date**: 2026-04-13
**Tool**: GitHub Copilot
**Model**: GPT-5.3-Codex
**Iterations**: 1

## Prompt

**2026-04-13**

```text
=============================================== tests coverage ===============================================
______________________________ coverage: platform win32, python 3.12.3-final-0 _______________________________

Name                               Stmts   Miss Branch BrPart  Cover   Missing
------------------------------------------------------------------------------
locust\util\__init__.py                0      0      0      0   100%
locust\util\cache.py                  22     19      8      0    10%   12-35
locust\util\date.py                   14     10      0      0    29%   5, 9, 13-23
locust\util\deprecation.py            21      4      6      2    70%   11-13, 26
locust\util\directory.py               3      1      0      0    67%   5
locust\util\exception_handler.py      20     12      4      0    33%   10-22
locust\util\load_locustfile.py        73     37     24      5    42%   51-57, 62, 66-67, 74->77, 78-79, 99-136
locust\util\rounding.py                2      0      0      0   100%
locust\util\timespan.py               15      1      8      1    91%   20
locust\util\url.py                     9      3      2      1    64%   11, 14-15
------------------------------------------------------------------------------
TOTAL                                179     87     52      9    46%
11 passed in 19.38s

I am currently doing coverage testing and wnat to get more coverage, pls fix in the file: locust\util\exception_handler.py the coverage so that i get 100%.
```
