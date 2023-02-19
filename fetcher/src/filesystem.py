from models.geoname import Geoname

def is_chart_current(chart_name: Geoname) -> bool:
    # tmp - just update the Chicago chart
    if chart_name is Geoname.CHICAGO:
        return False

    return True
