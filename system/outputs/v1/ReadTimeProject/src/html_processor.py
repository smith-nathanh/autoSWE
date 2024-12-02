from bs4 import BeautifulSoup

class HTMLProcessor:
    def parse(self, content: str) -> str:
        soup = BeautifulSoup(content, 'lxml')
        return soup.get_text(separator=' ', strip=True)