# Fenn × 萌宝宝：全栈执行系统（7任务 + 500 Agents + 可运行算法骨架）

本仓库已从“计划文档”升级为“可运行系统骨架”，覆盖：
- 7任务日程编排与执行；
- 500 agent + skills 调度规划；
- 真实行情CSV回测CLI；
- 可插拔策略接口；
- SLAM仿真回放器；
- 单元测试与自动化报告脚本。

## 快速开始

```bash
python3 src/main.py
python3 -m src.backtest_cli --csv data/sample_prices.csv --strategy ma_cross --param short=2 --param long=3
python3 -m pytest -q
./scripts/test_and_report.sh
```

## 目录
- `src/main.py`：7任务编排器
- `src/orchestration.py`：500 agents 调度计划
- `src/backtest_cli.py`：行情回测CLI
- `src/strategy.py`：策略插件接口与内置策略
- `src/quant.py`：评估指标
- `src/slam_pipeline.py`：SLAM基础链路
- `src/slam_replay.py`：SLAM仿真数据回放
- `docs/SYSTEM_DESIGN.md`：架构与论证
- `docs/ARCHITECTURE.md`、`docs/WORKFLOW.md`：架构与流程图
- `tests/`：单元测试

## 系统目标
1. 明确战略任务到工程落地的映射。
2. 保证代码可运行、可测试、可复盘。
3. 支持后续替换为生产级数据源、执行网关和控制器。
