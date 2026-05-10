from backend.src.bookstore import BookStore
from backend.src.favorite_books import FavoriteBooks


def test_integration_toggle_and_manage_favorites():
    book_store = BookStore()
    favorite_books = FavoriteBooks()

    book_1 = book_store.add_book("Author-1", "Title-1")
    book_2 = book_store.add_book("Author-2", "Title-2")

    assert not book_1.is_favorite

    # toggle favorite on book_1
    book_store.toggle_favorite(book_1.id)
    assert book_1.is_favorite

    # add book_1 to favorites
    assert favorite_books.add(book_1) is True

    # toggle off and remove from favorites
    book_store.toggle_favorite(book_1.id)
    assert not book_1.is_favorite
    assert favorite_books.remove(book_1) is True

    # add a non-favorite book
    assert not book_2.is_favorite
    assert favorite_books.add(book_2) is True

