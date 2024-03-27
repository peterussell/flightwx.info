package info.flightwx.fetcher.infrastructure.filesystem;

import info.flightwx.fetcher.domain.ChartEdition;

public abstract class FileSystem {
    public abstract ChartEdition GetLocalChartEdition(ChartEdition remoteChartEdition);
    public abstract void DeleteRaster(ChartEdition chartEdition);
    public abstract String GetRasterPath(ChartEdition chartEdition);
    public abstract String GetMBTilesPath(ChartEdition chartEdition);
    private boolean isChartCurrent(ChartEdition localEdition, ChartEdition remoteEdition) {
        return localEdition.getEditionNumber() >= remoteEdition.getEditionNumber();
    }
}
