package info.flightwx.fetcher.services;

import info.flightwx.fetcher.infrastructure.filesystem.FileSystem;

import java.util.ArrayList;

public class ChartService implements IChartService {
    private FileSystem fileSystem;
    private IFaaService faaService;

    public ChartService(FileSystem fileSystem) {
        this.fileSystem = fileSystem;
    }

    @Override
    public ArrayList<String> UpdateSectionalCharts() {
        throw new UnsupportedOperationException("Not implemented");
    }
}
