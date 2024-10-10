import json

def fetch_product_info():
    try:
        with open('products.json', 'r') as file:
            products = json.load(file)
            return process_product_data(products)
    except json.JSONDecodeError as e:
        print(f"Error reading JSON file: {e}")
        return None
    except FileNotFoundError:
        print("products.json file not found.")
        return None

def process_product_data(products):
    product_list = []
    for product in products:
        product_info = f"{product['name']}: {product['description']} - Price: {product['price']}"
        product_list.append(product_info)
    return product_list if product_list else None
