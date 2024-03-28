package info.flightwx.fetcher.services;

import info.flightwx.fetcher.domain.ChartEdition;
import info.flightwx.fetcher.infrastructure.api.FaaApi;
import info.flightwx.fetcher.infrastructure.filesystem.FileSystem;
import info.flightwx.fetcher.types.ChartType;
import info.flightwx.fetcher.types.Geoname;

public class FaaService implements IFaaService {
    private final FileSystem fileSystem;
    private final FaaApi faaApi;

    public FaaService(FileSystem fileSystem, FaaApi faaApi) throws InstantiationException {
        if (fileSystem == null) { throw new InstantiationException("File system not initialized"); }
        if (faaApi == null) { throw new InstantiationException("FAA API not initialized"); }

        this.fileSystem = fileSystem;
        this.faaApi = faaApi;
    }

    /**
     * {@inheritDoc}
     */
    @Override
    public ChartEdition GetVfrChartEdition(ChartType chartType, Geoname geoname) {
        // TODO - working here
        throw new UnsupportedOperationException("Not implemented");
    }

    /**
     * {@inheritDoc}
     */
    @Override
    public void DownloadChart(ChartEdition chartEdition) {
        // TODO
        throw new UnsupportedOperationException("Not implemented");
    }
}
