from models.chart_edition import ChartEdition
from models.geoname import Geoname

from filesystem.filesystem import Filesystem

class S3Filesystem(Filesystem):
    def chart_exists(self, edition: ChartEdition) -> bool:
        pass


    def delete_chart(self, chart_edition: ChartEdition) -> None:
        pass


    def get_chart_meta(self, chart_name: Geoname) -> bool:
        pass
