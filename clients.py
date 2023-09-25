import database

CLIENTS_MENU = """
1. Add
2. Remove
3. Update
4. Display all
x. Go Back
"""

def add_client():
    client_id = int(input('Please provide a client_id: '))
    print(client_id in database.clients.keys())
    last_name = input('Last name: ')
    first_name = input('First name: ')
    date_of_birth = input('Date of birth (dd/mm/yyyy): ')
    email = input('Email address: ')
    client_info = {
        'last_name': last_name,
        'first_name': first_name,
        'date_of_birth': date_of_birth,
        'email': email,
    }
    database.clients[client_id] = client_info
    print(f"{first_name} added successfully!")

def remove_client():
    client_id = int(input('Please provide a client_id: '))
    temp_name = database.clients[client_id]['last_name']
    del database.clients[client_id]
    print(f"{temp_name} removed successfully!")

def update_client():
    client_id = int(input("Please select a client to update: "))
    print(database.clients[client_id])
    update_input = input("Please select what you want to update and the new value:")
    update_values = update_input.split()
    update_key = update_values[0]
    update_value = update_values[1]
    database.clients[client_id][update_key] = update_value
    print(database.clients[client_id])
    print(f"{update_key} successfully updated!")