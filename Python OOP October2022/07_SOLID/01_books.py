class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.page = 0

    def turn_page(self, page):
        self.page = page


class Library:
    def __init__(self):
        self.books = []

    def add_books(self, book_obj):
        self.books.append(book_obj)

    def remove_book(self, title):
        pass

    def find_book(self, title):
        try:
            return [book_obj for book_obj in self.books if book_obj.title == title][0]
        except IndexError:
            return "Book not found"


library = Library()

for num in range(1, 11):
    book = Book(f'title {num}', f'author {num}')
    library.add_books(book)

