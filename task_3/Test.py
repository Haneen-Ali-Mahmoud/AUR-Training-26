from library import Book, DVD, Magazine, item_status
from main import main

book = Book(
    "Dune",
    "Frank Herbert",
    "9780441013593",
    item_status.AVAILABLE
)

dvd = DVD(
    "Inception",
    "Christopher Nolan",
    item_status.CHECKED_OUT
)

magazine = Magazine(
    "National Geographic",
    "2026-08",
    item_status.AVAILABLE
)

items = [book, dvd, magazine]

db = main()

db.save(items)

print("Saved successfully!")

loaded_items = db.load()

print("Loaded items:")

for item in loaded_items:
    print(item)
print(book.loan_period())
print(dvd.loan_period())
print(magazine.loan_period())

sorted_items = sorted(items)

for item in sorted_items:
    print(item.title)