from datetime import datetime, timedelta
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from src.utils.api_interaction import APIInteraction
from src.utils.xml_parser import XMLParser
from src.utils.output_handler import OutputHandler

class QueryArXiv:
    def __init__(self, category=None, title=None, author=None, abstract=None, recent_days=7, max_results=10, to_file=None, verbose=False):
        self.category = category
        self.title = title
        self.author = author
        self.abstract = abstract
        self.recent_days = recent_days
        self.max_results = max_results
        self.to_file = to_file
        self.verbose = verbose

    def executeQuery(self):
        url = self.constructQueryURL()
        api = APIInteraction()
        raw_data = api.fetchData(url)
        parser = XMLParser()
        parsed_data = parser.parseData(raw_data)
        filtered_data = self.filterByDate(parsed_data)
        self.outputResults(filtered_data)

    def constructQueryURL(self):
        base_url = "http://export.arxiv.org/api/query?"
        query = []
        if self.category:
            query.append(f"cat:{self.category}")
        if self.title:
            query.append(f"ti:{self.title}")
        if self.author:
            query.append(f"au:{self.author}")
        if self.abstract:
            query.append(f"abs:{self.abstract}")
        query_str = '+AND+'.join(query)
        params = {
            'search_query': query_str,
            'sortBy': 'submittedDate',
            'sortOrder': 'descending',
            'start': 0,
            'max_results': self.max_results
        }
        return base_url + urllib.parse.urlencode(params)

    def filterByDate(self, data):
        recent_date = datetime.now() - timedelta(days=self.recent_days)
        return [entry for entry in data if datetime.strptime(entry['published'], '%Y-%m-%dT%H:%M:%SZ') > recent_date]

    def outputResults(self, data):
        output_handler = OutputHandler()
        if self.verbose:
            output_handler.printToConsole(data)
        if self.to_file:
            output_handler.saveToCSV(data, self.to_file)
