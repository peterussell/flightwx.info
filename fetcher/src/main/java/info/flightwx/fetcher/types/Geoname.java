package info.flightwx.fetcher.types;

public enum Geoname {
    ALBUQUERQUE("Albuquerque"),
    CHICAGO("Chicago"),
    CINCINNATI("Cincinnati"),
    COLD_BAY("Cold Bay"),
    DALLAS_FT_WORTH("Dallas-Ft Worth"),
    DAWSON("Dawson"),
    DENVER("Denver"),
    DETROIT("Detroit"),
    DUTCH_HARBOR("Dutch Harbor"),
    EL_PASO("El Paso"),
    FAIRBANKS("Fairbanks"),
    ANCHORAGE("Anchorage"),
    GREAT_FALLS("Great Falls"),
    GREEN_BAY("Green Bay"),
    HALIFAX("Halifax"),
    HAWAIIAN_ISLANDS("Hawaiian Islands"),
    HOUSTON("Houston"),
    JACKSONVILLE("Jacksonville"),
    JUNEAU("Juneau"),
    KANSAS_CITY("Kansas City"),
    KETCHIKAN("Ketchikan"),
    KLAMATH_FALLS("Klamath Falls"),
    ATLANTA("Atlanta"),
    KODIAK("Kodiak"),
    LAKE_HURON("Lake Huron"),
    LAS_VEGAS("Las Vegas"),
    LOS_ANGELES("Los Angeles"),
    MCGRATH("McGrath"),
    MEMPHIS("Memphis"),
    MIAMI("Miami"),
    MONTREAL("Montreal"),
    NEW_ORLEANS("New Orleans"),
    NEW_YORK("New York"),
    BETHEL("Bethel"),
    NOME("Nome"),
    OMAHA("Omaha"),
    PHOENIX("Phoenix"),
    POINT_BARROW("Point Barrow"),
    SALT_LAKE_CITY("Salt Lake City"),
    SAN_ANTONIO("San Antonio"),
    SAN_FRANCISCO("San Francisco"),
    SEATTLE("Seattle"),
    SEWARD("Seward"),
    ST_LOUIS("St Louis"),
    BILLINGS("Billings"),
    TWIN_CITIES("Twin Cities"),
    WASHINGTON("Washington"),
    WESTERN_ALEUTIAN_ISLANDS("Western Aleutian Islands"),
    WHITEHORSE("Whitehorse"),
    WICHITA("Wichita"),
    BROWNSVILLE("Brownsville"),
    CAPE_LISBURNE("Cape Lisburne"),
    CHARLOTTE("Charlotte"),
    CHEYENNE("Cheyenne"),
    NONE("");

    private final String friendlyName;

    private Geoname(String friendlyName) {
        this.friendlyName = friendlyName;
    }

    public String GetFriendlyName() {
        return this.friendlyName;
    }
}
