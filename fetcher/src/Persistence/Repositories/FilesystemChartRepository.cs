using System.IO;

namespace Persistence.Repositories;

public class FilesystemChartRepository: IChartRepository
{
    private string _basePath;

    public FilesystemChartRepository(string basePath = "")
    {
        this._basePath = basePath;
    }

    public bool Exists(string filename)
    {
        return File.Exists($"{this._basePath}/{filename}");
    }
}