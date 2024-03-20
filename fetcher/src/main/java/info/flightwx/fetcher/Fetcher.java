package info.flightwx.fetcher;

import info.flightwx.fetcher.services.IFaaWebService;
import info.flightwx.fetcher.services.FaaWebService;

public class Fetcher {
    private IFaaWebService faaWebService;

    public Fetcher(String baseUrl) {
        this.faaWebService = new FaaWebService(baseUrl);
    }

    public void Run() {
        this.faaWebService.UpdateCharts();
    }
}
