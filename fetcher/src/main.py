"""An application to fetch and parse FAA aeronuatical charts"""
import api.faa_api as faa_api

if __name__ == "__main__":
    faa_api.update_sectional_charts()
