package info.flightwx.fetcher;

import info.flightwx.fetcher.infrastructure.AbstractFileSystem;
import info.flightwx.fetcher.services.IFaaService;
import info.flightwx.fetcher.services.FaaService;

public class Fetcher {
    private IFaaService faaService;

    public Fetcher(AbstractFileSystem fileSystem) {
        this.faaService = new FaaService(fileSystem);
        // TODO
        // this.chartService = new ChartService(faaService);
    }

    public void Run() {
        // TODO: this.chartService.UpdateSectionalCharts();
    }
}
