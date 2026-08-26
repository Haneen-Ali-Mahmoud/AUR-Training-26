Stock_file = "stock.txt"

def read_stock(filename):
    stock = {}

    try:
        with open(filename, "r") as file:
            lines = file.readlines()
    except FileNotFoundError:
        print(f"{filename} was not found")
        return stock

    for line in lines:
        line = line.strip()

        if not line:
            continue

        try:
            name, quantity = line.split(",")
            name = name.strip().lower()
            quantity = int(quantity.strip())
            stock[name] = quantity

        except ValueError:
            print(f"Error, Invalid Format")
    return stock

def write_stock(filename, stock):
    with open(filename, "w") as file:
        for name, quantity in stock.items():
            file.write(f"{name},{quantity}\n")


def show_stock(stock):
    print("\n--- Stock ---")
    if not stock:
        print("The stock is empty")
    else:
        for index, (name, quantity) in enumerate(stock.items(), start=1):
            print(f"{index}. {name}: {quantity}")

    print("-----------------------------------------\n")


def get_item(stock, allow_new_item):
    items = list(stock.keys())
    while True:
        if allow_new_item:
            stockn_i = ('Enter the stock new name or id: ')
        else:
            stockn_i = ('Enter the stock current name or id: ')

        user_input = input(stockn_i)

        if user_input == "":
            print("Input cann't be empty")
            continue

        if user_input.isdigit():
            item_id = int(user_input)

            if 1 <= item_id <= len(items):
                return items[item_id - 1]

            print(f"Enter a number between 1 and {len(items)}:")
            continue

        item_name = user_input.lower()

        if item_name in items:
            return item_name

        if allow_new_item:
            return item_name

        print(f"{item_name} isn't in the stock")

def get_value(Quantity):
    while True:
     value = input(Quantity)
     value = int(value)
     if value < 0:
        print("Value cann't be negative")
        continue
     break

    return int(value)

def add_stock(stock):
    show_stock(stock)

    item_name = get_item(stock, allow_new_item=True)
    amount = get_value(f"How much to add to {item_name}: ")

    if item_name in stock:
        stock[item_name] += amount
    else:
        stock[item_name] = amount

    print(f"Updated {item_name} to {stock[item_name]}.\n")


def remove_stock(stock):
    if not stock:
        print("The stock is empty\n")
        return

    show_stock(stock)

    item_name = get_item(stock, allow_new_item=False)

    while True:
        amount = get_value(f"How much to remove from {item_name}: ")

        if amount > stock[item_name]:
            print(f"Cann't remove {amount}, only {stock[item_name]} in stock")
            continue

        stock[item_name] -= amount
        break

    print(f"Updated {item_name} to {stock[item_name]}\n")


def get_menu_choice():
    print("1.add stock")
    print("2.remove stock")
    print("3.show stock's contents")
    print("4.to exit the program")

    while True:
        choice = input("Enter your choice: ")
        if choice in ("1", "2", "3", "4"):
            return choice

        print("Invalid choice, enter 1, 2, 3, 4\n")


def main():
    stock = read_stock(Stock_file)

    while True:
        choice = get_menu_choice()
        if choice == "1":
            add_stock(stock)
        elif choice == "2":
            remove_stock(stock)
        elif choice == "3":
            show_stock(stock)
        elif choice == "4":
            write_stock(Stock_file, stock)
            print("Stock saved")
            break


if __name__ == "__main__":
    main()
