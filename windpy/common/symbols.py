"""
Classes to understand symbols used in engineering calculations.
"""

from dataclasses import dataclass
from typing import List, Optional
from pint import Unit


@dataclass
class Symbol:
    """
    Symbols have a description and units
    """
    symbol: str  # the literal closest string representation to the real math symbol in Python
    unit: Unit
    description: Optional[str] = "No description provided."



class SymbolCollection:
    def __init__(self, standard_number: StandardNumber ):
        self.symbols: List[Symbol] = []

    def add_symbol(self, symbol: Symbol):
        self.symbols.append(symbol)

    def get_symbols(self) -> List[Symbol]:
        return self.symbols

