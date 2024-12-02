import markdown2

class MarkdownProcessor:
    def parse(self, content: str) -> str:
        html = markdown2.markdown(content)
        return HTMLProcessor().parse(html)