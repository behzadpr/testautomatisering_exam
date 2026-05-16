from behave import given, when, then
from playwright.sync_api import expect

from frontend.src.features.pages.lagg_till_bok_page import LaggTillBokPage
from frontend.src.features.pages.katalog_page import KatalogPage


@when('I navigate to "Lägg till bok"')
def step_navigate_to_lagg_till_bok(context):
    """Navigate to the Lägg till bok view"""
    context.main.click_add_book_button()
    context.lagg_till_bok = LaggTillBokPage(context.page)


@then('I should see a clean form with empty title and author fields')
def step_see_clean_form(context):
    """Verify the Lägg till bok view shows a clean form with empty
    fields"""
    assert context.lagg_till_bok.is_visible(), \
        '"Lägg till bok" view should be visible'
    assert context.lagg_till_bok.get_title_value() == '', \
        'Title field should be empty'
    assert context.lagg_till_bok.get_author_value() == '', \
        'Författare field should be empty after submission'


@then('the "Lägg till ny bok" button should be disabled')
def step_submit_button_disabled(context):
    """Verify that the submit button is disabled"""
    expect(context.lagg_till_bok.submit_button).to_be_disabled()


@given('I am on the "Lägg till bok" view')
def step_on_lagg_till_bok_view(context):
    """Navigate to the 'Lägg till bok' view"""
    context.execute_steps('When I navigate to "Lägg till bok"')


@when('I enter a title but no author')
def step_enter_title_only(context):
    """Fill in only the title field"""
    context.lagg_till_bok.fill_title('Testbok')


@when('I enter an author but no title')
def step_enter_author_only(context):
    """Fill in only the author field"""
    context.lagg_till_bok.fill_author('Testförfattare')


@when('I have not entered anything')
def step_enter_nothing(context):
    """Leave both fields empty (no action needed — fields are empty by
    default)"""
    pass


@when('I enter a title and an author')
def step_enter_title_and_author(context):
    """Fill in both title and author fields"""
    context.new_book_title = 'Test_bok'
    context.new_book_author = 'Test_författare'
    context.lagg_till_bok.fill_title(context.new_book_title)
    context.lagg_till_bok.fill_author(context.new_book_author)


@then('the "Lägg till ny bok" button should be enabled')
def step_submit_button_enabled(context):
    """Verify that the submit button is enabled"""
    expect(context.lagg_till_bok.submit_button).to_be_enabled()


@when('I click the "Lägg till ny bok" button')
def step_click_submit_button(context):
    """Click the submit button to add the book"""
    context.lagg_till_bok.click_submit()


@then('the new book should appear in the catalog')
def step_new_book_in_catalog(context):
    """Navigate to Katalog and verify the new book is listed"""
    context.main.click_catalog_button()
    context.katalog = KatalogPage(context.page)
    book_in_catalog = context.katalog.get_book_by_title(
        context.new_book_title)
    if book_in_catalog:
        assert context.new_book_author in \
            context.katalog.get_author(book_in_catalog), \
            f'New book "{context.new_book_title}",' \
            f'"{context.new_book_author}" should appear in ' \
            f'the catalog'


@then('the title and author fields should be empty')
def step_fields_are_empty(context):
    """Verify the title and author fields are cleared after submission"""
    assert context.lagg_till_bok.get_title_value() == '', \
        'Title field should be empty after submission'
    assert context.lagg_till_bok.get_author_value() == '', \
        'Författare field should be empty after submission'
