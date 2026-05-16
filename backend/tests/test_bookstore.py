from backend.src.bookstore import BookStore


def test_add_book_returns_book_and_assigns_id():
    # Given
    book_store = BookStore()
    # When
    book = book_store.add_book("Author", "Title")
    assert book.id == 1
    # Then
    assert book.author == "Author"
    assert book.title == "Title"
    assert book.is_favorite is False


def test_toggle_favorite_toggles_flag():
    # Given
    book_store = BookStore()
    # When
    book = book_store.add_book("A", "T")
    # Then
    assert book_store.toggle_favorite(book.id) is True
    assert book.is_favorite is True
    assert book_store.toggle_favorite(book.id) is False
    assert book.is_favorite is False
