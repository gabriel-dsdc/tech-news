# Requisito 7
from datetime import datetime
from tech_news.database import search_news


def search_by_title(title: str) -> list[tuple[str, str]]:
    news_list = search_news({"title": {"$regex": title, "$options": "i"}})
    return [(news["title"], news["url"]) for news in news_list]


# Requisito 8
def search_by_date(date: str) -> list[tuple[str, str]]:
    try:
        formatted_date = datetime.strptime(date, "%Y-%m-%d").strftime(
            "%d/%m/%Y"
        )
        news_list = search_news({"timestamp": formatted_date})
        return [(news["title"], news["url"]) for news in news_list]
    except ValueError:
        raise ValueError("Data inválida")


# Requisito 9
def search_by_category(category: str) -> list[tuple[str, str]]:
    news_list = search_news(
        {"category": {"$regex": category, "$options": "i"}}
    )
    return [(news["title"], news["url"]) for news in news_list]
