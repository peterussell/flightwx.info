from filesystem.filesystem import Filesystem
from models.chart_edition import ChartEdition
from models.chart_type import ChartType
from models.geoname import Geoname
from services.faa_service import FAAService


class ChartService:
    def __init__(self, filesystem: Filesystem, faa_service: FAAService) -> None:
        self.filesystem = filesystem
        self.faa_service = faa_service

    def update_sectional_charts(self) -> None:
        """
        Checks charts on the filesystem against current versions specified by the
        FAA API, and updates any that aren't current
        """
        # tmp - test with single chart 
        # for chart_name in Geoname: # tmp - uncomment when working
        chart_name = Geoname.CHICAGO
    
        # Check whether the chart needs an update (can we do this without making an API call?)
        ce: ChartEdition = self.faa_service.get_vfr_chart_edition(ChartType.SECTIONAL, chart_name)

        if not self.filesystem.is_saved_chart_current(ce):
            print(f"{chart_name.value}\t\tUPDATE REQUIRED")
            self.faa_service.update_chart(ce)

        else:
            print(f"{chart_name.value}\t\tCurrent")
