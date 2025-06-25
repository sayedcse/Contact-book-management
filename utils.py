import json


# Function to load contacts from a JSON file
def load_contacts():
    try:
        # Read contacts from a JSON file
        with open("contacts.json", "r", encoding="utf-8") as file:
            contact_book = json.load(file)
            print("Contacts loaded successfully.")
            return contact_book

    #  Handle the case where the file does not exist
    except FileNotFoundError:
        print("No contacts found. Starting with an empty contact book.")
        return {}
    except json.JSONDecodeError:
        print(
            """"Error: contacts.json is not a valid JSON file.
            Starting with an empty contact book."""
        )
        return {}


# Function to save contacts to a JSON file
def save_contacts(contact_book):
    try:
        # Write contact book to a JSON file
        with open("contacts.json", "w", encoding="utf-8") as file:
            json.dump(
                contact_book,
                file,
                indent=4,
            )
    except Exception as e:
        print(f"Error saving contacts: {e}")
