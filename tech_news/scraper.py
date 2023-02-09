# Requisito 1
import time
import requests
from parsel import Selector


HTML = str


def fetch(url: str):
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
def scrape_updates(html_content: HTML):
    selector = Selector(text=html_content)
    articles = selector.css(".entry-title a::attr(href)").getall()
    if articles:
        return articles
    return []


# Requisito 3
def scrape_next_page_link(html_content: HTML):
    selector = Selector(text=html_content)
    next_link = selector.css("a.next::attr(href)").get()
    if next_link:
        return next_link
    return None


# Requisito 4
def scrape_news(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
