"""An application to fetch and parse FAA aeronuatical charts"""
from filesystem.local_filesystem import LocalFilesystem
from services.chart_service import ChartService
from services.faa_service import FAAService

if __name__ == "__main__":
    fs = LocalFilesystem()
    faa = FAAService(fs)
    cs = ChartService(fs, faa)

    cs.update_sectional_charts()
