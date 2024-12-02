import csv

class CSVParser:
    def __init__(self):
        self.column_names = []
        self.data_rows = []

    def read_csv(self, filepath, delimiter=','):
        with open(filepath, mode='r', newline='') as file:
            reader = csv.reader(file, delimiter=delimiter)
            self.column_names = next(reader)
            self.data_rows = [row for row in reader]

    def extract_column_names(self):
        return self.column_names

    def extract_data_rows(self):
        return self.data_rows