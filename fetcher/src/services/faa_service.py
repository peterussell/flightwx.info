"""
A module for interacting with the faa.gov aeronautical chart API
"""
from requests import Response

import api.api as api
from filesystem.filesystem import Filesystem
from mappers.chart_edition import map_chart_edition
from models.chart_edition import ChartEdition
from models.chart_type import ChartType
from models.geoname import Geoname

class FAAService:
    """A service for interacting with the FAA chart API"""

    def __init__(self, filesystem: Filesystem):
        self.filesystem = filesystem


    def get_vfr_chart_edition(self, chart_type: ChartType, geoname: Geoname) -> ChartEdition | None:
        """
        Gets the chart edition metadata for a VFR chart for the specified chart
        type and geoname.
        """
        url = self._get_vfr_chart_edition_url(chart_type, geoname)

        res: Response = api.get(url) # TODO: is there a type from responses

        if (res.status_code != 200):
            err_msg = f"Failed to fetch {chart_type.value} chart edition for {geoname.value} "
            err_msg += f"(response code: {res.status}, request URL: {url})"
            raise RuntimeError(err_msg)

        return map_chart_edition(res)


    def is_chart_current(self, saved_chart: ChartEdition, api_chart: ChartEdition) -> bool:
        return saved_chart.edition_number >= api_chart.edition_number

    def update_chart(self, chart_edition: ChartEdition) -> str:
        """
        Downloads the chart file for chart_edition and saves to the filesystem
        """
        filename = self.filesystem.get_filename(chart_edition)
        api.download_file(chart_edition.product_url, filename)

        # TODO -- working here (2):
        # Delete the old chart file (if one was found)


    def _get_vfr_chart_edition_url(self, chart_type: ChartType, geoname: Geoname) -> str:
        return f"vfr/{chart_type.value}/chart?geoname={geoname.value}&edition=current&format=tiff"








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
