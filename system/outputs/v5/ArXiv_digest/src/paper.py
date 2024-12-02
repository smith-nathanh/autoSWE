from datetime import datetime

class Paper:
    def __init__(self, category, title, author, abstract, published, link):
        self.category = category
        self.title = title
        self.author = author
        self.abstract = abstract
        self.published = datetime.strptime(published, '%Y-%m-%dT%H:%M:%SZ')
        self.link = link

    def __repr__(self):
        return f"Paper(category={self.category}, title={self.title}, author={self.author}, published={self.published})"
