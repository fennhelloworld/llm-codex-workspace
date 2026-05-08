from __future__ import annotations
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable

from src.versioning import build_five_releases


@dataclass
class IterationResult:
    version: str
    status: str
    notes: str


def generate_iteration_report(results: Iterable[IterationResult], out: Path) -> Path:
    lines = ["# 5次版本迭代报告", "", "| Version | Status | Notes |", "|---|---|---|"]
    for r in results:
        lines.append(f"| {r.version} | {r.status} | {r.notes} |")
    out.write_text("\n".join(lines), encoding="utf-8")
    return out


def plan_template(out: Path) -> Path:
    rel = build_five_releases()
    lines = ["# 到明天前的5次版本计划", ""]
    for r in rel:
        lines.append(f"## {r.version} - {r.focus}")
        for c in r.changes:
            lines.append(f"- [ ] {c}")
        lines.append(f"- 验收门槛：{r.test_gate}")
        lines.append("")
    out.write_text("\n".join(lines), encoding="utf-8")
    return out
