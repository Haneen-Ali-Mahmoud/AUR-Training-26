from abc import ABC, abstractmethod
from enum import Enum

class item_status (Enum):
    AVAILABLE = "AVAILABLE"
    CHECKED_OUT = "CHECKED_OUT"
    LOST = "LOST"

class library_items (ABC):
    def __init__(self, title, status):
        self._title = title
        self._status = status

    @property
    def title(self):
        return self._title

    @title.setter
    def title (self, title):
        self._title = title

    @property
    def status(self):
        return self._status

    @abstractmethod
    def loan_period(self):
        pass

    def checkout(self):
        if self._status == item_status.CHECKED_OUT:
            raise ValueError("item is Checked out")
        if self._status == item_status.LOST:
            raise ValueError("item is LOST")
        self._status = item_status.CHECKED_OUT

    def return_item(self):
        if self._status == item_status.CHECKED_OUT:
            self._status = item_status.AVAILABLE
        else :
            raise ValueError("It wasn't Checked out")

    def mark_lost(self):
        if self._status == item_status.LOST:
            raise ValueError("Item is already lost")
        self._status = item_status.LOST

    def __str__ (self):
        return f"Type: {self.__class__.__name__}- Title: {self._title}- Status: {self._status.value}"
    def __lt__ (self, other):
         return self.title < other.title
    def __repr__ (self):
         return f"{self.__class__.__name__} (Title: {self._title} , Status: {self._status.value})"
    
    @classmethod
    def from_dict(cls, data):
        item_type = data["type"].lower()

        Items = ItemType.get(item_type)
        if Items is None:
           raise ValueError("Unknown item type")
    
        return Items.from_dict(data)


    @staticmethod
    def validate_isbn(isbn):
        if not isbn.isdigit() or len(isbn) !=13:
             return False
        total = 0
        for i in range(12):
            if i % 2 ==0:
                total += int(isbn[i]) * 1
            else:
                total += int(isbn[i]) * 3

        check_digit = (10 - (total % 10)) % 10
        return check_digit == int(isbn[12])


class Book (library_items):
    def __init__ (self, title, author, isbn, status):
        super().__init__(title, status)
        self.author = author
        self.isbn = isbn

    def loan_period(self):
        return 21
    @classmethod
    def from_dict(cls, data):
        return cls(
            data["title"],
            data["author"],
            data["isbn"],
            item_status[data["status"]]
    )
    def to_dict(self):
        return {
            "type": "Book",
            "title": self.title,
            "author": self.author,
            "isbn": self.isbn,
           "status": self.status.name
           }
    
class DVD (library_items):
    def __init__(self, title, director, status):
        super().__init__(title, status)
        self.director = director

    def loan_period(self):
        return 5
    @classmethod
    def from_dict(cls, data):
         return cls(
             data["title"],
            data["director"],
            item_status[data["status"]]
        )
    def to_dict(self):
        return {
           "type": "DVD",
           "title": self.title,
           "director": self.director,
           "status": self.status.name
           }

class Magazine(library_items):
    def __init__(self, title, issue, status):
        super().__init__(title, status)
        self.issue = issue

    def loan_period(self):
        return 14

    @classmethod
    def from_dict(cls, data):
      return cls(
         data["title"],
         data["issue"],
         item_status[data["status"]]
        )
    def to_dict(self):
        return {
            "type": "Magazine",
            "title": self.title,
            "issue": self.issue,
            "status": self.status.name}
    
ItemType = {
"book": Book,
"dvd": DVD,
"magazine": Magazine}



class library:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def find_by_title(self, title):
        for item in self.items:
            if item.title.lower() == title.lower():
                return item
        return None

    def list_available(self):
        available_items =[]
        for item in self.items:
            if item.status == item_status.AVAILABLE:
                available_items.append(item)
        return available_items
    
    def checkout (self, title):
        found = self.find_by_title(title)
        if found is None:
            raise ValueError("Title not found")
        found.checkout()

    def return_item(self, title):
        found = self.find_by_title(title)
        if found is None:
             raise ValueError("Title not found")
        found.return_item()

    def mark_lost(self, title):
         found = self.find_by_title(title)
         if found is None:
                 raise ValueError("Title not found")
         found.mark_lost()
