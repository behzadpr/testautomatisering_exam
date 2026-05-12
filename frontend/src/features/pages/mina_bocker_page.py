class MinaBockerPage:
    def __init__(self, page):
        self.page = page

        self.mina_bocker_view = page.locator('.favorites')
        self.book_items = self.mina_bocker_view.locator('[data-testid="book-list"] .book')

    def is_mina_bocker_visible(self):
        """Verify that the "Mina böcker" view is visible"""
        return self.mina_bocker_view.is_visible()

    def get_book_count(self):
        """Get the number of books in the "Mina böcker" list"""
        return self.book_items.count()

    def get_first_book(self):
        """Get the first book in the list"""
        return self.book_items.first
