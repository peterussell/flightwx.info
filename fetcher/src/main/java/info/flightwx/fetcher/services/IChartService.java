package info.flightwx.fetcher.services;

import java.util.ArrayList;

public interface IChartService {
    /**
     * Checks charts on the file system against the FAA API and updates any that aren't current.
     *
     * @return A list of any ChartEditions for charts which were updated.
     */
    public ArrayList<String> UpdateSectionalCharts();
}
