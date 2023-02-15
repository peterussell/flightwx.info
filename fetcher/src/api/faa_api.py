"""
A module for interacting with the faa.gov aeronautical chart API
"""

import api.api as api
from models.geoname import Geoname
import filesystem

__all__ = ["update_charts"]

SECTIONAL_URL = "vfr/sectional"
SECTIONAL_INFO_URL = f"{SECTIONAL_URL}/info"

def _get_sectional_info(geoname: Geoname) -> None:
    api.get(f"{SECTIONAL_INFO_URL}?geoname={geoname.value}")

def _get_sectional_chart(geoname: Geoname) -> None:
    api.get(f"{SECTIONAL_URL}?geoname={geoname.value}")

def update_sectional_charts() -> None:
    print("Updating sectional charts")
    for chart in Geoname:
        if not filesystem.is_chart_current(chart):
            print(f"Update required for chart {chart.value}")
            _get_sectional_chart(chart)
        else:
            print(f"No update required for chart {chart.value}")

def update_terminal_area_charts() -> None:
    """Updates terminal area charts"""
    print("Updating terminal area charts")

def update_gulf_coast_charts() -> None:
    """Updates Gulf Coast charts"""
    print("Updating Gulf Coast charts")

def update_grand_canyon_charts() -> None:
    """Updates Grand Canyon charts"""
    print("Updating Grand Canyon charts")

def update_helicopter_charts() -> None:
    """Updates helicopter charts")"""
    print("Updating helicopter charts")

def update_caribbean_charts() -> None:
    """Updates Caribbean charts")"""
    print("Updating Caribbean charts")

def update_planning_charts() -> None:
    """Updates planning charts")"""
    print("Updating planning charts")

def update_charts() -> None:
    """Updates all chart types"""
    update_sectional_charts()
    update_terminal_area_charts()
    update_gulf_coast_charts()
    update_grand_canyon_charts()
    update_helicopter_charts()
    update_caribbean_charts()
    update_planning_charts()
