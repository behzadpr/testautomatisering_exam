class LaggTillBokPage:
    def __init__(self, page):
        self.page = page

        self.add_book_view = page.locator('.form')
        self.title_label = self.add_book_view.locator('label[for="add-input-title"]')
        self.title_input = self.add_book_view.get_by_test_id('add-input-title')
        self.author_label = self.add_book_view.locator('label[for="add-input-author"]')
        self.author_input = self.add_book_view.get_by_test_id('add-input-author')
        self.submit_button = self.add_book_view.get_by_test_id('add-submit')

    def is_visible(self):
        """Verify that all items of the 'Lägg till bok' view are visible"""
        return (
            self.add_book_view.is_visible()
            and self.title_label.is_visible()
            and self.title_input.is_visible()
            and self.author_label.is_visible()
            and self.author_input.is_visible()
            and self.submit_button.is_visible()
        )

    def get_title_value(self):
        """Get the current value of the title input"""
        return self.title_input.input_value()

    def get_author_value(self):
        """Get the current value of the author input"""
        return self.author_input.input_value()

    def is_submit_button_enabled(self):
        """Check if the submit button is enabled"""
        return self.submit_button.is_enabled()

    def fill_title(self, title):
        """Fill in the title field"""
        self.title_input.fill(title)

    def fill_author(self, author):
        """Fill in the author field"""
        self.author_input.fill(author)

    def click_submit(self):
        """Click the submit button"""
        self.submit_button.click()

