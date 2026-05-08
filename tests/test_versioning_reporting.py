from pathlib import Path
from src.versioning import build_five_releases
from src.reporting import plan_template, generate_iteration_report, IterationResult


def test_five_versions_defined():
    rel = build_five_releases()
    assert len(rel) == 5
    assert rel[0].version == "v1.1"
    assert rel[-1].version == "v1.5"


def test_reporting_files(tmp_path: Path):
    plan = plan_template(tmp_path / "plan.md")
    assert plan.exists()
    report = generate_iteration_report([
        IterationResult("v1.1", "DONE", "ok"),
        IterationResult("v1.2", "DONE", "ok"),
    ], tmp_path / "report.md")
    assert report.exists()
