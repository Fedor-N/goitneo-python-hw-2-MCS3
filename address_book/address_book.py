from collections import UserDict

# - main classes


class Field:
    # - Base class for record fields.
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    # - A class for storing a contact name. Mandatory field.
    def __init__(self, name):
        super().__init__(name)


class Phone(Field):
    # - A class for storing a phone number. Has format validation (10 digits).
    def __init__(self, phone):
        super().__init__(phone)

    def validate(self):
        # - validation
        if len(self.value) == 10 and self.value.isdigit():
            return True
        else:
            raise ValueError("The phone number must consist of 10 digits")


class Record:
    # - A class for storing information about a contact, including name and phone list.
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def find_phone(self, phone_number):
        # - Phone search
        for phone in self.phones:
            if phone.value == phone_number:
                return phone
        return None

    def add_phone(self, phone_number):
        # - Adding phones
        phone = Phone(phone_number)
        if phone.validate():
            self.phones.append(phone)

    def remove_phone(self, phone_number):
        # - Deleting phones
        for phone in self.phones:
            if phone.value == phone_number:
                self.phones.remove(phone)
                return True
        return False

    def edit_phone(self, old_number, new_number):
        # - Editing phones
        for phone in self.phones:
            if phone.value == old_number:
                phone.value = new_number
                return True
        return False

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"


class AddressBook(UserDict):
    def add_record(self, record):
        # - Adding records
        if isinstance(record, Record):
            self.data[record.name.value] = record

    def find(self, name):
        # - Search records by name
        return self.data.get(name)

    def delete(self, name):
        # - Deleting records by name
        if name in self.data:
            del self.data[name]


def main():
    # - The main function
    # Створення нової адресної книги
    book = AddressBook()

    # Створення запису для John
    john_record = Record("John")
    john_record.add_phone("1234567890")
    john_record.add_phone("5555555555")

    # Додавання запису John до адресної книги
    book.add_record(john_record)

    # Створення та додавання нового запису для Jane
    jane_record = Record("Jane")
    jane_record.add_phone("9876543210")
    book.add_record(jane_record)

    # Виведення всіх записів у книзі
    for name, record in book.data.items():
        print(record)
        print("-----")

    # Знаходження та редагування телефону для John
    john = book.find("John")
    john.edit_phone("1234567890", "1112223333")

    print(john)  # Виведення: Contact name: John, phones: 1112223333; 5555555555
    print("=====")

    # Пошук конкретного телефону у записі John
    found_phone = john.find_phone("5555555555")
    print(f"{john.name}: {found_phone}")  # Виведення: 5555555555
    print("+++++")

    # Видалення запису Jane
    book.delete("Jane")


# Точка входу
if __name__ == "__main__":
    main()
