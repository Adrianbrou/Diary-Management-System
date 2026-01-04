# utils.py

def filter_by_tag(entries, tag):
    return list(filter(lambda e: tag in e["tags"], entries))


def search_by_keyword(entries, keyword):
    return list(filter(
        lambda e: keyword.lower() in e["title"].lower()
        or keyword.lower() in e["content"].lower(),
        entries
    ))


def sort_by_date(entries):
    return sorted(entries, key=lambda e: e["date"])


def extract_titles(entries):
    return list(map(lambda e: e["title"], entries))
