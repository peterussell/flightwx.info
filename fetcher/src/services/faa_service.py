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

        res: Response = api.get(url)

        if (res.status_code != 200):
            err_msg = f"Failed to fetch {chart_type.value} chart edition for {geoname.value} "
            err_msg += f"(response code: {res.status_code}, request URL: {url})"
            raise RuntimeError(err_msg)

        return map_chart_edition(res)


    # TODO: tests
    def is_chart_current(self, saved_chart: ChartEdition, api_chart: ChartEdition) -> bool:
        if saved_chart is None:
            return False

        return saved_chart.edition_number >= api_chart.edition_number


    def download_chart(self, chart_edition: ChartEdition) -> str:
        """
        Downloads the chart file for chart_edition and saves to the filesystem
        """
        path = self.filesystem.get_chart_path(chart_edition)

        print(f"Downloading {chart_edition.product_url} to {path}")
        api.download_file(chart_edition.product_url, path)


    def _get_vfr_chart_edition_url(self, chart_type: ChartType, geoname: Geoname) -> str:
        return f"vfr/{chart_type.value}/chart?geoname={geoname.value}&edition=current&format=tiff"
