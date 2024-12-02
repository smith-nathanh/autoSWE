import xml.etree.ElementTree as ET

class XMLParser:
    def parse(self, xml_data):
        root = ET.fromstring(xml_data)
        namespace = {'arxiv': 'http://arxiv.org/schemas/atom'}
        entries = []
        for entry in root.findall('arxiv:entry', namespace):
            category = entry.find('arxiv:category', namespace).attrib['term']
            title = entry.find('arxiv:title', namespace).text
            author = ', '.join([author.find('arxiv:name', namespace).text for author in entry.findall('arxiv:author', namespace)])
            abstract = entry.find('arxiv:summary', namespace).text
            published = entry.find('arxiv:published', namespace).text
            link = entry.find('arxiv:link', namespace).attrib['href']
            entries.append({
                'category': category,
                'title': title,
                'author': author,
                'abstract': abstract,
                'published': published,
                'link': link
            })
        return entries