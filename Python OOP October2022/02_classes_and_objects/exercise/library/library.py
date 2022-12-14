from user import User


class Library:
    def __init__(self):
        self.user_records = []
        self.books_available = {}  # {'authors': []}
        self.rented_books = {}  # {'usernames': {'book names': 0}}

    def get_book(self, author: str, book_name: str, days_to_return: int, user: User):
        if book_name not in self.books_available[author]:
            return f'The book "{book_name}" is already rented and will be available in ' \
                   f'{self.rented_books[user.username][book_name]} days!'

        user.books.append(book_name)
        self.books_available[author].remove(book_name)
        if user.username not in self.rented_books:
            self.rented_books[user.username] = {book_name: days_to_return}
        else:
            self.rented_books[user.username][book_name] = days_to_return
        return f"{book_name} successfully rented for the next {days_to_return} days!"

    def return_book(self, author: str, book_name: str, user: User):

        if book_name in self.rented_books[user.username]:
            self.books_available[author].append(book_name)
            del self.rented_books[user.username][book_name]
            user.books.remove(book_name)
        else:
            return f"{user.username} doesn't have this book in his/her records!"
