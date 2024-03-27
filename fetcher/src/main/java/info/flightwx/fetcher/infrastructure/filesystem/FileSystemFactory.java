package info.flightwx.fetcher.infrastructure.filesystem;

public abstract class FileSystemFactory {
    public FileSystem Create() {
        return createFileSystem();
    }

    protected abstract FileSystem createFileSystem();
}
