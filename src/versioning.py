from dataclasses import dataclass
from typing import List


@dataclass
class ReleaseSpec:
    version: str
    focus: str
    changes: List[str]
    test_gate: str


def build_five_releases() -> List[ReleaseSpec]:
    return [
        ReleaseSpec("v1.1", "稳定性", ["补齐单元测试", "统一CLI参数", "修复边界输入"], "pytest全绿"),
        ReleaseSpec("v1.2", "性能", ["回测向量化", "SLAM回放批处理", "报告缓存"], "回测耗时下降>=20%"),
        ReleaseSpec("v1.3", "功能", ["新增RSI策略插件", "新增止损规则", "新增多标的批量回测"], "新增功能测试通过"),
        ReleaseSpec("v1.4", "工程化", ["覆盖率报告", "质量门禁脚本", "结构化日志"], "coverage>=85%"),
        ReleaseSpec("v1.5", "可运营", ["周报自动生成", "500 agent负载审计", "风险暴露汇总"], "日报周报可自动生成"),
    ]
