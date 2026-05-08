from dataclasses import dataclass
from typing import List


@dataclass
class AgentTask:
    agent_id: int
    skill: str
    workload: str


def generate_agent_plan(agent_count: int = 500, skills: List[str] | None = None) -> List[AgentTask]:
    if skills is None:
        skills = [
            "stock-analysis", "hot-scanner", "financial-report-analysis", "market-sentiment",
            "backtest-tool", "finance-data", "auto-trading", "risk-calculator", "slam-sim", "research"
        ]
    plan: List[AgentTask] = []
    for i in range(agent_count):
        skill = skills[i % len(skills)]
        plan.append(AgentTask(agent_id=i + 1, skill=skill, workload=f"workstream-{i % 20 + 1}"))
    return plan
