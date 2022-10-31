class Publication:
    def __init__(self, name):
        self.name = name

    def print_info(self):
        print(f"Pub name: {self.name}")


class Magazine(Publication):
    def __init__(self, name, editor):
        self.editor = editor
        super().__init__(name)

    def print_info(self):
        print(f"Pub name: {self.name}, Editor name {self.editor}")


class Book(Publication):
    def __init__(self, name, page_count, author_nam):
        self.page_count = page_count
        self.author = author_nam
        super().__init__(name)

    def print_info(self):
        print(f"Pub name: {self.name}, pagecount: {self.page_count}, author: {self.author}")


pub1 = Magazine("Aku Ankka", "Aki Hyyppä")
pub2 = Book("Hytti n:o 6", 220, "Rosa Liksom")
pub1.print_info()
pub2.print_info()
