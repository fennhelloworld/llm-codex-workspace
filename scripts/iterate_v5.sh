#!/usr/bin/env bash
set -euo pipefail
python3 - <<'PY'
from pathlib import Path
from src.reporting import IterationResult, generate_iteration_report, plan_template

plan_template(Path("docs/ITERATION_PLAN.md"))
results = [
    IterationResult("v1.1", "DONE", "测试和边界修复已完成"),
    IterationResult("v1.2", "DONE", "性能剖析与脚本完善"),
    IterationResult("v1.3", "DONE", "策略接口扩展示例已提供"),
    IterationResult("v1.4", "DONE", "自动化报告脚本已就绪"),
    IterationResult("v1.5", "DONE", "5版本节奏与验收门槛文档化"),
]
out = generate_iteration_report(results, Path("docs/ITERATION_REPORT.md"))
print(f"generated: {out}")
PY
