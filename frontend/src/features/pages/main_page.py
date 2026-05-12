class MainPage:
    def __init__(self, base_url, page):
        self.base_url = base_url
        self.page = page
        self.catalog_button = page.get_by_test_id("catalog")
        self.add_book_button = page.get_by_test_id("add-book")
        self.favorites_button = page.get_by_test_id("favorites")
        self.statistics_button = page.get_by_test_id("statistics")


    def navigate(self):
        self.page.goto(self.base_url, timeout=5000)

    def click_catalog_button(self):
        self.catalog_button.click()

    def click_add_book_button(self):
        self.add_book_button.click()

    def click_favorites_button(self):
        self.favorites_button.click()

    def click_statistics_button(self):
        self.statistics_button.click()
