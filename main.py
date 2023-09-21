MAIN_MENU = """
1. Products
2. Clients
3. Transactions
4. Reports
x. Exit
"""

PRODUCTS_MENU = """
1. Add
2. Remove
3. Update
4. Display all
x. Go Back
"""

products = {
    1: {
        'name': 'Banana',
        'manufacturer': 'Guatemala',
        'category': 'Fruit',
        'price': 1,
        'stock': 500
    },
    2: {
        'name': 'Kiwi',
        'manufacturer': 'Ecuador',
        'category': 'Fruit',
        'price': 2,
        'stock': 234
    }
}

clients = {
    1: {
        'last_name': 'Doe',
        'first_name': 'John',
        'date_of_birth': '26/04/1965',
        'email': 'john.doe@test.com'
    }
}


def add_product():
    product_id = int(input('Please provide a product_id: '))
    print(product_id in products.keys())
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
    products[product_id] = product_info
    print(f"{name} added successfully!")


while True:
    print(MAIN_MENU)

    option = input('Select an option from the menu: ').lower()

    match option:
        case '1':
            display_second_menu = True
            while display_second_menu:
                print(PRODUCTS_MENU)
                option = input('Select an option from the product menu: ').lower()

                match option:
                    case '1':
                        add_product()
                    case '2':
                        print('Remove')
                    case '3':
                        print('Update')
                    case '4':
                        print(products)
                    case 'x':
                        print('Back')
                        display_second_menu = False
                    case _:
                        print('No such option!')

        case '2':
            print('Client')
        case '3':
            print('Transactions')
        case '4':
            print('Reports')
        case 'x':
            print('Exiting')
            break
        case _:
            print('No such option!')