from windpy.common.symbols import Symbol, SymbolCollection
from pint import UnitRegistry

# Create a Unit Registry
ureg = UnitRegistry()


symbols = SymbolCollection(standard_number=61400, section=12, edition=2.0)
symbols.add_symbol(Symbol(symbol='A', unit=ureg.meter ** 2,
                                       description='Swept area of the wind turbine rotor'))

