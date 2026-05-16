from behave import given
from playwright.sync_api import expect

from frontend.src.features.pages.main_page import MainPage
from frontend.src.features.pages.katalog_page import KatalogPage


@given("the main page is open")
def step_main_page_is_open(context):
    context.main = MainPage(context.base_url, context.page)
    context.main.navigate()
    context.katalog = KatalogPage(context.page)
    main_element = context.page.locator('main')
    welcome_header = main_element.locator('h2')
    welcome_header_text = welcome_header.get_by_text("Välkommen")
    assert welcome_header_text.is_visible(), \
        'Header "Välkommen!" should be visible'


@given("page has all necessary items loaded")
def step_all_main_page_items(context):
    """Verify that all main page navigation items are loaded and visible"""
    expect(context.page.get_by_text("Katalog")).to_be_visible()
    expect(context.page.get_by_text("Lägg till bok")).to_be_visible()
    expect(context.page.get_by_text("Mina böcker")).to_be_visible()
    expect(context.page.get_by_text("Statistik")).to_be_visible()


@given("I have marked several books as favorites in Katalog")
def step_mark_several_favorites(context):
    """Mark multiple books as favorites in Katalog and store their titles"""
    context.katalog = KatalogPage(context.page)
    context.catalog_favorited_titles = []
    book_count = min(3, context.katalog.book_items.count())
    for i in range(book_count):
        book = context.katalog.book_items.nth(i)
        title = context.katalog.get_title(book)
        context.katalog.click_star_icon(book)
        context.catalog_favorited_titles.append(title)
