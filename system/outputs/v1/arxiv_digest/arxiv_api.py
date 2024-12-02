import urllib.request
import urllib.parse

class ArXivAPI:
    BASE_URL = "http://export.arxiv.org/api/query?"

    def construct_query_url(self, category, title, author, abstract, max_results):
        query_parts = []
        if category:
            query_parts.append(f"cat:{category}")
        if title:
            query_parts.append(f"ti:{title}")
        if author:
            query_parts.append(f"au:{author}")
        if abstract:
            query_parts.append(f"abs:{abstract}")

        query = '+AND+'.join(query_parts)
        url = f"{self.BASE_URL}search_query={query}&sortBy=submittedDate&sortOrder=descending&start=0&max_results={max_results}"
        return url

    def fetch_data(self, url):
        with urllib.request.urlopen(url) as response:
            return response.read()
