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

def remove_product():
    product_id = int(input('Please provide a product_id: '))
    temp_name = database.products[product_id]['name']
    del database.products[product_id]
    print(f"{temp_name} removed successfully!")

def update_product():
    product_id = int(input("Please select a product to update: "))
    print(database.products[product_id])
    update_input = input("Please select what you want to update and the new value:")
    update_values = update_input.split()
    update_key = update_values[0]
    update_value = update_values[1]
    database.products[product_id][update_key] = update_value
    print(database.products[product_id])
    print(f"{update_key} successfully updated!")