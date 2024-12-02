import xml.etree.ElementTree as ET

class XMLParser:
    def parse(self, xml_data):
        root = ET.fromstring(xml_data)
        namespace = {'ns': 'http://www.w3.org/2005/Atom'}
        entries = root.findall('ns:entry', namespace)
        results = []
        for entry in entries:
            result = {
                'category': entry.find('ns:category', namespace).attrib.get('term', 'N/A'),
                'title': entry.find('ns:title', namespace).text,
                'author': entry.find('ns:author/ns:name', namespace).text,
                'abstract': entry.find('ns:summary', namespace).text,
                'published': entry.find('ns:published', namespace).text,
                'link': entry.find('ns:link', namespace).attrib.get('href', 'N/A')
            }
            results.append(result)
        return results
