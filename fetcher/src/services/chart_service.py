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
        api_chart: ChartEdition = self.faa_service.get_vfr_chart_edition(ChartType.SECTIONAL, chart_name)
        saved_chart = self.filesystem.get_saved_chart_edition(api_chart)

        if not self.faa_service.is_chart_current(saved_chart, api_chart):
            print(f"{chart_name.value}\t\tUPDATE REQUIRED")
            self.faa_service.update_chart(api_chart)

        else:
            print(f"{chart_name.value}\t\tCurrent")
