from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

# 🔹 API 1: Fake Store
def get_fake_store_products(query):
    url = "https://fakestoreapi.com/products"
    res = requests.get(url).json()

    results = []
    for item in res:
        if query.lower() in item['title'].lower():
            results.append({
                "site": "FakeStore",
                "title": item["title"],
                "price": float(item["price"]),
                "link": item["image"]
            })
    return results


# 🔹 API 2: Dummy JSON Store
def get_dummy_products(query):
    url = "https://dummyjson.com/products/search?q=" + query
    res = requests.get(url).json()

    results = []
    for item in res["products"]:
        results.append({
            "site": "DummyStore",
            "title": item["title"],
            "price": float(item["price"]),
            "link": item["thumbnail"]
        })
    return results


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/search")
def search():
    query = request.args.get("product")

    results = []
    results += get_fake_store_products(query)
    results += get_dummy_products(query)

    # Sort by lowest price
    results = sorted(results, key=lambda x: x["price"])

    return jsonify(results)


if __name__ == "__main__":
    app.run(debug=True)