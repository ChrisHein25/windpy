"""
Track all classes for dealing with engineering standards
"""
from dataclasses import dataclass
from typing import List, Union, Optional

# import latest IEC libraries
import windpy.iec.iec_61400.part_12_1.ed3 as iec_61400_12_1_ed3_lib
import windpy.iec.iec_61400.part_12_3.ed1 as iec_61400_12_3_ed1_lib
import windpy.iec.iec_61400.part_12_5.ed1 as iec_61400_12_5_ed1_lib


@dataclass
class Organization:
    """
    An Organization creates engineering Standards (IEC, AMCE, etc)
    """
    name: str


@dataclass
class StandardPartNumber:
    major: int  # like 12
    minor: Optional[int] = None  # like 1, 3, 5

    @property
    def __str__(self):
        if self.minor is None:
            return str(self.major)
        else:
            return f"{self.major}-{self.minor}"


@dataclass
class StandardPart:
    number: StandardPartNumber
    name: str
    edition: int
    library: any  # the python library corresponding to this section
    description: Optional[str] = ""


@dataclass
class Standard:
    organization: Organization  # like "IEC"
    number: Union[int, str]  # like "iec_61400"
    parts: List[StandardPart]
    name: str


# define IEC iec_61400 standard with latest editions for each section
iec_61400 = Standard(
    organization=Organization(name='IEC'),
    number=61400,
    name="Wind energy generation systems",
    parts=[
        StandardPart(number=StandardPartNumber(major=12, minor=1), edition=3,
                     name="Power performance measurements of electricity producing wind turbines",
                     library=iec_61400_12_1_ed3_lib),
        StandardPart(number=StandardPartNumber(major=12, minor=3), edition=1,
                     name="Power performance - Measurement based site calibration",
                     library=iec_61400_12_3_ed1_lib),
        StandardPart(number=StandardPartNumber(major=12, minor=5), edition=1,
                     name="Power performance - Assessment of obstacles and terrain",
                     library=iec_61400_12_5_ed1_lib)
    ]
)


