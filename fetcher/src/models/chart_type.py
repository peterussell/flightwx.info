"""Contains a ChartType enum representing types of aeronatical charts."""
from enum import Enum

class ChartType(Enum):
    """Enum representing types of aeronautical charts."""
    SECTIONAL = "sectional"
    TERMINAL_AREA = "tac"
    HELICOPTER = "helicopter"
    GRAND_CANYON = "grandcanyon"
