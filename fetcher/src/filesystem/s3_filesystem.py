from models.chart_edition import ChartEdition

from filesystem.filesystem import Filesystem

class S3Filesystem(Filesystem):
    def get_local_chart_edition(self, remote_chart_edition: ChartEdition) -> ChartEdition | None:
        raise NotImplementedError


    def delete_raster(self, chart_edition: ChartEdition) -> None:
        raise NotImplementedError


    def get_raster_path(self, chart_edition: ChartEdition) -> str:
        raise NotImplementedError


    def get_mbtiles_path(self, chart_edition: ChartEdition) -> str:
        raise NotImplementedError
