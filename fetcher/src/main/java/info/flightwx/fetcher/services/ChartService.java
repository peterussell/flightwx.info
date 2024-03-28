package info.flightwx.fetcher.services;

import java.util.ArrayList;

public class ChartService implements IChartService {
    private IFaaService faaService;

    public ChartService(IFaaService faaService) {
        this.faaService = faaService;
    }

    @Override
    public ArrayList<String> UpdateSectionalCharts() {
        System.out.println("Updating sectional charts...");
        return null; // tmp
    }
}
