"""An application to fetch and parse FAA aeronuatical charts"""
from filesystem.filesystem import Filesystem
from filesystem.local_filesystem import LocalFilesystem
from models.chart_edition import ChartEdition
from services.chart_service import ChartService
from services.faa_service import FAAService
from utils.gdal import generate_mbtiles

def init() -> None:
    global filesystem, faa_service, chart_service
    filesystem = LocalFilesystem()
    faa_service = FAAService(filesystem)
    chart_service = ChartService(filesystem, faa_service)


def fetch_charts() -> list[ChartEdition]:
    return chart_service.update_sectional_charts()


def process_charts(charts: list[ChartEdition]) -> None:
    # TODO: need an unzip step here

    for chart in charts:
        generate_mbtiles(
            filesystem.get_raster_path(chart),
            filesystem.get_mbtiles_path(chart))

if __name__ == "__main__":
    init()
    updated: list[ChartEdition] = fetch_charts()
    process_charts(updated)
