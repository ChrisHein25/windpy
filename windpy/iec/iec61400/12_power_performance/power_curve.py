from dataclasses import dataclass
from typing import List, Union


@dataclass
class PowerCurve:
    wind_arr: List[Union[float, int]]
    power_arr: List[Union[float, int]]


