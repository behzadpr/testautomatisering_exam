from behave import given, when, then
from playwright.sync_api import expect

from frontend.src.features.pages.main_page import MainPage
from frontend.src.features.pages.katalog_page import KatalogPage
from frontend.src.features.pages.mina_bocker_page import MinaBockerPage


@given("the main page is open")
def step_main_page_is_open(context):
    context.main = MainPage(context.base_url, context.page)
    context.main.navigate()
    context.katalog = KatalogPage(context.page)
    main_element = context.page.locator('main')
    welcome_header = main_element.locator('h2')
    welcome_header_text = welcome_header.get_by_text("Välkommen")
    assert welcome_header_text.is_visible(), 'Header "Välkommen!" should be visible'

@given("page has all necessary items loaded")
def step_all_main_page_items(context):
    """Verify that all main page navigation items are loaded and visible"""
    expect(context.page.get_by_text("Katalog")).to_be_visible()
    expect(context.page.get_by_text("Lägg till bok")).to_be_visible()
    expect(context.page.get_by_text("Mina böcker")).to_be_visible()
    expect(context.page.get_by_text("Statistik")).to_be_visible()


@then('I should see the Katalog view by default')
def step_see_katalog_view_by_default(context):
    """Verify that Katalog is the default view"""
    assert context.katalog.is_catalog_visible(), 'Catalog view should be visible'
    katalog_header = context.katalog.catalog_view.locator('p')
    expect(katalog_header.get_by_text("Sidan för dig som gillar att läsa. Välj dina favoriter.")).to_be_visible()


@then('the list of available books should be displayed')
def step_list_of_books_displayed(context):
    """Verify that a list of books is displayed"""
    assert context.katalog.get_book_count() > 0, "No books found in the catalog"


@given('I see a list of books')
def step_see_list_of_books(context):
    """Verify that the list of books is visible"""
    step_list_of_books_displayed(context)


@then('each book should display a title')
def step_each_book_has_title(context):
    """Verify that each book displays a title (book text content is non-empty)"""
    books = context.page.locator('.book')
    for i in range(books.count()):
        assert books.nth(i).text_content().strip() != "", "Book item should have text content"


@then('each book should display an author name')
def step_each_book_has_author(context):
    """Verify that each book displays an author (inline text contains a comma separating title and author)"""
    books = context.page.locator('.book')
    for i in range(books.count()):
        text = books.nth(i).text_content().strip()
        assert ',' in text, f"Book item text should contain author separated by comma: {text}"


@when('I hover over a book item')
def step_hover_over_book(context):
    """Move mouse cursor over a book item"""
    books = context.page.locator('.book')
    context.current_book = books.first
    context.current_book.hover()


@then('a low-opacity heart icon should appear to the left of the book')
def step_heart_icon_appears(context):
    """Verify that a low-opacity heart icon appears on hover"""
    heart_icon = context.katalog.get_heart_icon(context.current_book)
    assert heart_icon.first.is_visible()


@given('I see a book in the catalog')
def step_see_book_in_catalog(context):
    """Pick a book in the catalog"""
    context.current_book = context.katalog.get_first_book()
    context.current_book_title = context.katalog.get_title(context.current_book)


@given('I hover over the book to show the heart icon')
def step_hover_to_show_heart(context):
    """Hover over the book to get the heart icon"""
    context.heart_icon = context.katalog.get_heart_icon(context.current_book)


@when('I click the heart icon')
def step_click_heart_icon(context):
    """Click the heart icon to toggle favorite status"""
    context.katalog.click_star_icon(context.current_book)


@then('the book should be marked as a favorite')
def step_book_marked_as_favorite(context):
    """Verify that the book is now marked as a favorite"""
    assert context.current_book.locator('.star.selected').count() == 1, "Star icon should have 'selected' class"


@then('the heart icon should appear in filled state')
def step_heart_icon_filled(context):
    """Verify that the heart icon is now filled/highlighted"""

    selected_icon = context.current_book.locator('.star.selected')
    expect(selected_icon).to_be_visible()


@given('I have marked a book as a favorite')
def step_mark_book_favorite(context):
    """Mark a book as a favorite"""

    context.current_book = context.katalog.get_first_book()
    context.katalog.click_star_icon(context.current_book)


@given('I hover over the favorite book')
def step_hover_favorite_book(context):
    """Hover over the already-favorited book"""
    context.katalog.hover_over_book(context.selected_book)


@then('the heart icon should return to unfilled state')
def step_heart_icon_unfilled(context):
    """Verify that the heart icon is now unfilled"""
    assert not context.katalog.is_book_favorited(context.current_book)


@given('I have marked several books as favorites in Katalog')
def step_mark_several_favorites(context):
    """Mark multiple books as favorites"""
    context.favorited_books = []
    for i in range(min(3, context.katalog.book_items.count())):
        book = context.katalog.book_items.nth(i)
        context.katalog.click_star_icon(book)
        context.favorited_books.append(book)


@when('I navigate to another page')
def step_navigate_to_another_page(context):
    """Navigate to a different page"""
    context.main.click_add_book_button()


@when('then I return to Katalog')
def step_return_to_katalog(context):
    """Return to the Katalog page"""
    context.main.click_catalog_button()


@then('my favorite selections should still be marked')
def step_favorites_still_marked(context):
    """Verify that favorite selections persist"""
    favorite_books = context.favorited_books
    for i in range(len(favorite_books)):
        assert context.katalog.is_book_favorited(favorite_books[i])


@then('the book should appear in my "Mina böcker" list')
def step_book_in_mina_bocker_list(context):
    """Verify that the favorited book appears in Mina böcker list"""
    context.main.click_favorites_button()
    context.favorites = MinaBockerPage(context.page)
    favorites_current_book = context.favorites.get_first_book().text_content().strip()
    assert favorites_current_book in context.current_book_title, "Book should appear in Mina böcker list with correct title"



