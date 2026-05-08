#!/usr/bin/env bash
set -euo pipefail
python3 -m pytest -q --maxfail=1
python3 - <<'PY'
from src.orchestration import generate_agent_plan
plan = generate_agent_plan()
print(f"agent_count={len(plan)}")
print(f"unique_skills={len(set(p.skill for p in plan))}")
PY
