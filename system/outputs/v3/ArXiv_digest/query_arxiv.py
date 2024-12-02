import sys
from src.query_arxiv import QueryArXiv

if __name__ == "__main__":
    query_arxiv = QueryArXiv()
    query_arxiv.execute_query()