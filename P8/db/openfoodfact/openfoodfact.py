import requests

def get_products(initial_product):
    url = f"https://fr.openfoodfacts.org/cgi/search.pl?search_terms={initial_product}&search_simple=1&json=1"
    request = requests.get(url)
    data = request.json()
    if data.get("count",0) == 0:
        return None
    product = data.get("products")[0]
    return product.get("categories")

def get_products_by_category(category):
    url = f"https://fr.openfoodfacts.org/category/{category}&json=1"
    request = requests.get(url)
    data = request.json()
    if data.get("count",0) == 0:
        return None
    results = []
    products = data.get("products")[:6]
    for product in products:
        p = {'nutriscore':product.get("nutriscore_grade","e"), 'name':product.get("product_name","produit indisponible"),
             'image':product.get("image_url","")}
        results.append(p)
    return results

if __name__ == "__main__":
    print(get_products("coke"))
    print(get_products_by_category("boissons"))

