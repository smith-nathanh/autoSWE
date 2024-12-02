import urllib.request


def fetch_data(url):
    with urllib.request.urlopen(url) as response:
        return response.read()
