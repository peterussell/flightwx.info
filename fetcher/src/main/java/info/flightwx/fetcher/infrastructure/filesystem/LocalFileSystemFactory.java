package info.flightwx.fetcher.infrastructure.filesystem;

public class LocalFileSystemFactory extends FileSystemFactory {
    @Override
    public FileSystem createFileSystem() {
        return new LocalFileSystem();
    }
}
