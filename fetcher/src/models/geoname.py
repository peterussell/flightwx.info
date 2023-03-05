from enum import Enum
from typing import Type, TypeVar

T = TypeVar("T", bound="Geoname")

class Geoname(Enum):
    ALBUQUERQUE = "Albuquerque"
    CHICAGO = "Chicago"
    CINCINNATI = "Cincinnati"
    COLD_BAY = "Cold Bay"
    DALLAS_FT_WORTH = "Dallas-Ft Worth"
    DAWSON = "Dawson"
    DENVER = "Denver"
    DETROIT = "Detroit"
    DUTCH_HARBOR = "Dutch Harbor"
    EL_PASO = "El Paso"
    FAIRBANKS = "Fairbanks"
    ANCHORAGE = "Anchorage"
    GREAT_FALLS = "Great Falls"
    GREEN_BAY = "Green Bay"
    HALIFAX = "Halifax"
    HAWAIIAN_ISLANDS = "Hawaiian Islands"
    HOUSTON = "Houston"
    JACKSONVILLE = "Jacksonville"
    JUNEAU = "Juneau"
    KANSAS_CITY = "Kansas City"
    KETCHIKAN = "Ketchikan"
    KLAMATH_FALLS = "Klamath Falls"
    ATLANTA = "Atlanta"
    KODIAK = "Kodiak"
    LAKE_HURON = "Lake Huron"
    LAS_VEGAS = "Las Vegas"
    LOS_ANGELES = "Los Angeles"
    MCGRATH = "McGrath"
    MEMPHIS = "Memphis"
    MIAMI = "Miami"
    MONTREAL = "Montreal"
    NEW_ORLEANS = "New Orleans"
    NEW_YORK = "New York"
    BETHEL = "Bethel"
    NOME = "Nome"
    OMAHA = "Omaha"
    PHOENIX = "Phoenix"
    POINT_BARROW = "Point Barrow"
    SALT_LAKE_CITY = "Salt Lake City"
    SAN_ANTONIO = "San Antonio"
    SAN_FRANCISCO = "San Francisco"
    SEATTLE = "Seattle"
    SEWARD = "Seward"
    ST_LOUIS = "St Louis"
    BILLINGS = "Billings"
    TWIN_CITIES = "Twin Cities"
    WASHINGTON = "Washington"
    WESTERN_ALEUTIAN_ISLANDS = "Western Aleutian Islands"
    WHITEHORSE = "Whitehorse"
    WICHITA = "Wichita"
    BROWNSVILLE = "Brownsville"
    CAPE_LISBURNE = "Cape Lisburne"
    CHARLOTTE = "Charlotte"
    CHEYENNE = "Cheyenne"
    NONE = ""


    def to_safe_str(self):
        return self.value.replace(" ", "%")


    @classmethod
    def from_safe_str(cls: Type[T], geoname_str: str) -> T:
        if not geoname_str:
            return None

        orig = geoname_str.replace("%", " ")
        return cls(orig)
