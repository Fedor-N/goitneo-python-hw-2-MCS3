def input_error(func):
    # - Exception handling
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Can't find the contact."
        except ValueError:
            return "Give me name and phone please!"
        except IndexError:
            return "No arguments."
    return inner


@input_error
def parse_input(user_input):
    # - parse input data.
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


@input_error
def add_contact(args, contacts):
    # - Create contact
    name, phone = args
    contacts[name] = phone
    return "Contact added."


@input_error
def show_phone(args, contacts):
    # - Show contact
    [name] = args
    if name in contacts:
        return f"{contacts[name]}"
    else:
        return f"Not found."


@input_error
def change_contact(args, contacts):
    # - Update contact
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return f"Contact updated."
    else:
        return f"Not found."


@input_error
def show_all(contacts):
    # - Show all contatcs
    if contacts:
        all_contacts = []
        for name, phone in contacts.items():
            all_contacts.append(f"{name}: {phone}")
        return "\n".join(all_contacts)
    else:
        return "No contacts stored."


def main():
    contacts = {}
    print("Welcome to the assistant bot!")

    while True:
        # Enter a command
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)  # Parse_input
        if command in ["close", "exit"]:
            print("Good bye!")
            break  # Exit
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))  # Add Contact
        elif command == "change":
            print(change_contact(args, contacts))  # Update Contac
        elif command == "phone":
            print(show_phone(args, contacts))  # Show phone Contact
        elif command == "all":
            print(show_all(contacts))  # Show All Contacts
        else:
            print("Invalid command.")


# Input point
if __name__ == "__main__":
    main()
