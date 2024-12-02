# csv_parser.py

import csv
from typing import List, Dict, Any

class CSVParser:
    def read_csv(self, filepath: str, delimiter: str = ',') -> List[Dict[str, Any]]:
        with open(filepath, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file, delimiter=delimiter)
            return [row for row in reader]

    def extract_column_names(self, data: List[Dict[str, Any]]) -> List[str]:
        if data:
            return list(data[0].keys())
        return []

    def extract_data_rows(self, data: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        return data