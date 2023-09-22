import database
import products


MAIN_MENU = """
1. Products
2. Clients
3. Transactions
4. Reports
x. Exit
"""

while True:
    print(MAIN_MENU)

    option = input('Select an option from the menu: ').lower()

    match option:
        case '1':
            display_second_menu = True
            while display_second_menu:
                print(products.PRODUCTS_MENU)
                option = input('Select an option from the product menu: ').lower()

                match option:
                    case '1':
                        products.add_product()
                    case '2':
                        products.remove_product()
                    case '3':
                        print('Update')
                    case '4':
                        print(database.products)
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