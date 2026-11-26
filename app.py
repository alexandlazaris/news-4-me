from flask import Flask, render_template
from service import get_custom_news

app = Flask(__name__)


@app.route("/")
def home():
    get_tech_news = get_custom_news(
        endpoint="everything",
        params={
            "sources": "the-verge,techcrunch",
            "q": "programming OR gaming",
            "language": "en",
            "pageSize": 10,
        },
    )

    get_sports_news = get_custom_news(
        endpoint="everything",
        params={
            "q": '"EPL" OR "Champions League"',
            "sortBy": "publishedAt",
            "language": "en",
            "pageSize": 10,
        },
    )

    get_eu_news = get_custom_news(
        endpoint="everything",
        params={
            "q": '"greece history" OR "greek dancing" OR "Peloponnese"',
            "sortBy": "publishedAt",
            "language": "en",
            "pageSize": 10,
        },
    )

    get_dinosaur_news = get_custom_news(
        endpoint="everything",
        params={
            "q": '"dinosaur bones" OR "dinosaur fossils" OR "fossils" OR "prehistoric"',
            "domains": (
                "nature.com,"
                "sciencenews.org,"
                "smithsonianmag.com,"
                "livescience.com,"
                "theguardian.com,"
                "abc.net.au"
            ),
            "language": "en",
            "sortBy": "publishedAt",
            "pageSize": 10,
        },
    )

    results_tech = get_tech_news.get("articles", [])
    results_sports = get_sports_news.get("articles", [])
    results_eu = get_eu_news.get("articles", [])
    results_dinosaurs = get_dinosaur_news.get("articles", [])
    return render_template(
        "index.html",
        results_tech=results_tech,
        results_sports=results_sports,
        results_eu=results_eu,
        results_dinosaurs=results_dinosaurs,
    )


if __name__ == "__main__":
    app.run(debug=False)
