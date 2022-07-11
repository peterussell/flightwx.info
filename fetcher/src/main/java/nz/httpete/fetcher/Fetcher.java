package nz.httpete.fetcher;

import nz.httpete.fetcher.services.FaaWebService;

public class Fetcher {
    private FaaWebService faaWebService;

    public Fetcher(String baseUrl) {
        this.faaWebService = new FaaWebService(baseUrl);
    }

    public void Run() {
        this.faaWebService.UpdateCharts();
    }
}
