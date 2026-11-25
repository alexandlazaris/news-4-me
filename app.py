from flask import Flask, render_template
from service import get_news, get_all_categories_news

app = Flask(__name__)

@app.route("/")
def home():
    response = get_all_categories_news()
    response.raise_for_status()

    data = response.json()
    results = data.get("articles", [])

    return render_template(
        "index.html",
        results=results
    )

if __name__ == "__main__":
    app.run(debug=True)