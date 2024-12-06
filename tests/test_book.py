from src.book import Book

def test_book_creation():
    book = Book("1984", "George Orwell")
    assert book.title == "1984"
    assert book.author == "George Orwell"
    assert str(book) == "'1984' by George Orwell"
