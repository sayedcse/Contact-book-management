# Importing Regular Expression for validate data.
import re


# Function to add contact
def add_contact(contact_book):

    # Validator function for name phone & email.
    def is_valid_name(name):
        pattern = r"^[A-Za-z\s]+$"
        return re.match(pattern, name)

    def is_valid_phone(phone):
        return phone.isdigit() and len(phone) == 11

    def is_valid_email(email):
        pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
        return re.match(pattern, email)

    # Taking user input with a helper function
    def get_contact_info(existing_phone):

        # Looping for invalid input
        while True:
            # name input
            name = input("Enter Name: ").strip()
            if not is_valid_name(name):
                print("The contact’s name must be a string!")
                continue

            # Phone number input
            phone = input("Enter Phone Number: ").strip()
            if phone in existing_phone:
                print("Error: Phone number already exists for another contact!")
                continue
            if not is_valid_phone(phone):
                print("Phone number Must be exactly 11 digits!")
                continue
            #
            #  Email input with validation
            email = input("Enter Email: ").strip()
            if not is_valid_email(email):
                print("Invalid Email Format!!! Try again.")
                continue

            # Address input
            address = input("Enter Address: ").strip()

            return {"name": name, "phone": phone, "email": email, "address": address}

    # Calling the func & Storing return values
    new_contact = get_contact_info(existing_phone=contact_book.keys())

    contact_book[new_contact["phone"]] = {
        "name": new_contact["name"],
        "email": new_contact["email"],
        "address": new_contact["address"],
    }
    # Printing Success msg.
    print("Contacts added successfully!!!")
