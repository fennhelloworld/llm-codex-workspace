from src.quant import max_drawdown, sharpe_ratio, evaluate


def test_metrics():
    eq = [1.0, 1.1, 1.0, 1.2]
    rets = [0.1, -0.0909, 0.2]
    assert max_drawdown(eq) > 0
    assert sharpe_ratio(rets) != 0
    result = evaluate(eq, rets)
    assert result.max_drawdown >= 0
