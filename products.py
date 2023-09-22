import database

PRODUCTS_MENU = """
1. Add
2. Remove
3. Update
4. Display all
x. Go Back
"""

def add_product():
    product_id = int(input('Please provide a product_id: '))
    print(product_id in database.products.keys())
    name = input('Please provide a name: ')
    manufacturer = input('Please provide a manufacturer: ')
    category = input('Please provide a category: ')
    price = float(input('Please provide a price: '))
    stock = int(input('Please provide a stock: '))
    product_info = {
        'name': name,
        'manufacturer': manufacturer,
        'category': category,
        'price': price,
        'stock': stock
    }
    database.products[product_id] = product_info
    print(f"{name} added successfully!")
