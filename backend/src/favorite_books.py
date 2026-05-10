class FavoriteBooks:
    """A container to manage favorite books."""

    def __init__(self):
        self.favorites_books = []

    def add(self, book):
        """Adds a book to favorites."""

        if book in self.favorites_books:
            return False
        self.favorites_books.append(book)
        return True

    def remove(self, book):
        """Removes a book from favorites."""

        if book in self.favorites_books:
            self.favorites_books.remove(book)
            return True
        return False
