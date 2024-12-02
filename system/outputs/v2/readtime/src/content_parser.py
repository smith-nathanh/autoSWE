from bs4 import BeautifulSoup
import markdown2

class ContentParser:
    def parse_plain_text(self, content: str) -> str:
        return content

    def parse_html(self, content: str) -> str:
        soup = BeautifulSoup(content, 'lxml')
        return soup.get_text()

    def parse_markdown(self, content: str) -> str:
        html = markdown2.markdown(content)
        return self.parse_html(html)