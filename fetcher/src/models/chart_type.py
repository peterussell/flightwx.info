"""Contains a ChartType enum representing types of aeronatical charts."""
from enum import Enum

class ChartType(Enum):
    """Enum representing types of aeronautical charts."""
    SECTIONAL = 1
    TERMINAL_AREA = 2
    HELICOPTER = 3
    GRAND_CANYON = 4
    CARIBBEAN = 5
