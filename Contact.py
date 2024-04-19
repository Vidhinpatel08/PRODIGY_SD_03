"""
    Task 3: Simple Contact Management System

    Build a program to store and manage contact information.
    Allow users to:
        1. Add new contacts (name, phone number, email).
        2. View the contact list.
        3. Edit existing contacts.
        4. Delete contacts.
    Implement data persistence using memory or a file.
"""
##################################################################################################################


class Contact:
    def __init__(self, firstName, lastName, phone, email):
        """Constructor that executes when an object of the Contact class is created."""
        self.firstName = firstName
        self.lastName = lastName
        self.phone = phone
        self.email = email

    def view_contact(self):
        """Returns a formatted string representing the contact's details."""
        return f"""
    Name:  {self.firstName} {self.lastName}
    Phone: {self.phone}
    Email: {self.email}
------------------------------------------------------------------------
"""

    def update_contact(self):
        """Prompts user for new information and updates the contact details."""
        self.firstName = input("Enter new first name (or press Enter to keep existing): ").strip().lower() or self.firstName
        self.lastName = input("Enter new last name (or press Enter to keep existing): ").strip().lower() or self.lastName
        self.phone = input("Enter new phone number (or press Enter to keep existing): ").strip() or self.phone
        self.email = input("Enter new email (or press Enter to keep existing): ").strip().lower() or self.email

    def delete_contact(self):
        """Sets all contact information to empty strings."""
        self.firstName = ""
        self.lastName = ""
        self.phone = ""
        self.email = ""


class ContactManager:
    def __init__(self, filename="contacts.txt"):
        """Initializes a new ContactManager object."""
        self.filename = filename
        self.contacts = self.load_contacts()

    def load_contacts(self):
        """Loads contact information from the specified file into a list of Contact objects."""
        contacts = []
        try:
            with open(self.filename, "r") as file:
                for line in file:
                    name, phone, email = line.strip().split(",")
                    firstName, lastName = name.split()
                    contacts.append(Contact(firstName, lastName, phone, email))
        except FileNotFoundError:
            # Create an empty file if it doesn't exist
            with open(self.filename, "w") as file:
                pass
        return contacts

    def save_contacts(self):
        """Saves the list of contacts from the ContactManager object to the specified file."""
        try:
            with open(self.filename, "w") as file:
                for contact in self.contacts:
                    file.write(f"{contact.firstName} {contact.lastName},{contact.phone},{contact.email}\n")
        except Exception as e:
            print(f"An error occurred while saving contacts: {e}")

    def add_contact(self):
        """Adds a new contact to the contact list."""
        print("\n** Add New Contact **")
        firstName = input("Enter first name: ").strip().lower()
        lastName = input("Enter last name: ").strip().lower()
        phone = input("Enter phone number: ").strip()
        email = input("Enter email: ").strip().lower()
        new_contact = Contact(firstName, lastName, phone, email)
        self.contacts.append(new_contact)
        self.save_contacts()
        print("Contact added successfully!")

    def view_contacts(self):
        """Displays all contacts in the contact list."""
        if not self.contacts:
            print("No contacts found.\n")
            return

        print("\n** Contact List **\n")
        for index, contact in enumerate(self.contacts):
            print(f"{index+1}. {contact.view_contact()}")

    def edit_contact(self):
        """Edits an existing contact in the contact list."""
        self.view_contacts()  

        while True:
            index = int(input("\nEnter the index of the contact to edit (or -1 to cancel): "))
            if index < -1 or (index-1) >= len(self.contacts):
                print("Invalid contact index. Please try again.")
            elif index == -1:
                break  # Exit edit loop if user cancels
            else:
                print(f"\n** Edit Contact (Index: {index})**")
                self.contacts[index-1].update_contact()
                self.save_contacts()
                print("Contact updated successfully!")
                break  # Exit edit loop after successful update

    def delete_contact(self):
        """Deletes a contact from the contact list."""
        self.view_contacts()  

        while True:
            index = int(input("\nEnter the index of the contact to delete (or -1 to cancel): "))
            if index < -1 or (index-1) >= len(self.contacts):
                print("Invalid contact index. Please try again.")
            elif index == -1:
                break  # Exit delete loop if user cancels
            else:
                confirmation = input(f"Are you sure you want to delete contact {index}? (y/n): ").strip().lower()
                if confirmation.lower() == "y" or 'yes' or '1':
                    del self.contacts[index-1]
                    self.save_contacts()
                    print("Contact deleted successfully!")
                    break  # Exit delete loop after successful deletion
                else:
                    print("Deletion cancelled.")

    def run(self):
        while True:
            print("\n** Contact Management System **")
            print("1. Add Contact")
            print("2. View Contacts")
            print("3. Edit Contact")
            print("4. Delete Contact")
            print("5. Exit")

            choice = input("Enter your choice: ").strip().lower()

            if choice == "1":
                self.add_contact()
            elif choice == "2":
                self.view_contacts()
            elif choice == "3":
                self.edit_contact()
            elif choice == "4":
                self.delete_contact()
            elif choice == "5":
                self.save_contacts()
                print("Exiting Contact Management System...")
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    manager = ContactManager()
    manager.run()
