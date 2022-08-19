using System;

namespace Fetcher.Domain.Entities;

class ChartEdition
{
    public DateTime EditionDate { get; private set; }
    public Uri ZipUrl { get; private set; }
    public Uri PdfUrl { get; private set; }

    public ChartEdition(DateTime editionDate, Uri zipUrl, Uri pdfUrl)
    {
        this.EditionDate = editionDate;
        this.ZipUrl = zipUrl;
        this.PdfUrl = pdfUrl;
    }
}