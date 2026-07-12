from dataclasses import dataclass
from datetime import date


@dataclass
class Dive:
    dive_number: int
    date: date
    location: str
    max_depth: float
    dive_time: int
    buddy: str