import requests

def get_products(initial_product):
    url = f"https://fr.openfoodfacts.org/cgi/search.pl?search_terms={initial_product}&search_simple=1&json=1"
    request = requests.get(url)
    data = request.json()
    if data.get("count",0) == 0:
        return None
    product = data.get("products")[0]
    return product.get("categories")


if __name__ == "__main__":
    print(get_products("coke"))