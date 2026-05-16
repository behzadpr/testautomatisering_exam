class StatistikPage:
    def __init__(self, page):
        self.page = page

        self.statistik_view = page.locator('.stats')
        self.book_count_text = self.statistik_view.get_by_test_id(
            'book-count')
        self.heart_count_text = self.statistik_view.get_by_test_id(
            'stars-count')

    def is_visible(self):
        """Verify that the Statistik view is visible"""
        return (self.statistik_view.is_visible()
                and self.book_count_text.is_visible()
                and self.heart_count_text.is_visible())

    def get_total_book_count(self):
        """Extract the total book count from the statistics text"""
        text = self.book_count_text.text_content().strip()
        # "Listan har 13 böcker."
        parts = text.split()
        for part in parts:
            if part.isdigit():
                return int(part)
        return 0

    def get_heart_marked_count(self):
        """Extract the heart-marked book count from the statistics text"""
        text = self.heart_count_text.text_content().strip()
        # "Våra användare har hjärtmarkerat 0 böcker."
        parts = text.split()
        for part in parts:
            if part.isdigit():
                return int(part)
        return 0
