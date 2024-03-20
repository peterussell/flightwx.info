from filesystem.filesystem import Filesystem
from models.chart_edition import ChartEdition
from models.chart_type import ChartType
from models.geoname import Geoname
from services.faa_service import FAAService

class ChartService:
    def __init__(self, filesystem: Filesystem, faa_service: FAAService) -> None:
        self.filesystem = filesystem
        self.faa_service = faa_service


    def update_sectional_charts(self) -> list[str]:
        """
        Checks charts on the filesystem against current versions specified by the
        FAA API, and updates any that aren't current.

        Returns a list containing ChartEditions for any updated charts.
        """

        updated_charts: list[str] = []

        # tmp - test with single chart
        # for chart_name in Geoname: # tmp - uncomment when working
        chart_name = Geoname.DUTCH_HARBOR

        # Check whether the chart needs an update (can we do this without making an API call?)
        remote_chart: ChartEdition = self.faa_service.get_vfr_chart_edition(ChartType.SECTIONAL, chart_name)
        saved_chart = self.filesystem.get_local_chart_edition(remote_chart)

        update_required = not self.faa_service.is_chart_current(saved_chart, remote_chart)

        if update_required:
            print(f"{chart_name.value}: update required")
            self._do_update(remote_chart)
            self._delete_if_exists(saved_chart)
            updated_charts.append(remote_chart)

        else:
            print(f"{chart_name.value}: current")

        return updated_charts


    def _do_update(self, remote_chart: ChartEdition) -> None:
        print(f"Updating chart {remote_chart.geoname.value}")
        self.faa_service.download_chart(remote_chart)


    def _delete_if_exists(self, saved_chart: ChartEdition) -> None:
        if saved_chart is not None:
            print(f"Deleting old chart {saved_chart.geoname.value} v{saved_chart.edition_number}")
            self.filesystem.delete_raster(saved_chart)
