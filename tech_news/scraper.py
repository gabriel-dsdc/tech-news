# Requisito 1
import time
import requests
from parsel import Selector
from tech_news.database import create_news


HTML = str


def fetch(url: str) -> HTML | None:
    try:
        response = requests.get(
            url, timeout=3, headers={"user-agent": "Fake user-agent"}
        )
        time.sleep(1)
        if response.status_code == 200:
            return response.text
    except requests.ReadTimeout:
        return None


# Requisito 2
def scrape_updates(html_content: HTML) -> list[str]:
    selector = Selector(text=html_content)
    news_url = selector.css(".entry-title a::attr(href)").getall()
    if news_url:
        return news_url
    return []


# Requisito 3
def scrape_next_page_link(html_content: HTML) -> str | None:
    selector = Selector(text=html_content)
    next_link = selector.css("a.next::attr(href)").get()
    if next_link:
        return next_link
    return None


# Requisito 4
def scrape_news(html_content: HTML) -> dict[str, int]:
    news = {}
    selector = Selector(text=html_content)
    news["url"] = selector.css("link[rel='canonical']::attr(href)").get()
    news["title"] = selector.css("h1.entry-title::text").get().strip()
    news["timestamp"] = selector.css("li.meta-date::text").get()
    news["writer"] = selector.css("span.author a::text").get()
    news["reading_time"] = int(
        selector.css("li.meta-reading-time::text").get().split(" ")[0]
    )
    news["summary"] = "".join(
        selector.css("div.entry-content > p:first-of-type *::text").getall()
    ).strip()
    news["category"] = selector.css("span.label::text").get()
    return news


# Requisito 5
def scrape_all_news(url_list: list[str]) -> list[dict[str, int]]:
    news_list = []
    for url in url_list:
        news_content = fetch(url=url)
        if news_content:
            news_list.append(scrape_news(html_content=news_content))
    return news_list


def get_tech_news(amount: int) -> list[dict[str, int]]:
    url_list = []
    url = "https://blog.betrybe.com"
    while len(url_list) < amount:
        base_content = fetch(url=url)
        if base_content:
            url_list += scrape_updates(html_content=base_content)
            next_page_link = scrape_next_page_link(html_content=base_content)
            if next_page_link:
                url = next_page_link

    news_list = scrape_all_news(url_list=url_list[:amount])
    create_news(news_list)
    return news_list
