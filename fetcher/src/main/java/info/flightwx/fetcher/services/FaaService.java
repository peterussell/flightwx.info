package info.flightwx.fetcher.services;

import info.flightwx.fetcher.domain.ChartEdition;
import info.flightwx.fetcher.infrastructure.AbstractFileSystem;
import info.flightwx.fetcher.types.ChartType;
import info.flightwx.fetcher.types.Geoname;

public class FaaService implements IFaaService {
    private final AbstractFileSystem fileSystem;

    public FaaService(AbstractFileSystem fileSystem) {
        this.fileSystem = fileSystem;
    }

    public ChartEdition GetVfrChartEdition(ChartType chartType, Geoname geoname) {
        // TODO
        throw new UnsupportedOperationException();
    }

    public String DownloadChart(ChartEdition chartEdition) {
        // TODO
        throw new UnsupportedOperationException();
    }
}
