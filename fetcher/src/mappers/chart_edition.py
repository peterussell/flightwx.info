from urllib3 import HTTPResponse
import xml.etree.ElementTree as ET

from models.chart_edition import ChartEdition
from utils.xml import FAA_XML_NAMESPACE as NS

# TODO: test
def map_chart_edition(res: HTTPResponse) -> ChartEdition:
    """
    Maps a chart edition HTTPResponse from the FAA API to a ChartEdition object
    """
    root = ET.fromstring(res.text)
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
