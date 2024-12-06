import pytest
from src.library import Library
from src.book import Book

def test_add_and_list_books():
    library = Library()
    book1 = Book("1984", "George Orwell")
    book2 = Book("Brave New World", "Aldous Huxley")

    library.add_book(book1)
    library.add_book(book2)

    books = library.list_books()
    assert len(books) == 2
    assert books[0].title == "1984"
    assert books[1].title == "Brave New World"

def test_add_duplicate_book():
    library = Library()
    book = Book("1984", "George Orwell")
    library.add_book(book)
    with pytest.raises(ValueError):
        library.add_book(book)  # Tentando adicionar o mesmo livro novamente

def test_remove_book():
    library = Library()
    book = Book("1984", "George Orwell")
    library.add_book(book)

    library.remove_book("1984")
    assert len(library.list_books()) == 0

def test_remove_nonexistent_book():
    library = Library()
    with pytest.raises(ValueError):
        library.remove_book("Not Real Book")

def test_find_book():
    library = Library()
    book = Book("1984", "George Orwell")
    library.add_book(book)

    found = library.find_book("1984")
    assert found is not None
    assert found.title == "1984"

    not_found = library.find_book("Nonexistent")
    assert not_found is None
