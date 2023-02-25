"""
Contains a ChartEdition class, representing an edition/release of an
aeronautical chart.
"""
from datetime import datetime

from models.geoname import Geoname

class ChartEdition:
    """Represents an edition/release of an aeronautical chart."""

    FILESYSTEM_DATE_FORMAT = "%Y-%m-%d"
    API_DATE_FORMAT = "%m/%d/%Y"

    def __init__(
        self,
        geoname: Geoname = Geoname.NONE,
        edition_name: str = "",
        file_format: str = "",
        edition_date: str = "",
        edition_number: int = None,
        product_name: str  = "",
        product_url: str = ""
        ):
        self.geoname = Geoname(geoname)
        self.edition_name = edition_name
        self.file_format = file_format
        self.edition_date = self.parse_edition_date(edition_date)
        self.edition_number = edition_number
        self.product_name = product_name
        self.product_url = product_url

    def __str__(self):
        attrib = {
            "Geoname": self.geoname,
            "Edition name" : self.edition_name,
            "File format": self.file_format,
            "Edition date": self.get_formatted_edition_date(),
            "Edition number" : self.edition_number,
            "Product name" : self.product_name,
            "URL": self.product_url,
        }

        res = ""
        for k,v in attrib.items():
            res += f"{k}: {v}\n"

        return res


    def parse_edition_date(self, edition_date: str) -> datetime:
        """Parses the edition date in FAA format into a python datetime"""
        if edition_date == "":
            return None

        return datetime.strptime(edition_date, ChartEdition.API_DATE_FORMAT)


    def parse_formatted_edition_date(self, edition_date: str) -> datetime:
        """Parses the edition date formatted for the local filesystem (YYYY-mm-dd)"""
        if edition_date == "":
            return None

        return datetime.strptime(edition_date, ChartEdition.FILESYSTEM_DATE_FORMAT)


    def get_formatted_edition_date(self) -> str:
        """Returns the edition date formatted as YYYY-mm-dd"""
        if self.edition_date is None:
            return ""

        return datetime.strftime(self.edition_date, ChartEdition.FILESYSTEM_DATE_FORMAT)

    # TODO -- working here: move all the filename stuff into here, ChartEdition
    # should handle the to/from filename conversions, not the filesystem

    def get_filename_prefix(self) -> str:
        """
        Returns the chart filename prefix (product name and geoname) without
        any version or date information, eg. "sectional_chicago"
        """
        return f"{self.product_name}_{self.geoname.value}"
