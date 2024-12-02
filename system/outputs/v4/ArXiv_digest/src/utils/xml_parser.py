import xml.etree.ElementTree as ET

class XMLParser:
    def parseData(self, xmlData):
        root = ET.fromstring(xmlData)
        ns = {'arxiv': 'http://www.w3.org/2005/Atom'}
        entries = []
        for entry in root.findall('arxiv:entry', ns):
            entry_data = {
                'category': entry.find('arxiv:category', ns).attrib['term'],
                'title': entry.find('arxiv:title', ns).text,
                'author': ', '.join([author.find('arxiv:name', ns).text for author in entry.findall('arxiv:author', ns)]),
                'abstract': entry.find('arxiv:summary', ns).text.strip(),
                'published': entry.find('arxiv:published', ns).text,
                'link': entry.find('arxiv:link', ns).attrib['href']
            }
            entries.append(entry_data)
        return entries
