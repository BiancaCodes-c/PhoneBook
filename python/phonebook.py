from typing import Dict, List, Optional


class PhoneBook:

    def __init__(self, phonebook_dict: Optional[Dict[str, List[str]]] = None):
        if phonebook_dict is None:
            self.phonebook = {}
        else:
            self.phonebook = phonebook_dict

    def add(self, name: str, phone_number: str) -> None:
        if name not in self.phonebook:
            self.phonebook[name] = []
        self.phonebook[name].append(phone_number)

    def add_all(self, name: str, *phone_numbers: str) -> None:
        if name not in self.phonebook:
            self.phonebook[name] = []

        for number in phone_numbers:
            self.phonebook[name].append(number)

    def remove(self, name: str) -> None:
        if name in self.phonebook:
            del self.phonebook[name]

    def has_entry(self, name: str, phone_number: str = None) -> bool:
        if name not in self.phonebook:
            return False

        if phone_number is None:
            return True

        return phone_number in self.phonebook[name]

    def lookup(self, name: str) -> List[str]:
        if name in self.phonebook:
            return self.phonebook[name]
        return []

    def reverse_lookup(self, phone_number: str) -> str:
        for name, numbers in self.phonebook.items():
            if phone_number in numbers:
                return name
        return None

    def get_all_contact_names(self) -> List[str]:
        return list(self.phonebook.keys())

    def get_map(self) -> Dict[str, List[str]]:
        return self.phonebook
    