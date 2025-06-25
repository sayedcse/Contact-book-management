# View contact function.
def view_contacts(contact_book):

    # Empty contact validate
    if not contact_book:
        print("Contact List Empty!!!")
        return
    # Looping through Contact dictionary & enumerate func for index.
    for index, (phone, info) in enumerate(contact_book.items(), 1):
        # Prints values given format
        print(
            f"""{index}. Name: {info["name"]}
Phone: {phone}
Email: {info["email"]}
Address: {info["address"]}
"""
        )
