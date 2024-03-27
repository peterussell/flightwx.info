package info.flightwx.fetcher.infrastructure.filesystem;

public class S3FileSystemFactory extends FileSystemFactory {
    @Override
    public FileSystem createFileSystem() {
        return new S3FileSystem();
    }
}
