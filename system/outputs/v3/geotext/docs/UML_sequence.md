sequenceDiagram
    participant User
    participant GeoText
    participant DataFileLoader
    User->>GeoText: extract_cities(text)
    GeoText->>DataFileLoader: load_city_patches()
    DataFileLoader-->>GeoText: city_patches
    GeoText->>DataFileLoader: load_cities()
    DataFileLoader-->>GeoText: cities
    GeoText-->>User: List of cities
    User->>GeoText: extract_countries(text)
    GeoText->>DataFileLoader: load_country_info()
    DataFileLoader-->>GeoText: country_info
    GeoText-->>User: List of countries
    User->>GeoText: count_country_mentions(text)
    GeoText->>DataFileLoader: load_country_info()
    DataFileLoader-->>GeoText: country_info
    GeoText-->>User: Country mention counts