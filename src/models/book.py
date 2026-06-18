
 # Classe que representa um livro na biblioteca.

class Book:
    def __init__(self, book_id: int, title: str, author: str, year: int):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.year = year