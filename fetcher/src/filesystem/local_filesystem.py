import os.path

from filesystem.filesystem import Filesystem
from models.chart_edition import ChartEdition

class LocalFilesystem(Filesystem):
    base_path = "../charts"

    def chart_exists(self, edition: ChartEdition) -> bool:
        filename = super().get_filename(edition)
        return os.path.isfile(f"{self.base_path}/{filename}")
    
    def save_chart(self, edition: ChartEdition) -> None:
        pass
        # tmp

    def is_chart_current(self, chart_edition: ChartEdition) -> bool:
        # tmp - just update the Chicago chart
        filename = super.get_filename(chart_edition)
        print(f"filename for {chart_edition.geoname.value}: {filename}")
