package info.flightwx.fetcher.services;

public class FaaWebService implements IFaaWebService {
    private String baseUrl;

    public FaaWebService(String baseUrl) {
        this.baseUrl = baseUrl;
    }

    public void UpdateCharts() {
        UpdateSectionalCharts();
        UpdateTerminalAreaCharts();
        UpdateGulfCoastCharts();
        UpdateGrandCanyonCharts();
        UpdateHelicopterCharts();
        UpdateCaribbeanCharts();
        UpdatePlanningCharts();
    }

    private void UpdateSectionalCharts() {
        System.out.println("Updating Sectional charts");
    }

    private void UpdateTerminalAreaCharts() {
        System.out.println("Updating Terminal Area charts");
    }

    private void UpdateGulfCoastCharts() {
        System.out.println("Updating Gulf Coast charts");
    }

    private void UpdateGrandCanyonCharts() {
        System.out.println("Updating Grand Canyon charts");
    }

    private void UpdateHelicopterCharts() {
        System.out.println("Updating Helicopter charts");
    }

    private void UpdateCaribbeanCharts() {
        System.out.println("Updating Caribbean charts");
    }

    private void UpdatePlanningCharts() {
        System.out.println("Updating Planning charts");
    }

    private void Get56DaySetsMetadata() {
        throw new UnsupportedOperationException();
    }
}
