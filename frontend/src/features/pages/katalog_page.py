class KatalogPage:
    def __init__(self, page):
        self.page = page

        self.catalog_view = page.locator('.catalog')
        self.book_items = self.catalog_view.locator('.book')

    def is_catalog_visible(self):
        """Verify that the catalog section is visible"""
        return self.catalog_view.is_visible()

    def get_book_count(self):
        """Get the number of books displayed in the catalog"""
        return self.book_items.count()

    def get_first_book(self):
        """Get the first book in the catalog"""
        return self.book_items.first

    def hover_over_book(self, book_locator):
        """Hover over a book item to reveal the heart icon"""
        book_locator.hover()

    def get_heart_icon(self, book_locator):
        """Get the heart icon inside a book"""
        return book_locator.locator('.star')

    def get_title(self, book_locator):
        """Get the title of a book"""
        return book_locator.text_content().strip().split(',')[0]

    def click_star_icon(self, book_locator):
        """Click the heart icon on a book to toggle favorite status"""
        book_locator.hover()
        book_locator.locator('.star').click()

    def is_book_favorited(self, book_locator):
        """Check if a book's heart icon has the 'selected' class"""
        return book_locator.locator('.star.selected').count() == 1
