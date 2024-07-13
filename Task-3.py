# CONTACT MANAGEMENT SYSTEM

import pandas as pd

def add_contact(name, phone, email):
    contact = {'Name': name, 'Phone': phone, 'Email': email}
    df = pd.DataFrame(contact, index=[0])
    
    try:
        existing_contacts = pd.read_excel('contacts.xlsx')
        df = pd.concat([existing_contacts, df], ignore_index=True)
    except FileNotFoundError:
        pass
    
    df.to_excel('contacts.xlsx', index=False)
    print("Contact added successfully!")

def update_contact(name, new_phone, new_email):
    df = pd.read_excel('contacts.xlsx')
    df.loc[df['Name'] == name, ['Phone', 'Email']] = new_phone, new_email
    df.to_excel('contacts.xlsx', index=False, header=True)

def delete_contact(name):
    df = pd.read_excel('contacts.xlsx')
    df = df[df['Name'] != name]
    df.to_excel('contacts.xlsx', index=False, header=True)

def display_contacts():
    try:
        contacts = pd.read_excel('contacts.xlsx')
        print(contacts)
    except FileNotFoundError:
        print("No contacts found.")

while True:
    print("\nContact Management System")
    print("1. Add Contact")
    print("2. Update Contact")
    print("3. Delete Contact")
    print("4. Display Contacts")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        name = input("Enter Name: ")
        phone = input("Enter Phone: ")
        email = input("Enter Email: ")
        add_contact(name, phone, email)

    elif choice == '2':
        name = input("Enter Name to update: ")
        new_phone = input("Enter New Phone: ")
        new_email = input("Enter New Email: ")
        update_contact(name, new_phone, new_email)
        print("Contact updated successfully!")

    elif choice == '3':
        name = input("Enter Name to delete: ")
        delete_contact(name)
        print("Contact deleted successfully!")

    elif choice == '4':
        display_contacts()

    elif choice == '5':
        print("Exiting Contact Management System. Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")
