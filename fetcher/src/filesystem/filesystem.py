from abc import ABC, abstractmethod
from datetime import datetime

from models.chart_edition import ChartEdition
from models.geoname import Geoname

class Filesystem:
    @abstractmethod
    def chart_exists(self, edition: ChartEdition) -> bool:
        pass

    @abstractmethod
    def get_chart_meta(self, chart_name: Geoname) -> bool:
        pass
    
    @abstractmethod
    def is_chart_current(self, chart_name: Geoname) -> bool:
        pass

    # TODO: tests
    def get_filename(self, edition: ChartEdition) -> str:
        """Returns a filename for a given chart edition"""
        parts = []
        parts.append(edition.product_name)
        parts.append(edition.get_formatted_edition_date)
        parts.append(edition.edition_number)
        parts.append(str(edition.geoname.value))

        filename = "-".join(parts)
        filename += edition.file_format

        return filename.lower()

