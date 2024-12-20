import json

def add_contact():
    name = input("Enter name: ")
    phone_number = input("Enter phone number: ")
    email = input("Enter email: ")
    address = input("Enter address: ")
    contacts[name] = {"phone_number": phone_number, "email": email, "address": address}
    save_contacts()
    print("Contact added successfully!")

def view_contacts():
    if not contacts:
        print("No contacts found.")
    else:
        for name, details in contacts.items():
            print(f"Name: {name}")
            print(f"Phone Number: {details['phone_number']}")
            print(f"Email: {details['email']}")
            print(f"Address: {details['address']}")
            print()

def search_contact():
    query = input("Enter name or phone number to search: ")
    found = False
    for name, details in contacts.items():
        if query in name or query in details['phone_number']:
            print(f"Name: {name}")
            print(f"Phone Number: {details['phone_number']}")
            print(f"Email: {details['email']}")
            print(f"Address: {details['address']}")
            found = True
    if not found:
        print("Contact not found.")

def update_contact():
    name = input("Enter name of contact to update: ")
    if name in contacts:
        print("Enter new details:")
        new_phone_number = input("New phone number (press Enter to keep current): ")
        new_email = input("New email (press Enter to keep current): ")
        new_address = input("New address (press Enter to keep current): ")
        if new_phone_number:
            contacts[name]['phone_number'] = new_phone_number
        if new_email:
            contacts[name]['email'] = new_email
        if new_address:
            contacts[name]['address'] = new_address
        save_contacts()
        print("Contact updated successfully!")
    else:
        print("Contact not found.")

def delete_contact():
    name = input("Enter name of contact to delete: ")
    if name in contacts:
        del contacts[name]
        save_contacts()
        print("Contact deleted successfully!")
    else:
        print("Contact not found.")

def save_contacts():
    with open('contacts.json', 'w') as f:
        json.dump(contacts, f)

def load_contacts():
    global contacts
    try:
        with open('contacts.json', 'r') as f:
            contacts = json.load(f)
    except FileNotFoundError:
        contacts = {}

load_contacts()

while True:
    print("\nContact Management System")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        add_contact()
    elif choice == '2':
        view_contacts()
    elif choice == '3':
        search_contact()
    elif choice == '4':
        update_contact()
    elif choice == '5':
        delete_contact()
    elif choice == '6':
        break
    else:
        print("Invalid choice. Please try again.")