"""
Contains a ChartEdition class, representing an edition/release of an
aeronautical chart.
"""

class ChartEdition:
    """Represents an edition/release of an aeronautical chart."""
    def __init__(self, edition_date, zip_url, pdf_url):
        self.edition_date = edition_date
        self.zip_url = zip_url
        self.pdf_url = pdf_url
