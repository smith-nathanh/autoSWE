# Example usage of the Query ArXiv tool

# Fetch papers in the category 'cs.CL' by author 'Smith' with 'neural' in the title and 'learning' in the abstract, from the last 7 days, and save to 'results.csv'.
python query_arxiv.py --category cs.CL --author Smith --title neural --abstract learning --recent_days 7 --to_file results.csv --verbose
