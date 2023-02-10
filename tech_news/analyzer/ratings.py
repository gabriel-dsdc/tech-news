# Requisito 10
from tech_news.database import find_news


def top_5_categories() -> list[str]:
    categories_list = [news["category"] for news in find_news()]
    categories_count = {}
    for category in categories_list:
        categories_count[category] = categories_list.count(category)
    categories_sorted = sorted(
        categories_count.items(), key=lambda x: (-x[1], x[0])
    )
    return [item[0] for item in categories_sorted[:5]]
