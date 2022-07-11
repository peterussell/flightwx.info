package nz.httpete.fetcher.services;

public class FaaWebService {
    private String baseUrl;

    public FaaWebService(String baseUrl) {
        this.baseUrl = baseUrl;
    }

    public void UpdateCharts() {
        UpdateSectionalCharts();
        UpdateTerminalAreaCharts();
        UpdateHelicopterCharts();
        UpdateCaribbeanCharts();
        UpdatePlanningCharts();
    }

    private void UpdateSectionalCharts() {
        System.out.println("Updating sectional charts");
    }

    private void UpdateTerminalAreaCharts() {
        System.out.println("Updating terminal area charts");
    }

    private void UpdateHelicopterCharts() {
        System.out.println("Updating helicopter charts");
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
