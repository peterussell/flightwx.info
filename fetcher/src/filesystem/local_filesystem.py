import os
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
        filename = api_chart_edition.get_chart_path(LocalFilesystem.CHARTS_BASE_PATH)

        chart_prefix = api_chart_edition.get_filename_prefix()
        search_str = f"{LocalFilesystem.CHARTS_BASE_PATH}/{chart_prefix}*.zip"
        matching_charts = glob.glob(search_str)

        if len(matching_charts) == 0:
            # 0 charts found
            return None

        if len(matching_charts) > 1:
            # >1 chart found, uh oh...
            raise RuntimeError(f"More than one saved chart found for prefix {chart_prefix}. Bailing.")

        # One chart found, return it
        filename = matching_charts[0]
        return ChartEdition.from_filename(LocalFilesystem.CHARTS_BASE_PATH, filename)


    def delete_chart(self, chart_edition: ChartEdition) -> None:
        """Deletes the chart file associated with this chart_edition."""
        filename = chart_edition.get_chart_path(LocalFilesystem.CHARTS_BASE_PATH)

        try:
            os.remove(filename)
        except OSError as e:
            print(f"Failed to delete old chart at {e.filename} - {e.strerror}.")


    def get_chart_path(self, chart_edition: ChartEdition) -> str:
        """Gets the path to the chart associated with this chart_edition."""
        return chart_edition.get_chart_path(LocalFilesystem.CHARTS_BASE_PATH)
