from pathlib import Path
from src.backtest_cli import read_csv, run_backtest


def test_backtest_cli_pipeline():
    bars = read_csv(Path("data/sample_prices.csv"))
    result = run_backtest(bars, "buy_hold", {})
    assert result.max_drawdown >= 0
