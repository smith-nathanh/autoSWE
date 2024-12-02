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
    class City {
        -name: str
        -country_code: str
    }
    class Country {
        -name: str
        -iso_code: str
    }
    GeoText --> City : extracts
    GeoText --> Country : extracts