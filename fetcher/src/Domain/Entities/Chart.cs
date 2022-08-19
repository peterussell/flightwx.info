namespace Fetcher.Domain.Entities;

class Chart
{
    public string Name { get; private set; }
    public ChartEdition CurrentEdition { get; private set; }
    public ChartEdition NextEdition { get; private set; }

    public Chart(string name, ChartEdition currentEdition, ChartEdition nextEdition)
    {
        this.Name = name;
        this.CurrentEdition = currentEdition;
        this.NextEdition = nextEdition;
    }
}