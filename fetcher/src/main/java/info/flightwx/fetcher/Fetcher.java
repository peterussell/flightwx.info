package info.flightwx.fetcher;

import info.flightwx.fetcher.infrastructure.api.FaaApi;
import info.flightwx.fetcher.infrastructure.config.Config;
import info.flightwx.fetcher.infrastructure.filesystem.FileSystem;
import info.flightwx.fetcher.infrastructure.filesystem.LocalFileSystemFactory;
import info.flightwx.fetcher.infrastructure.filesystem.S3FileSystemFactory;
import info.flightwx.fetcher.services.ChartService;
import info.flightwx.fetcher.services.FaaService;
import info.flightwx.fetcher.services.IChartService;

public class Fetcher {
    private final IChartService chartService;

    public Fetcher() throws InstantiationException {
        FaaService faaService = new FaaService(getFileSystem(), new FaaApi());
        this.chartService = new ChartService(faaService);
    }

    public void Run() {
        this.chartService.UpdateSectionalCharts();
    }

    private FileSystem getFileSystem() {
        String fsType = Config.GetConfig().get("FILESYSTEM").toLowerCase();

        return switch (fsType) {
            case "local" -> new LocalFileSystemFactory().Create();
            case "s3" -> new S3FileSystemFactory().Create();
            default -> throw new IllegalArgumentException("Invalid file system type " + fsType);
        };
    }
}
