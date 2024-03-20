import os
import glob

from filesystem.filesystem import Filesystem
from models.chart_edition import ChartEdition

class LocalFilesystem(Filesystem):
    RASTERS_BASE_PATH = "../charts/tiff"
    MBTILES_BASE_PATH = "../charts/mbtiles"

    # TODO: tests
    def get_local_chart_edition(self, remote_chart_edition: ChartEdition) -> ChartEdition | None:
        filename = remote_chart_edition.get_raster_path(LocalFilesystem.RASTERS_BASE_PATH)

        # Perform a fuzzy search for any local charts matching the chart prefix.
        chart_prefix = remote_chart_edition.get_filename_prefix()
        search_str = f"{LocalFilesystem.RASTERS_BASE_PATH}/{chart_prefix}*.zip"
        matching_charts = glob.glob(search_str)

        if len(matching_charts) == 0:
            # 0 charts found
            return None

        if len(matching_charts) > 1:
            # >1 chart found, uh oh...
            raise RuntimeError(f"More than one saved chart found for prefix {chart_prefix}. Bailing.")

        # One chart found, return it
        filename = matching_charts[0]
        return ChartEdition.from_filename(LocalFilesystem.RASTERS_BASE_PATH, filename)


    def delete_raster(self, chart_edition: ChartEdition) -> None:
        filename = chart_edition.get_raster_path(LocalFilesystem.RASTERS_BASE_PATH)

        try:
            os.remove(filename)
        except OSError as e:
            print(f"Failed to delete old chart at {e.filename} - {e.strerror}.")


    def get_raster_path(self, chart_edition: ChartEdition) -> str:
        return chart_edition.get_raster_path(LocalFilesystem.RASTERS_BASE_PATH)


    def get_mbtiles_path(self, chart_edition: ChartEdition) -> str:
        return chart_edition.get_mbtiles_path(LocalFilesystem.MBTILES_BASE_PATH)
