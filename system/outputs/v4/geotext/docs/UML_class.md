classDiagram
    class GeoText {
        +extract_cities(text: str) : List[str]
        +extract_countries(text: str) : List[str]
        +filter_cities_by_country(cities: List[str], country_code: str) : List[str]
        +count_country_mentions(text: str) : Dict[str, int]
    }
    class DataLoader {
        +load_city_patches() : Dict[str, str]
        +load_country_info() : Dict[str, Any]
        +load_nationalities() : Dict[str, str]
        +load_cities() : List[Dict[str, Any]]
    }
    GeoText --> DataLoader : uses
    class CityPatch {
        -city_name: str
        -country_code: str
    }
    class CountryInfo {
        -iso: str
        -iso3: str
        -iso_numeric: str
        -fips: str
        -country: str
        -capital: str
        -area: int
        -population: int
        -continent: str
        -tld: str
        -currency_code: str
        -currency_name: str
        -phone: str
        -postal_code_format: str
        -postal_code_regex: str
        -languages: str
        -geonameid: int
        -neighbours: str
        -equivalent_fips_code: str
    }
    class Nationality {
        -nationality: str
        -country_code: str
    }
    class City {
        -geonameid: int
        -name: str
        -latitude: float
        -longitude: float
        -feature_class: str
        -feature_code: str
        -country_code: str
        -population: int
        -timezone: str
        -modification_date: str
    }
    DataLoader --> CityPatch : loads
    DataLoader --> CountryInfo : loads
    DataLoader --> Nationality : loads
    DataLoader --> City : loads