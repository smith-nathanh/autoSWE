import urllib.request

class APIInteraction:
    def fetchData(self, url):
        with urllib.request.urlopen(url) as response:
            return response.read()
