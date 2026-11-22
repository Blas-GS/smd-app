"""The data the app works with."""

from dataclasses import dataclass
from datetime import date
from decimal import Decimal


@dataclass(frozen=True)
class Transaction:
    date: date
    account: str
    description: str
    category: str
    amount: Decimal
