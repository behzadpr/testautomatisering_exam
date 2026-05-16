from behave import given, when, then

from frontend.src.features.pages.statistik_page import StatistikPage
from frontend.src.features.pages.katalog_page import KatalogPage
from frontend.src.features.pages.lagg_till_bok_page import LaggTillBokPage


def navigate_to_statistik(context):
    """Helper: click Statistik nav button and instantiate StatistikPage"""
    context.main.click_statistics_button()
    context.statistik = StatistikPage(context.page)


@when('I navigate to "Statistik"')
def step_navigate_to_statistik(context):
    """Navigate to the Statistik view"""
    navigate_to_statistik(context)


@then('I should see the total number of books in the catalog')
def step_see_total_book_count(context):
    """Verify that a positive total book count is displayed"""
    assert context.statistik.is_visible(), \
        '"Statistik" view should be visible'
    assert context.statistik.get_total_book_count() > 0, \
        'Total book count should be greater than 0'


@then('I should see that 0 books have been heart-marked')
def step_see_zero_heart_marked(context):
    """Verify that the heart-marked count is 0"""
    assert context.statistik.is_visible(), \
        '"Statistik" view should be visible'
    assert context.statistik.get_heart_marked_count() == 0, \
        'Heart-marked count should be 0 when no books are favorited'


@given('I navigate to "Statistik"')
def step_given_navigate_to_statistik(context):
    """Navigate to the Statistik view (given step)"""
    navigate_to_statistik(context)


@given('I store the current heart-marked count')
def step_note_heart_marked_count(context):
    """Store the current heart-marked count for later comparison"""
    context.initial_heart_marked_count = \
        context.statistik.get_heart_marked_count()


@when('I favorite a book in Katalog')
def step_favorite_a_book_in_katalog(context):
    """Navigate to Katalog and favorite the first book"""
    context.main.click_catalog_button()
    context.katalog = KatalogPage(context.page)
    first_book = context.katalog.get_first_book()
    context.katalog.click_star_icon(first_book)


@then('the heart-marked count should have increased by 1')
def step_heart_marked_count_increased(context):
    """Verify the heart-marked count increased by 1"""
    new_count = context.statistik.get_heart_marked_count()
    expected = context.initial_heart_marked_count + 1
    assert new_count == expected, \
        f'Heart-marked count should be {expected} but was {new_count}'


@given('I note the current total book count')
def step_note_total_book_count(context):
    """Store the current total book count for later comparison"""
    context.initial_total_book_count = \
        context.statistik.get_total_book_count()


@when('I add a new book in "Lägg till bok"')
def step_add_new_book(context):
    """Navigate to Lägg till bok and add a new book"""
    context.main.click_add_book_button()
    context.lagg_till_bok = LaggTillBokPage(context.page)
    context.lagg_till_bok.fill_title('Statistik_testbok')
    context.lagg_till_bok.fill_author('Statistik_författare')
    context.lagg_till_bok.click_submit()


@then('the total book count should have incremented by 1')
def step_total_book_count_increased(context):
    """Verify the total book count incremented by 1"""
    new_count = context.statistik.get_total_book_count()
    expected = context.initial_total_book_count + 1
    assert new_count == expected, \
        f'Total book count should be {expected} but was {new_count}'
