import csv

class CSVParser:
    def __init__(self, filepath, delimiter=','):
        self.filepath = filepath
        self.delimiter = delimiter
        self.column_names = []
        self.data_rows = []

    def read_csv(self):
        with open(self.filepath, mode='r', newline='', encoding='utf-8') as csvfile:
            csvreader = csv.reader(csvfile, delimiter=self.delimiter)
            self.column_names = next(csvreader)
            self.data_rows = [row for row in csvreader]

    def extract_column_names(self):
        return self.column_names

    def extract_data_rows(self):
        return self.data_rows
