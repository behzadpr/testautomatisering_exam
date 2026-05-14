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

    def get_book_by_title(self, title):
        """Get a book locator by its title"""
        for i in range(self.book_items.count()):
            book = self.book_items.nth(i)
            if title in self.get_title(book):
                return book
        return None

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

    def get_author(self, book_locator):
        """Get the author of a book"""
        return book_locator.text_content().strip().split(',')[1]

    def click_star_icon(self, book_locator):
        """Click the heart icon on a book to toggle favorite status"""
        book_locator.hover()
        book_locator.locator('.star').click()

    def is_book_favorited(self, book_locator):
        """Check if a book's heart icon has the 'selected' class"""
        return book_locator.locator('.star.selected').count() == 1


    def get_favorited_titles(self):
        """Return a list of titles for all currently favorited books"""
        titles = []
        for i in range(self.book_items.count()):
            book = self.book_items.nth(i)
            if book.locator('.star.selected').count() == 1:
                titles.append(self.get_title(book))
        return titles

    def clear_all_favorites(self):
        """Deselect all favorited books by clicking each selected heart icon."""
        selected = self.book_items.locator('.star.selected')
        # Loop until there are no selected item left
        while selected.count() > 0:
            selected.first.click()
