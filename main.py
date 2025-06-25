# importing modules.
from utils import load_contacts, save_contacts
from add_contact import add_contact
from view_contacts import view_contacts
from search_contact import search_contact
from remove_contact import remove_contact


# Greeting and Loading contacts.
print("Welcome to the Contact Book CLI System!")
contact_book = load_contacts()


# Menu function that displays options to the users.
def menu():
    while True:
        print(
            """=========== MENU ===========
1. Add Contact
2. View Contacts
3. Search Contact
4. Remove Contact
5. Exit
==========================="""
        )
        try:
            # Getting user input for the menu option
            user_input = int(input("Enter your choice: "))

            # Checking if the input is within the valid range
            if 1 <= user_input <= 5:
                if user_input == 1:
                    add_contact(contact_book)
                    save_contacts(contact_book)
                elif user_input == 2:
                    print("======= All Contacts =======")
                    # Here you would call the function to view contacts
                    view_contacts(contact_book)
                    print("=" * 28)
                elif user_input == 3:
                    # Here you would call the function to search for a contact
                    search_contact(contact_book)
                elif user_input == 4:
                    # Here you would call the function to remove a contact
                    remove_contact(contact_book)
                    save_contacts(contact_book)
                elif user_input == 5:
                    print("Thank you for using the Contact Book CLI System. Goodbye!")
                    break
            else:
                print("Invalid option, Please Enter 1 to 5")
                continue
        except ValueError:
            print("Invalid option, Please Enter 1 to 5")
            continue
        except KeyboardInterrupt:
            print("\nProgram terminated by user.")
            break


if __name__ == "__main__":
    menu()
