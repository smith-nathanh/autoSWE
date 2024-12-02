import urllib.request

class ArXivAPI:
    def fetch_data(self, query_url):
        with urllib.request.urlopen(query_url) as response:
            return response.read().decode('utf-8')
