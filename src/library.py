from .book import Book

class Library:
    def __init__(self):
        self._books = []

    def add_book(self, book: Book):
        # Adiciona um livro à coleção, se já não existir um livro com o mesmo título
        if any(b.title == book.title for b in self._books):
            raise ValueError(f"Book '{book.title}' already exists in the library.")
        self._books.append(book)

    def remove_book(self, title: str):
        # Remove um livro pelo título
        for b in self._books:
            if b.title == title:
                self._books.remove(b)
                return
        raise ValueError(f"Book '{title}' not found in the library.")

    def list_books(self):
        # Retorna a lista de livros
        return list(self._books)  # Retorna uma cópia da lista

    def find_book(self, title: str):
        # Retorna um livro específico pelo título
        for b in self._books:
            if b.title == title:
                return b
        return None
