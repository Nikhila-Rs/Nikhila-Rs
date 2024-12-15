import json
import os

class Contact:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

    def to_dict(self):
        return {
            'name': self.name,
            'phone': self.phone,
            'email': self.email
        }

    @staticmethod
    def from_dict(data):
        return Contact(data['name'], data['phone'], data['email'])

class ContactManager:
    def __init__(self, filename='contacts.json'):
        self.filename = filename
        self.contacts = self.load_contacts()

    def load_contacts(self):
        """Load contacts from a JSON file."""
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as file:
                return [Contact.from_dict(contact) for contact in json.load(file)]
        return []

    def save_contacts(self):
        """Save contacts to a JSON file."""
        with open(self.filename, 'w') as file:
            json.dump([contact.to_dict() for contact in self.contacts], file)

    def add_contact(self, name, phone, email):
        """Add a new contact."""
        new_contact = Contact(name, phone, email)
        self.contacts.append(new_contact)
        self.save_contacts()
        print(f'Contact "{name}" added.')

    def view_contacts(self):
        """Display all contacts."""
        if not self.contacts:
            print("No contacts available.")
        else:
            print("Your Contacts:")
            for index, contact in enumerate(self.contacts, start=1):
                print(f"{index}. Name: {contact.name}, Phone: {contact.phone}, Email: {contact.email}")

    def update_contact(self, index, name, phone, email):
        """Update an existing contact."""
        if 0 <= index < len(self.contacts):
            self.contacts[index].name = name
            self.contacts[index].phone = phone
            self.contacts[index].email = email
            self.save_contacts()
            print(f'Contact "{name}" updated.')
        else:
            print("Invalid contact number.")

    def delete_contact(self, index):
        """Delete a contact."""
        if 0 <= index < len(self.contacts):
            removed_contact = self.contacts.pop(index)
            self.save_contacts()
            print(f'Contact "{removed_contact.name}" deleted.')
        else:
            print("Invalid contact number.")

def main():
    contact_manager = ContactManager()

    while True:
        print("\nContact Management Menu:")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Update Contact")
        print("4. Delete Contact")
        print("5. Exit")
        
        choice = input("Choose an option (1-5): ")

        if choice == '1':
            name = input("Enter name: ")
            phone = input("Enter phone: ")
            email = input("Enter email: ")
            contact_manager.add_contact(name, phone, email)
        elif choice == '2':
            contact_manager.view_contacts()
        elif choice == '3':
            contact_manager.view_contacts()
            contact_number = int(input("Enter the contact number to update: ")) - 1
            name = input("Enter new name: ")
            phone = input("Enter new phone: ")
            email = input("Enter new email: ")
            contact_manager.update_contact(contact_number, name, phone, email)
        elif choice == '4':
            contact_manager.view_contacts()
            contact_number = int(input("Enter the contact number to delete: ")) - 1
            contact_manager.delete_contact(contact_number)
        elif choice == '5':
            print("Exiting the Contact Management application.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
