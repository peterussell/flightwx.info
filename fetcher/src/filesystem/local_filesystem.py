import os.path
import glob

from filesystem.filesystem import Filesystem
from models.chart_edition import ChartEdition

class LocalFilesystem(Filesystem):
    CHARTS_BASE_PATH = "../charts"

    # TODO: tests
    def get_saved_chart_edition(self, api_chart_edition: ChartEdition) -> ChartEdition | None:
        """
        Returns a value indicating whether the API chart is newer than the saved chart,
        or False if no saved chart was found.
        """
        filename = super()._get_filename(LocalFilesystem.CHARTS_BASE_PATH, api_chart_edition)

        chart_prefix = api_chart_edition.get_filename_prefix()
        search_str = f"{LocalFilesystem.CHARTS_BASE_PATH}/{chart_prefix}*.zip"
        matching_charts = glob.glob(search_str.lower())

        if len(matching_charts) == 0:
            # No charts found for this product and geoname, so return 'not current'
            return None

        if len(matching_charts) > 1:
            # More than one chart found, uh oh...
            raise RuntimeError(f"More than one saved chart found for prefix {chart_prefix}. Bailing.")

        # One chart found, now we just need to check the version
        filename = matching_charts[0]
        return super()._get_edition_from_filename(LocalFilesystem.CHARTS_BASE_PATH, filename)


    def get_filename(self, chart_edition: ChartEdition) -> str:
        return super()._get_filename(LocalFilesystem.CHARTS_BASE_PATH, chart_edition)
