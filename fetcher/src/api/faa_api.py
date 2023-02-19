"""
A module for interacting with the faa.gov aeronautical chart API
"""
from urllib3 import HTTPResponse
import xml.etree.ElementTree as ET

import api.api as api
import filesystem
from models.chart_type import ChartType
from models.geoname import Geoname

__all__ = ["update_charts"]

SECTIONAL_URL = "vfr/sectional"
SECTIONAL_CHART_URL = f"{SECTIONAL_URL}/chart"
SECTIONAL_INFO_URL = f"{SECTIONAL_URL}/info"



def _get_sectional_info(geoname: Geoname) -> None:
    api.get(f"{SECTIONAL_INFO_URL}?geoname={geoname.value}")

def _get_vfr_chart_url(chart_type: ChartType, geoname: Geoname) -> str:
    return f"vfr/{chart_type.value}/chart?geoname={geoname.value}&edition=current&format=tiff"

def _get_chart_meta(chart_type: ChartType, geoname: Geoname) -> None:
    # res: HTTPResponse = api.get(_get_vfr_chart_url(chart_type, geoname))

    # tmp - test parsing using a string
    tmp_data = '<?xml version="1.0" encoding="UTF-8" standalone="yes"?><productSet xmlns="http://arpa.ait.faa.gov/arpa_response"><status code="200" message="OK"/><edition geoname="Chicago" editionName="CURRENT" format="TIFF"><editionDate>12/29/2022</editionDate><editionNumber>114</editionNumber><product productName="SECTIONAL" url="https://aeronav.faa.gov/visual/12-29-2022/sectional-files/Chicago.zip"/></edition></productSet>'

    ns = {"product_set": "http://arpa.ait.faa.gov/arpa_response"}
    
    root = ET.fromstring(tmp_data)
    edition = root.find("product_set:edition", ns)

    edition_attrib = edition.attrib
    # edition_date_attrib = root.find("product_set:editionDate", ns) # not working

    # this is working!
    geoname = edition_attrib["geoname"]
    edition_name = edition_attrib["editionName"]
    format = edition_attrib["format"]

    # edition_date = edition_date_attrib.text # not working

    print(edition_date_attrib)

    print(f"Geoname: {geoname}")
    print(f"Edition name: {edition_name}")
    print(f"Format: {format}")
    # print(f"Edition date: {edition_date}") # not working



    # if (res.status == 200):
    #     body = res.data.decode("utf-8")
    #     print(body) # tmp
    #     root = ET.fromstring(body)

    #     for child in root:
    #         print(child.tag)


def update_sectional_charts() -> None:
    print("Updating sectional charts")
    for chart_name in Geoname:
        if not filesystem.is_chart_current(chart_name):
            _get_chart_meta(ChartType.SECTIONAL, chart_name)











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
