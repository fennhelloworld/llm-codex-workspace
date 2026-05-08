from __future__ import annotations
from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Dict


@dataclass
class MarketRow:
    close: float


class Strategy(ABC):
    name: str = "base"

    @abstractmethod
    def on_bar(self, row: MarketRow) -> int:
        """Return target position in {-1,0,1}."""


class MovingAverageCrossStrategy(Strategy):
    name = "ma_cross"

    def __init__(self, short: int = 5, long: int = 20):
        self.short = short
        self.long = long
        self.prices: list[float] = []

    def on_bar(self, row: MarketRow) -> int:
        self.prices.append(row.close)
        if len(self.prices) < self.long:
            return 0
        s = sum(self.prices[-self.short:]) / self.short
        l = sum(self.prices[-self.long:]) / self.long
        return 1 if s > l else -1


class BuyHoldStrategy(Strategy):
    name = "buy_hold"

    def on_bar(self, row: MarketRow) -> int:
        return 1


def build_strategy(name: str, params: Dict[str, str]) -> Strategy:
    if name == "ma_cross":
        return MovingAverageCrossStrategy(
            short=int(params.get("short", 5)),
            long=int(params.get("long", 20)),
        )
    if name == "buy_hold":
        return BuyHoldStrategy()
    raise ValueError(f"Unknown strategy: {name}")
