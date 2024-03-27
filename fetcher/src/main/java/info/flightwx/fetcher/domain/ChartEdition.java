package info.flightwx.fetcher.domain;

import info.flightwx.fetcher.types.Geoname;

import java.util.Date;

public class ChartEdition {
    private Geoname geoname = Geoname.NONE;
    private String editionName;
    private String fileFormat;
    private Date editionDate;
    private int editionNumber;
    private String productName;
    private String productUrl;

    public ChartEdition(Geoname geoname, String editionName, String fileFormat, Date editionDate,
                        int editionNumber, String productName, String productUrl) {
        this.geoname = geoname;
        this.editionName = editionName;
        this.fileFormat = fileFormat;
        this.editionDate = editionDate;
        this.editionNumber = editionNumber;
        this.productName = productName;
        this.productUrl = productUrl;
    }

    public Geoname getGeoname() { return this.geoname; }
    public String getEditionName() { return this.editionName; }
    public String getFileFormat() { return this.fileFormat; }
    public Date getEditionDate() { return this.editionDate; }
    public int getEditionNumber() { return this.editionNumber; }
    public String getProductName() { return this.productName; }
    public String getProductUrl() { return this.productUrl; }

    // TODO: port rest of ChartEdition from python
}
