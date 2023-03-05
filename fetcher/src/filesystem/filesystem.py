from abc import ABC, abstractmethod

from models.chart_edition import ChartEdition
from models.geoname import Geoname

class Filesystem(ABC):
    @abstractmethod
    def get_saved_chart_edition(self, chart_name: Geoname) -> ChartEdition | None:
        pass


    @abstractmethod
    def delete_chart(self, chart_edition: ChartEdition) -> None:
        pass


    @abstractmethod
    def get_chart_path(self, edition: ChartEdition) -> str:
        pass


    # TODO: tests
    def _is_chart_current(self, saved_edition: ChartEdition, api_edition: ChartEdition) -> bool:
        return saved_edition.edition_number >= api_edition.edition_number
