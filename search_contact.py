# Function to search for a contact
def search_contact(contact_book):

    # Empty contact validate
    if not contact_book:
        print("Contact List Empty!!!")
        return
    # Taking user input for search term
    search_term = input("Enter search term (name/email/phone): ").strip().lower()

    matched = []  # List to store matched contacts

    # Looping through Contact dictionary to find matches
    for phone, info in contact_book.items():
        if (
            search_term in phone.lower()
            or search_term in info["name"].lower()
            or search_term in info["email"].lower()
        ):
            matched.append((phone, info))  # Append matched contacts to the list

    # If matches found, print them
    if matched:
        print(f"Search Result:")
        for index, (phone, info) in enumerate(matched, 1):
            print(
                f"""{index}. Name: {info["name"]}
Phone: {phone}
Email: {info["email"]}
Address: {info["address"]}
"""
            )
    else:
        print("No matching contact found!!!")
