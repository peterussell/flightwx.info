package info.flightwx.fetcher.services;

import info.flightwx.fetcher.domain.ChartEdition;
import info.flightwx.fetcher.infrastructure.filesystem.FileSystem;
import info.flightwx.fetcher.types.ChartType;
import info.flightwx.fetcher.types.Geoname;

public class FaaService implements IFaaService {
    private final FileSystem fileSystem;

    public FaaService(FileSystem fileSystem) {
        this.fileSystem = fileSystem;
    }

    @Override
    public ChartEdition GetVfrChartEdition(ChartType chartType, Geoname geoname) {
        // TODO
        throw new UnsupportedOperationException("Not implemented");
    }

    @Override
    public String DownloadChart(ChartEdition chartEdition) {
        // TODO
        throw new UnsupportedOperationException("Not implemented");
    }
}
