import xml.etree.ElementTree as ET
from src.paper import Paper


def parse_xml_data(xml_data):
    root = ET.fromstring(xml_data)
    papers = []
    for entry in root.findall('{http://www.w3.org/2005/Atom}entry'):
        category = entry.find('{http://arxiv.org/schemas/atom}primary_category').attrib['term']
        title = entry.find('{http://www.w3.org/2005/Atom}title').text
        author = ', '.join([author.find('{http://www.w3.org/2005/Atom}name').text for author in entry.findall('{http://www.w3.org/2005/Atom}author')])
        abstract = entry.find('{http://www.w3.org/2005/Atom}summary').text
        published = entry.find('{http://www.w3.org/2005/Atom}published').text
        link = entry.find('{http://www.w3.org/2005/Atom}id').text
        papers.append(Paper(category, title, author, abstract, published, link))
    return papers
