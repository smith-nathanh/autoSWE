from datetime import datetime, timedelta

def check_date(published_date, recent_days):
    published_date = datetime.strptime(published_date, '%Y-%m-%dT%H:%M:%SZ')
    cutoff_date = datetime.now() - timedelta(days=recent_days)
    return published_date >= cutoff_date
