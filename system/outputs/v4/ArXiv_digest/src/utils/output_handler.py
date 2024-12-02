import csv

class OutputHandler:
    def printToConsole(self, data):
        for entry in data:
            print(f"Category: {entry['category']}")
            print(f"Title: {entry['title']}")
            print(f"Author: {entry['author']}")
            print(f"Abstract: {entry['abstract']}")
            print(f"Published: {entry['published']}")
            print(f"Link: {entry['link']}")
            print("-" * 40)

    def saveToCSV(self, data, filePath):
        with open(filePath, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=['category', 'title', 'author', 'abstract', 'published', 'link'])
            writer.writeheader()
            for entry in data:
                writer.writerow(entry)
