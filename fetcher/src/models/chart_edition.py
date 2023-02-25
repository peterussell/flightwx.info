"""
Contains a ChartEdition class, representing an edition/release of an
aeronautical chart.
"""
from datetime import datetime

from models.geoname import Geoname

class ChartEdition:
    """Represents an edition/release of an aeronautical chart."""
    def __init__(
        self,
        geoname: Geoname,
        edition_name: str,
        file_format: str,
        edition_date: str, # TODO: date type?
        edition_number: int,
        product_name: str,
        product_url: str
        ):
        self.geoname = geoname
        self.edition_name = edition_name
        self.file_format = file_format
        self.edition_date = datetime.strptime(edition_date, "%m/%d/%Y")
        self.edition_number = edition_number
        self.product_name = product_name
        self.product_url = product_url

    def __str__(self):
        attrib = {
            "Geoname": self.geoname,
            "Edition name" : self.edition_name,
            "File format": self.file_format,
            "Edition date": datetime.strftime(self.edition_date, "%m/%d/%Y"),
            "Edition number" : self.edition_number,
            "Product name" : self.product_name,
            "URL": self.product_url,
        }

        res = ""
        for k,v in attrib.items():
            res += f"{k}: {v}\n"

        return res

    def get_formatted_edition_date(self) -> str:
        """Returns the edition date formatted as YYYY-mm-dd"""
        if self.edition_date is None or len(self.edition_date) == 0:
            return ""

        parsed = datetime.strptime(self.edition_date, "mm/dd/YYYY")
        return datetime.strftime(parsed, "YYYY-mm-dd")
