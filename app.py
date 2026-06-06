from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

# 🔹 Dummy API (works)
def get_dummy_products(query):
    url = f"https://dummyjson.com/products/search?q={query}"
    res = requests.get(url).json()

    results = []
    for item in res["products"]:
        results.append({
            "site": "Global Store",
            "title": item["title"],
            "price": float(item["price"]),
            "image": item["thumbnail"],
            "link": "#"
        })
    return results


# 🔹 RapidAPI Example (optional real API)
def get_rapidapi_products(query):
    url = "https://real-time-product-search.p.rapidapi.com/search"

    headers = {
        "X-RapidAPI-Key": "YOUR_API_KEY",
        "X-RapidAPI-Host": "real-time-product-search.p.rapidapi.com"
    }

    params = {"q": query, "country": "in"}

    try:
        res = requests.get(url, headers=headers, params=params).json()

        results = []
        for item in res.get("data", [])[:5]:
            results.append({
                "site": item.get("source", "Store"),
                "title": item.get("title"),
                "price": float(item.get("price", 0)),
                "image": item.get("product_photo"),
                "link": item.get("product_page_url")
            })
        return results

    except:
        return []


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/search")
def search():
    query = request.args.get("product")

    results = []
    results += get_dummy_products(query)

    # Uncomment after adding API key
    # results += get_rapidapi_products(query)

    results = [r for r in results if r["price"] > 0]

    results = sorted(results, key=lambda x: x["price"])

    return jsonify(results)


if __name__ == "__main__":
    app.run(debug=True)
