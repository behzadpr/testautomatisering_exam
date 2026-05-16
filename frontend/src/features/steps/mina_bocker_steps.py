from behave import given, when, then

from frontend.src.features.pages.katalog_page import KatalogPage
from frontend.src.features.pages.mina_bocker_page import MinaBockerPage


@given("I have no favorite books")
def step_no_favorite_books(context):
    """Ensure no books are favorited by navigating fresh"""
    context.katalog = KatalogPage(context.page)
    context.katalog.clear_all_favorites()


@when('I navigate to "Mina böcker"')
def step_navigate_to_mina_bocker(context):
    """Navigate to the Mina böcker view"""
    context.main.click_favorites_button()
    context.favorites = MinaBockerPage(context.page)


@then("I should see a default message indicating no favorites have been added")
def step_see_default_message(context):
    """Verify a default message is visible when there are no
    favorites"""
    assert context.favorites.is_mina_bocker_visible(), \
        '"Mina böcker" view should be visible'
    assert context.favorites.has_default_message(), \
        'Default empty-state message should be visible'
    assert context.favorites.get_book_count() == 0, \
        "No books should be listed when there are no favorites"


@then("I should see all my favorited books listed")
def step_see_all_favorited_books(context):
    """Verify that all favorited books appear in the "Mina böcker" list"""
    assert context.favorites.is_mina_bocker_visible(), \
        '"Mina böcker" view should be visible'
    for i in range(context.favorites.get_book_count()):
        book_text = context.favorites.book_items.nth(i).text_content() \
            .strip()
        assert any(book_text in title for title in \
                   context.catalog_favorited_titles), (
            f'Book "{book_text}" should appear in favorited titles: '
            f'{context.catalog_favorited_titles}'
        )


@given('I can see the book in "Mina böcker"')
def step_verify_book_in_mina_bocker(context):
    """Navigate to Mina böcker and verify the favorited book is listed"""
    context.main.click_favorites_button()
    context.favorites = MinaBockerPage(context.page)
    assert context.favorites.is_mina_bocker_visible(), \
        '"Mina böcker" view should be visible'
    assert context.favorites.get_book_count() > 0, \
        "Favorited book should be listed in Mina böcker"
    first_book_text = context.favorites.get_first_book() \
        .text_content().strip()
    assert first_book_text in context.catalog_current_book_title, (
        f'Expected "{context.catalog_current_book_title}" to appear in '
        f'Mina böcker'
    )


@when("I navigate to Katalog")
def step_navigate_to_katalog(context):
    """Navigate back to the Katalog view"""
    context.main.click_catalog_button()
    context.katalog = KatalogPage(context.page)


@when("I click the heart icon on that book to deselect it")
def step_deselect_heart_icon(context):
    """Deselect the previously favorited book by clicking its heart icon"""
    context.execute_steps('When I click the heart icon')


@then('the book should no longer appear in "Mina böcker"')
def step_book_removed_from_mina_bocker(context):
    """Navigate to Mina böcker and verify the book is no longer listed"""
    context.main.click_favorites_button()
    context.favorites = MinaBockerPage(context.page)
    assert context.favorites.is_mina_bocker_visible(), \
        '"Mina böcker" view should be visible'
    book_count = context.favorites.get_book_count()
    for i in range(book_count):
        book_text = context.favorites.book_items.nth(i).text_content() \
            .strip()
        assert context.catalog_current_book_title not in book_text, (
            f'Book "{context.catalog_current_book_title}" should have '
            f'been removed from Mina böcker'
        )