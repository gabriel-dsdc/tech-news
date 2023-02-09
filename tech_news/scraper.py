# Requisito 1
import time
import requests
from parsel import Selector


HTML = str


def fetch(url: str) -> HTML | None:
    try:
        response = requests.get(
            url,
            timeout=3,
            headers={"user-agent": "Fake user-agent"})
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
def scrape_news(html_content: HTML) -> str:
    news = {}
    selector = Selector(text=html_content)
    news["url"] = selector.css("link[rel='canonical']::attr(href)").get()
    news["title"] = selector.css("h1.entry-title::text").get().strip()
    news["timestamp"] = selector.css("li.meta-date::text").get()
    news["writer"] = selector.css("span.author a::text").get()
    news["reading_time"] = int(
        selector.css("li.meta-reading-time::text").get().split(" ")[0])
    news["summary"] = "".join(selector.css(
        "div.entry-content > p:first-of-type *::text").getall()).strip()
    news["category"] = selector.css("span.label::text").get()
    return news


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
