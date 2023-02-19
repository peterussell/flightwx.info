"""
A module for interacting with the faa.gov aeronautical chart API
"""
from urllib3 import HTTPResponse
import xml.etree.ElementTree as ET

import api.api as api
import filesystem

from models.chart_edition import ChartEdition
from models.chart_type import ChartType
from models.geoname import Geoname

__all__ = ["update_charts"]

# Namespaces for the FAA XML docs
# NB. there may be a better way to extract these from the doc rather than hard coding them
NS = { "product_set": "http://arpa.ait.faa.gov/arpa_response" }


def _get_vfr_chart_url(chart_type: ChartType, geoname: Geoname) -> str:
    return f"vfr/{chart_type.value}/chart?geoname={geoname.value}&edition=current&format=tiff"


def _get_chart_edition(chart_type: ChartType, geoname: Geoname) -> None:
    url = _get_vfr_chart_url(chart_type, geoname)
    res: HTTPResponse = api.get(url)
    
    if (res.status != 200):
        raise RuntimeError(f"Received a {res.status} response from {url}")

    chart_edition = _parse_chart_edition(res)

    # tmp - testing
    print(str(chart_edition))


# TODO: test
def _parse_chart_edition(res: HTTPResponse) -> ChartEdition:
    root = ET.fromstring(res.data.decode("utf-8"))
    edition = root.find("product_set:edition", NS)

    # Geoname, edition name, and format are attributes of <edition>
    geoname = edition.attrib["geoname"]
    edition_name = edition.attrib["editionName"]
    file_format = edition.attrib["format"]

    # Edition date, number, and product are children of <edition>
    edition_date = edition.find("product_set:editionDate", NS).text
    edition_number = edition.find("product_set:editionNumber", NS).text

    # Product name and URL are attributes of <product>
    product = edition.find("product_set:product", NS)
    product_name = product.attrib["productName"]
    product_url = product.attrib["url"]

    chart_edition = ChartEdition(
        geoname,
        edition_name,
        file_format,
        edition_date,
        edition_number,
        product_name,
        product_url
    )
    
    return chart_edition


def update_sectional_charts() -> None:
    print("Updating sectional charts")
    for chart_name in Geoname:
        if not filesystem.is_chart_current(chart_name):
            _get_chart_edition(ChartType.SECTIONAL, chart_name)


def update_terminal_area_charts() -> None:
    """Updates terminal area charts"""
    print("Updating terminal area charts")

def update_gulf_coast_charts() -> None:
    """Updates Gulf Coast charts"""
    print("Updating Gulf Coast charts")

def update_grand_canyon_charts() -> None:
    """Updates Grand Canyon charts"""
    print("Updating Grand Canyon charts")

def update_helicopter_charts() -> None:
    """Updates helicopter charts")"""
    print("Updating helicopter charts")

def update_caribbean_charts() -> None:
    """Updates Caribbean charts")"""
    print("Updating Caribbean charts")

def update_planning_charts() -> None:
    """Updates planning charts")"""
    print("Updating planning charts")

def update_charts() -> None:
    """Updates all chart types"""
    update_sectional_charts()
    update_terminal_area_charts()
    update_gulf_coast_charts()
    update_grand_canyon_charts()
    update_helicopter_charts()
    update_caribbean_charts()
    update_planning_charts()
