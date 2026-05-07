from __future__ import annotations
import argparse
import csv
from dataclasses import dataclass
from pathlib import Path
from typing import List

from src.quant import evaluate
from src.strategy import build_strategy, MarketRow


@dataclass
class Bar:
    date: str
    close: float


def read_csv(path: Path) -> List[Bar]:
    bars: List[Bar] = []
    with path.open("r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for r in reader:
            bars.append(Bar(date=r["Date"], close=float(r["Close"])))
    return bars


def run_backtest(bars: List[Bar], strategy_name: str, params: dict[str, str]):
    st = build_strategy(strategy_name, params)
    equity = [1.0]
    returns: List[float] = []
    prev_close = bars[0].close
    pos = 0
    for b in bars[1:]:
        pos = st.on_bar(MarketRow(close=b.close))
        r = ((b.close / prev_close) - 1.0) * pos
        returns.append(r)
        equity.append(equity[-1] * (1 + r))
        prev_close = b.close
    return evaluate(equity, returns)


def main() -> None:
    ap = argparse.ArgumentParser(description="Real-market-data backtest CLI (CSV Date,Close)")
    ap.add_argument("--csv", required=True)
    ap.add_argument("--strategy", default="ma_cross")
    ap.add_argument("--param", action="append", default=[])
    args = ap.parse_args()

    params: dict[str, str] = {}
    for p in args.param:
        k, v = p.split("=", 1)
        params[k] = v

    bars = read_csv(Path(args.csv))
    result = run_backtest(bars, args.strategy, params)
    print(f"annual_return={result.annual_return:.6f}")
    print(f"max_drawdown={result.max_drawdown:.6f}")
    print(f"sharpe={result.sharpe:.6f}")
    print(f"calmar={result.calmar:.6f}")


if __name__ == "__main__":
    main()
