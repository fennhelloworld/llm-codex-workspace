"""Simplified SLAM data-fusion pipeline skeleton for documentation-to-code traceability."""
from dataclasses import dataclass
from typing import List, Tuple


Point3D = Tuple[float, float, float]


@dataclass
class FramePacket:
    lidar_points: List[Point3D]
    imu_accel: Tuple[float, float, float]
    gps_llh: Tuple[float, float, float]
    timestamp_ms: int


@dataclass
class PoseEstimate:
    x: float
    y: float
    z: float
    yaw: float


def preprocess_points(points: List[Point3D], z_clip: float = 3.0) -> List[Point3D]:
    return [p for p in points if -z_clip <= p[2] <= z_clip]


def front_end_odometry(prev: PoseEstimate, packet: FramePacket) -> PoseEstimate:
    ax, ay, _ = packet.imu_accel
    return PoseEstimate(prev.x + ax * 0.01, prev.y + ay * 0.01, prev.z, prev.yaw)


def back_end_optimize(traj: List[PoseEstimate]) -> List[PoseEstimate]:
    if not traj:
        return traj
    # tiny smoother
    out = [traj[0]]
    for i in range(1, len(traj)):
        p0, p1 = out[-1], traj[i]
        out.append(PoseEstimate((p0.x + p1.x) / 2, (p0.y + p1.y) / 2, p1.z, p1.yaw))
    return out
