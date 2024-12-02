from datetime import datetime, timedelta


def filter_by_date(papers, recent_days):
    cutoff_date = datetime.now() - timedelta(days=recent_days)
    return [paper for paper in papers if paper.published >= cutoff_date]
