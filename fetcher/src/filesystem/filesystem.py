from abc import ABC, abstractmethod
from datetime import datetime

from models.chart_edition import ChartEdition
from models.geoname import Geoname

FILENAME_DELIM: str = "_"

class Filesystem:
    @abstractmethod
    def chart_exists(self, edition: ChartEdition) -> bool:
        pass


    @abstractmethod
    def get_chart_meta(self, chart_name: Geoname) -> bool:
        pass


    @abstractmethod
    def get_saved_chart_edition(self, chart_name: Geoname) -> ChartEdition | None:
        pass


    # TODO: change to get_file_path, and internally call ChartEdition.get_filename(),
    # and prefix with base_path (in concrete classes)
    @abstractmethod
    def get_filename(self, edition: ChartEdition) -> str:
        pass


    # TODO: tests
    # TODO: move to ChartEdition.get_filename()
    def _get_filename(self, base_path: str, edition: ChartEdition) -> str:
        """Returns a filename for a given chart edition"""
        parts = []
        parts.append(edition.product_name)
        parts.append(str(edition.geoname.value.replace(" ", "")))
        parts.append(edition.edition_number)
        parts.append(edition.get_formatted_edition_date())

        return f"{base_path}/{FILENAME_DELIM.join(parts)}.zip".lower()


    # TODO: move to ChartEdition.from_filename(filename: str)
    def _get_edition_from_filename(self, base_path: str, file_path: str) -> ChartEdition:
        """Returns chart edition metadata given a local chart filename"""

        file_path = file_path.replace(f"{base_path}/", "")
        file_path = file_path.replace(".zip", "")

        parts = file_path.split(FILENAME_DELIM)

        # TODO: move this somewhere else, and is there a more pythonic way to do this?
        geoname: Geoname = None
        for g in Geoname:
            if g.value == parts[1]:
                geoname = g

        edition = ChartEdition()
        edition.product_name = parts[0]
        edition.geoname = geoname
        edition.edition_number = parts[2]
        edition.edition_date = edition.parse_formatted_edition_date(parts[3])

        return edition


    # TODO: tests
    def _is_chart_current(self, saved_edition: ChartEdition, api_edition: ChartEdition) -> bool:
        return saved_edition.edition_number >= api_edition.edition_number
