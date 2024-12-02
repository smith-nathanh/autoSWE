import csv

class CSVExporter:
    def export_to_csv(self, results, file_path):
        with open(file_path, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=['category', 'title', 'author', 'abstract', 'published', 'link'])
            writer.writeheader()
            for result in results:
                writer.writerow(result)
