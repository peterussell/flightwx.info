package info.flightwx.fetcher.services;

import info.flightwx.fetcher.domain.ChartEdition;
import info.flightwx.fetcher.types.ChartType;
import info.flightwx.fetcher.types.Geoname;

public interface IFaaService {
    public ChartEdition GetVfrChartEdition(ChartType chartType, Geoname geoname);
    public String DownloadChart(ChartEdition chartEdition);
}
