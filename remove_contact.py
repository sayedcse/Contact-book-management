# Function to remove a contact.
def remove_contact(contact_book):

    # Function to validate phone number
    def is_valid_phone(phone):
        return phone.isdigit() and len(phone) == 11

    while True:

        phone = input("Enter the phone number of the contact to delete: ").strip()
        if not is_valid_phone(phone):
            print("Phone number Must be 11 digits integer.")
            continue

        # Check if the phone number exists in the contact book
        if phone in contact_book:
            confirmed = (
                input(
                    f"Are you sure you want to delete contact numbers {phone}? (y/n):"
                )
                .strip()
                .lower()
            )
            # Confirm deletion
            if confirmed == "y":
                del contact_book[phone]
                print(f"Contact deleted successfully!")
                break
            elif confirmed == "n":
                print("Contact Deletion Canceled!!!")
                break
            else:
                print("Invalid input, Please enter Y/N")
        else:
            print("Phone Number not found!!!")
