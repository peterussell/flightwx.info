package info.flightwx.fetcher.infrastructure.filesystem;

import info.flightwx.fetcher.domain.ChartEdition;

public class LocalFileSystem extends FileSystem {
    public ChartEdition GetLocalChartEdition(ChartEdition remoteChartEdition) {
        throw new UnsupportedOperationException("Not implemented");
    }

    public void DeleteRaster(ChartEdition chartEdition)
    {
        throw new UnsupportedOperationException("Not implemented");
    }

    public String GetRasterPath(ChartEdition chartEdition) {
        throw new UnsupportedOperationException("Not implemented");
    }

    public String GetMBTilesPath(ChartEdition chartEdition) {
        throw new UnsupportedOperationException("Not implemented");
    }
}
