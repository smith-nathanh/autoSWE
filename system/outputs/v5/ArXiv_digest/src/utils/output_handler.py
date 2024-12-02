import csv


def output_results(papers, to_file, verbose):
    if verbose:
        for paper in papers:
            print(f"Category: {paper.category}")
            print(f"Title: {paper.title}")
            print(f"Author: {paper.author}")
            print(f"Abstract: {paper.abstract}")
            print(f"Published: {paper.published}")
            print(f"Link: {paper.link}")
            print("-" * 40)

    if to_file:
        with open(to_file, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(['Category', 'Title', 'Author', 'Abstract', 'Published', 'Link'])
            for paper in papers:
                writer.writerow([paper.category, paper.title, paper.author, paper.abstract, paper.published, paper.link])
