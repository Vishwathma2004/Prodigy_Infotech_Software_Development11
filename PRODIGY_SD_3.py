class Contact:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

    def __str__(self):
        return f"Name: {self.name}, Phone: {self.phone}, Email: {self.email}"


class ContactManager:
    def __init__(self):
        self.contacts = []

    def add_contact(self):
        name = input("Enter contact name: ")
        phone = input("Enter contact phone number: ")
        email = input("Enter contact email address: ")
        new_contact = Contact(name, phone, email)
        self.contacts.append(new_contact)
        print("Contact added successfully.")

    def view_contacts(self):
        if not self.contacts:
            print("No contacts available.")
        else:
            for index, contact in enumerate(self.contacts, start=1):
                print(f"{index}. {contact}")

    def edit_contact(self):
        if not self.contacts:
            print("No contacts available to edit.")
            return

        self.view_contacts()
        try:
            contact_number = int(input("Select the contact number you want to edit: ")) - 1
            if contact_number < 0 or contact_number >= len(self.contacts):
                print("Invalid contact number.")
                return

            contact = self.contacts[contact_number]
            print(f"Editing contact: {contact}")

            new_name = input("Enter new name (press Enter to keep the current name): ")
            new_phone = input("Enter new phone (press Enter to keep the current phone): ")
            new_email = input("Enter new email (press Enter to keep the current email): ")

            if new_name:
                contact.name = new_name
            if new_phone:
                contact.phone = new_phone
            if new_email:
                contact.email = new_email

            print("Contact updated successfully.")
        except ValueError:
            print("Invalid input. Please enter a valid contact number.")

    def delete_contact(self):
        if not self.contacts:
            print("No contacts available to delete.")
            return

        self.view_contacts()
        try:
            contact_number = int(input("Select the contact number you want to delete: ")) - 1
            if contact_number < 0 or contact_number >= len(self.contacts):
                print("Invalid contact number.")
                return

            self.contacts.pop(contact_number)
            print("Contact deleted successfully.")
        except ValueError:
            print("Invalid input. Please enter a valid contact number.")

    def show_menu(self):
        while True:
            print("\n--- Contact Manager ---")
            print("1. Add Contact")
            print("2. View Contacts")
            print("3. Edit Contact")
            print("4. Delete Contact")
            print("5. Exit")

            try:
                choice = int(input("Choose an option: "))
                if choice == 1:
                    self.add_contact()
                elif choice == 2:
                    self.view_contacts()
                elif choice == 3:
                    self.edit_contact()
                elif choice == 4:
                    self.delete_contact()
                elif choice == 5:
                    print("Exiting...")
                    break
                else:
                    print("Invalid choice. Please select a valid option.")
            except ValueError:
                print("Invalid input. Please enter a number.")


if __name__ == "__main__":
    manager = ContactManager()
    manager.show_menu()
