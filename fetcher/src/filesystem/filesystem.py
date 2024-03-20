from abc import ABC, abstractmethod

from models.chart_edition import ChartEdition
from models.geoname import Geoname

class Filesystem(ABC):
    @abstractmethod
    def get_local_chart_edition(self, remote_chart_edition: ChartEdition) -> ChartEdition | None:
        """
        Returns the local chart edition matching the given remote_chart_edition, or 
        or None if no saved chart was found. Throws a RuntimeError if more than one
        chart matching this chart_edition's prefix was found.
        """
        pass


    @abstractmethod
    def delete_raster(self, chart_edition: ChartEdition) -> None:
        """Deletes the chart file associated with this chart_edition."""
        pass


    @abstractmethod
    def get_raster_path(self, chart_edition: ChartEdition) -> str:
        """Gets the raster file path associated with this chart_edition."""
        pass
    

    @abstractmethod
    def get_mbtiles_path(self, chart_edition: ChartEdition) -> str:
        """Gets the mbtiles file path associated with this chart_edition."""
        pass


    # TODO: tests
    def _is_chart_current(self, saved_edition: ChartEdition, api_edition: ChartEdition) -> bool:
        return saved_edition.edition_number >= api_edition.edition_number
