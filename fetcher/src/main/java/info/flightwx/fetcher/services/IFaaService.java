package info.flightwx.fetcher.services;

import info.flightwx.fetcher.domain.ChartEdition;
import info.flightwx.fetcher.types.ChartType;
import info.flightwx.fetcher.types.Geoname;

public interface IFaaService {
    /**
     * Gets the chart edition metadata for a VFR chart matching the specified chart type and geoname.
     *
     * @param chartType type of chart to retrieve chart edition metadata for
     * @param geoname geoname of chart to retrieve chart edition metadata for
     * @return chart edition metadata for the requested chart
     */
    public ChartEdition GetVfrChartEdition(ChartType chartType, Geoname geoname);

    /**
     * Downloads the chart file matching the given chart edition and saves it to the file system.
     *
     * @param chartEdition chart edition metadata specifying the chart to download
     */
    public void DownloadChart(ChartEdition chartEdition);
}
