from backend.src.book import Book
from backend.src.favorite_books import FavoriteBooks


def make_book():
    return Book(1, "A", "T")


def test_add_book_to_favorites():
    fav = FavoriteBooks()
    book = make_book()

    assert fav.add(book) is True
    # adding again should return False
    assert fav.add(book) is False


def test_remove_book_from_favorites():
    fav = FavoriteBooks()
    book = make_book()
    fav.add(book)
    assert fav.remove(book) is True
    # removing again returns False
    assert fav.remove(book) is False
