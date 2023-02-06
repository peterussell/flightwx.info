"""
Contains a ChartUpdateSet class representing updates for charts of a single
type.
"""

class ChartUpdateSet:
    """
    Represents an set of updates for all charts of a single type on a specified
    date.
    """
    def __init__(self, update_date, chart_type):
        self.update_date = update_date
        self.chart_type = chart_type
