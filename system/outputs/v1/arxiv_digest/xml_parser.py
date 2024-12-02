import xml.etree.ElementTree as ET

class XMLParser:
    def parse_xml(self, data):
        root = ET.fromstring(data)
        ns = {'arxiv': 'http://arxiv.org/schemas/atom'}
        results = []

        for entry in root.findall('arxiv:entry', ns):
            result = {
                'category': entry.find('arxiv:primary_category', ns).attrib['term'],
                'title': entry.find('arxiv:title', ns).text.strip(),
                'author': ', '.join(author.find('arxiv:name', ns).text for author in entry.findall('arxiv:author', ns)),
                'abstract': entry.find('arxiv:summary', ns).text.strip(),
                'published': entry.find('arxiv:published', ns).text,
                'link': entry.find('arxiv:id', ns).text
            }
            results.append(result)

        return results
