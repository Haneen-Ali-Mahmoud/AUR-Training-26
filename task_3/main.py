from library import library_items

class main:
    def __init__(self, filename="database.txt"):
        self.filename = filename

    def load(self):
        items = []
        with open(self.filename, "r") as file:
            for line in file:
                line = line.strip()
                parts = line.split("|")

                data = {}
                for part in parts:
                    key, value = part.split("=")
                    data[key] = value

                item = library_items.from_dict(data)
                items.append(item)

        return items
    def save(self, items):
        with open(self.filename, "w") as file:
            for item in items:
                    data = item.to_dict()
                    line = "|".join(f"{key}={value}" for key, value in data.items())
                    file.write(line + "\n")

