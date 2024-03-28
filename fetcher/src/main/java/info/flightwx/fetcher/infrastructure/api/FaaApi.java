package info.flightwx.fetcher.infrastructure.api;

import info.flightwx.fetcher.infrastructure.config.Config;

public class FaaApi {
    private final String BASE_URL = Config.GetConfig().get("FAA_BASE_URL");

    public void Get(String path) { // TODO: not void
        throw new UnsupportedOperationException("Not implemented");
    }

    public void DownloadFile(String url, String filePath) {
        throw new UnsupportedOperationException("Not implemented");
    }
}
