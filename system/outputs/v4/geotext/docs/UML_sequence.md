sequenceDiagram
    participant User
    participant GeoText
    participant DataLoader
    User->>GeoText: extract_cities(text)
    GeoText->>DataLoader: load_city_patches()
    DataLoader-->>GeoText: city_patches
    GeoText->>DataLoader: load_cities()
    DataLoader-->>GeoText: cities
    GeoText-->>User: List of cities
    User->>GeoText: extract_countries(text)
    GeoText->>DataLoader: load_country_info()
    DataLoader-->>GeoText: country_info
    GeoText-->>User: List of countries
    User->>GeoText: filter_cities_by_country(cities, country_code)
    GeoText-->>User: Filtered list of cities
    User->>GeoText: count_country_mentions(text)
    GeoText->>DataLoader: load_country_info()
    DataLoader-->>GeoText: country_info
    GeoText-->>User: Dictionary of country mentions