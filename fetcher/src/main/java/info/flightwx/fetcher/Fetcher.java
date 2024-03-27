package info.flightwx.fetcher;

import info.flightwx.fetcher.infrastructure.config.Config;
import info.flightwx.fetcher.infrastructure.filesystem.FileSystem;
import info.flightwx.fetcher.infrastructure.filesystem.LocalFileSystemFactory;
import info.flightwx.fetcher.infrastructure.filesystem.S3FileSystemFactory;
import info.flightwx.fetcher.services.FaaService;
import info.flightwx.fetcher.services.IFaaService;

public class Fetcher {
    private FileSystem fileSystem;
    private IFaaService faaService;

    public Fetcher() throws InstantiationException {
        initializeFileSystem();
        initializeFaaService();
    }

    public void Run() {
        System.out.println("Hello from the Fetcher");
    }

    private void initializeFileSystem() {
        String fsType = Config.GetConfig().get("FILESYSTEM");

        if (fsType.equalsIgnoreCase("local")) {
            this.fileSystem = new LocalFileSystemFactory().Create();
        } else if (fsType.equalsIgnoreCase("s3")) {
            this.fileSystem = new S3FileSystemFactory().Create();
        }
    }

    private void initializeFaaService() throws InstantiationException {
        if (this.fileSystem == null) {
            throw new InstantiationException("Failed to create FAAService, no file system configured. Check .env FILESYSTEM value.");
        }

        this.faaService = new FaaService(this.fileSystem);
    }
}
