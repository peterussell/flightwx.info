package info.flightwx.fetcher.infrastructure;

import info.flightwx.fetcher.domain.ChartEdition;

public abstract class AbstractFileSystem {
    public abstract ChartEdition GetLocalChartEdition(ChartEdition remoteChartEdition);
    public abstract void DeleteRaster(ChartEdition chartEdition);
    public abstract String GetRasterPath(ChartEdition chartEdition);
    public abstract String GetMBTilesPath(ChartEdition chartEdition);
    private boolean isChartCurrent(ChartEdition localEdition, ChartEdition remoteEdition) {
        return localEdition.getEditionNumber() >= remoteEdition.getEditionNumber();
    }
}
