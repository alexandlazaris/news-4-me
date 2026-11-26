from dotenv import load_dotenv
import requests
import os

load_dotenv()
API_KEY = os.getenv("API_KEY")


def get_custom_news(
    category: str = None, params: dict = None, endpoint: str = "top-headlines"
):
    """
    Get news using args
    """
    combined_params = {}
    if category:
        combined_params["category"] = category
    if params:
        combined_params.update(params)

    base_url = "https://newsapi.org/v2/"

    headers = {"Authorization": API_KEY}
    try:
        response = requests.get(
            base_url + endpoint,
            params=combined_params,
            headers=headers,
            timeout=(3, 10),
        )

        response.raise_for_status()
        return response.json()
    except requests.Timeout:
        print("NewsAPI request timed out")
        return {"articles": []}

    except requests.RequestException:
        print("NewsAPI request failed")
        return {"articles": []}
