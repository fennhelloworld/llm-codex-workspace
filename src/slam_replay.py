from __future__ import annotations
import csv
from dataclasses import dataclass
from pathlib import Path
from typing import List

from src.slam_pipeline import FramePacket, PoseEstimate, preprocess_points, front_end_odometry, back_end_optimize


@dataclass
class ReplayResult:
    frames: int
    optimized_poses: int


def load_packets(csv_path: Path) -> List[FramePacket]:
    packets: List[FramePacket] = []
    with csv_path.open("r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for r in reader:
            lidar = [(float(r["x"]), float(r["y"]), float(r["z"]))]
            packets.append(
                FramePacket(
                    lidar_points=lidar,
                    imu_accel=(float(r["ax"]), float(r["ay"]), float(r["az"])),
                    gps_llh=(float(r["lat"]), float(r["lon"]), float(r["h"])),
                    timestamp_ms=int(r["ts"]),
                )
            )
    return packets


def replay(csv_path: Path) -> ReplayResult:
    packets = load_packets(csv_path)
    pose = PoseEstimate(0, 0, 0, 0)
    traj: List[PoseEstimate] = [pose]
    for p in packets:
        _ = preprocess_points(p.lidar_points)
        pose = front_end_odometry(pose, p)
        traj.append(pose)
    opt = back_end_optimize(traj)
    return ReplayResult(frames=len(packets), optimized_poses=len(opt))
