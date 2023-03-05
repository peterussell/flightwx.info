from models.chart_edition import ChartEdition

from filesystem.filesystem import Filesystem

class S3Filesystem(Filesystem):
    def get_saved_chart_edition(self, api_chart_edition: ChartEdition) -> ChartEdition | None:
        pass


    def delete_chart(self, chart_edition: ChartEdition) -> None:
        pass


    def get_chart_path(self, chart_edition: ChartEdition) -> str:
        pass
