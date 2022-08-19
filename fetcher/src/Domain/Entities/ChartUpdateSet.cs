using Fetcher.Domain.Enums;

namespace Fetcher.Domain.Entities;

class ChartUpdateSet
{
    private ChartType _chartType;

    public ChartUpdateSet(ChartType chartType)
    {
        this._chartType = chartType;
    }
}