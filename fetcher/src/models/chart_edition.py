"""
Contains a ChartEdition class, representing an edition/release of an
aeronautical chart.
"""
from datetime import datetime
from typing import Type, TypeVar

from models.geoname import Geoname

T = TypeVar("T", bound="ChartEdition")

class ChartEdition:
    FILENAME_DELIM: str = "_"

    """Represents an edition/release of an aeronautical chart."""

    FILESYSTEM_DATE_FORMAT = "%Y-%m-%d"
    API_DATE_FORMAT = "%m/%d/%Y"

    def __init__(
            self,
            geoname: Geoname = Geoname.NONE,
            edition_name: str = "",
            file_format: str = "",
            edition_date: datetime = None,
            edition_number: int = None,
            product_name: str  = "",
            product_url: str = ""
        ):
        self.geoname = Geoname(geoname)
        self.edition_name = edition_name
        self.file_format = file_format
        self.edition_date = edition_date
        self.edition_number = edition_number
        self.product_name = product_name
        self.product_url = product_url


    @classmethod
    def from_filename(cls: Type[T], base_path: str, file_path: str) -> T:
        """Constructs """
        file_path = file_path.replace(f"{base_path}/", "")
        file_path = file_path.replace(".zip", "")

        parts = file_path.split(ChartEdition.FILENAME_DELIM)

        product_name = parts[0]
        geoname = Geoname.from_safe_str(parts[1])
        edition_number = parts[2]
        edition_date = ChartEdition.parse_fs_edition_date(parts[3])

        return cls(
            geoname=geoname,
            product_name=product_name,
            edition_number=edition_number,
            edition_date=edition_date
        )


    # TODO: tests
    @staticmethod
    def parse_faa_edition_date(edition_date: str) -> datetime:
        """Parses the edition date in FAA format into a python datetime"""
        if edition_date == "":
            return None

        return datetime.strptime(edition_date, ChartEdition.API_DATE_FORMAT)


    # TODO: tests
    @staticmethod
    def parse_fs_edition_date(edition_date: str) -> datetime:
        """Parses the edition date formatted for the local filesystem (YYYY-mm-dd)"""
        if edition_date == "":
            return None

        return datetime.strptime(edition_date, ChartEdition.FILESYSTEM_DATE_FORMAT)


    # TODO: tests
    def format_edition_date_for_faa(self) -> str:
        """Returns the edition date formatted as YYYY-mm-dd"""
        if self.edition_date is None:
            return ""

        return datetime.strftime(self.edition_date, ChartEdition.API_DATE_FORMAT)


    # TODO: tests
    def format_edition_date_for_fs(self) -> str:
        """Returns the edition date formatted as YYYY-mm-dd"""
        if self.edition_date is None:
            return ""

        return datetime.strftime(self.edition_date, ChartEdition.FILESYSTEM_DATE_FORMAT)


    # TODO: tests
    def get_filename_prefix(self) -> str:
        """
        Returns the chart filename prefix (product name and geoname) without
        any version or date information, eg. "sectional_chicago"
        """
        return f"{self.product_name}_{self.geoname.to_safe_str()}"


    # TODO: tests
    def get_raster_path(self, rasters_base_path: str) -> str:
        """Returns the raster path+filename for this chart edition"""
        filename = self._generate_filename()
        return f"{rasters_base_path}/{filename}.zip"


    # TODO: tests
    def get_mbtiles_path(self, mbtiles_base_path: str) -> str:
        """Returns the mbtiles path+filename for this chart edition"""
        filename = self._generate_filename()
        return f"{mbtiles_base_path}/{filename}.mbtiles"


    # TODO: tests
    def _generate_filename(self) -> str:
        parts = []
        parts.append(self.product_name)
        parts.append(self.geoname.to_safe_str())
        parts.append(self.edition_number)
        parts.append(self.format_edition_date_for_fs())

        return ChartEdition.FILENAME_DELIM.join(parts)


    # TODO: tests
    def __str__(self):
        attrib = {
            "Geoname": self.geoname,
            "Edition name" : self.edition_name,
            "File format": self.file_format,
            "Edition date": self.format_edition_date_for_fs(),
            "Edition number" : self.edition_number,
            "Product name" : self.product_name,
            "URL": self.product_url,
        }

        res = ""
        for k,v in attrib.items():
            res += f"{k}: {v}\n"

        return res
