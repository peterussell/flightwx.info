namespace Persistence.Repositories;

interface IChartRepository
{
    public bool Exists(string filename);
}