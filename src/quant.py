"""Minimal quant research utilities (educational use)."""
from dataclasses import dataclass
from typing import List
import statistics


@dataclass
class BacktestResult:
    annual_return: float
    max_drawdown: float
    sharpe: float
    calmar: float


def max_drawdown(equity_curve: List[float]) -> float:
    peak = equity_curve[0]
    mdd = 0.0
    for x in equity_curve:
        peak = max(peak, x)
        dd = (peak - x) / peak if peak else 0.0
        mdd = max(mdd, dd)
    return mdd


def sharpe_ratio(returns: List[float], rf: float = 0.0) -> float:
    if len(returns) < 2:
        return 0.0
    excess = [r - rf for r in returns]
    std = statistics.pstdev(excess)
    if std == 0:
        return 0.0
    return statistics.mean(excess) / std


def evaluate(equity_curve: List[float], daily_returns: List[float]) -> BacktestResult:
    total_return = equity_curve[-1] / equity_curve[0] - 1
    annual_return = (1 + total_return) ** (252 / max(len(daily_returns), 1)) - 1
    mdd = max_drawdown(equity_curve)
    sharpe = sharpe_ratio(daily_returns)
    calmar = annual_return / mdd if mdd > 0 else 0.0
    return BacktestResult(annual_return, mdd, sharpe, calmar)
