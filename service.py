from dotenv import load_dotenv
import requests
import os

load_dotenv()
API_KEY = os.getenv("API_KEY")

def get_news():
    """
    Get top headlines for tech news
    """
    query_params = {
        "category": "technology",
        "pageSize": "5",
        "to": "2026-11-20",
        "searchIn": "title, content, description",
    }

    headers = {"Authorization": API_KEY}

    base_url = "https://newsapi.org/v2/"
    path_top_headlines = "top-headlines"

    response = requests.get(
        base_url + path_top_headlines, params=query_params, headers=headers
    )
    return response


def get_all_categories_news():
    """
    Fetch news from multiple categories
    """
    query_params = {
        # wired-de
        # the-sport-bible
        # "techcrunch-cn",
        # "techradar",
        # "recode",
        # "new-scientist",
        # "national-geographic"
        # "ign"
        "sources": "the-sport-bible",
        "pageSize": "20",
        # "to": "2026-11-20",
    }

    headers = {"Authorization": API_KEY}

    base_url = "https://newsapi.org/v2/"
    path_top_headlines = "top-headlines"

    response = requests.get(
        base_url + path_top_headlines, params=query_params, headers=headers
    )
    return response

# TODO: convert desired url path to be interchangeable, cut down duplication