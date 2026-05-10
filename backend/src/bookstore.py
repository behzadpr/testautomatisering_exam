from .book import Book


class BookStore:
    """ A class to store and manage books """

    def __init__(self):
        self.books = {}
        self.assigned_id = 1

    def add_book(self, author, title):
        """Creates and stores a new Book."""
        book = Book(self.assigned_id, author, title)
        self.books[self.assigned_id] = book
        self.assigned_id += 1
        return book

    def toggle_favorite(self, book_id):
        """Toggles the is_favorite flag for a book by id."""

        book = self.books[book_id]
        book.is_favorite = not book.is_favorite
        return book.is_favorite

    def get_book(self, book_id):
        return self.books.get(book_id)

