class MinaBockerPage:
    def __init__(self, page):
        self.page = page

        self.mina_bocker_view = page.locator('.favorites')
        self.book_items = self.mina_bocker_view.locator(
            '[data-testid="book-list"] .book')

    def is_mina_bocker_visible(self):
        """Verify that the 'Mina böcker' view container is visible"""
        return self.mina_bocker_view.is_visible()

    def has_default_message(self):
        """Verify the empty-state paragraph is visible (no favorites selected)"""
        default_header = self.mina_bocker_view.locator('p')
        default_header_text = default_header.get_by_text(
            "När du valt, kommer dina favoritböcker att visas här.")
        return default_header_text.is_visible()

    def get_book_count(self):
        """Get the number of books in the "Mina böcker" list"""
        return self.book_items.count()

    def get_first_book(self):
        """Get the first book in the list"""
        return self.book_items.first
