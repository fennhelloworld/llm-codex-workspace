from pathlib import Path
from src.slam_replay import replay


def test_replay():
    res = replay(Path("data/sample_slam.csv"))
    assert res.frames == 3
    assert res.optimized_poses >= 1
