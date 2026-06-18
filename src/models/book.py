class Book:
    def __init__(self, book_id: int, title: str, author: str, year: int):
        # Guarda o identificador do livro, usado como chave da árvore.
        self.book_id = book_id

        # Guarda o título do livro.
        self.title = title

        # Guarda o nome do autor do livro.
        self.author = author

        # Guarda o ano de publicação do livro.
        self.year = year

    def __str__(self) -> str:
        # Retorna uma representação amigável do livro para exibir no menu.
        return f"ID: {self.book_id} | Title: {self.title} | Author: {self.author} | Year: {self.year}"

    def __lt__(self, other) -> bool:
        # Permite comparar livros usando o ID.
        return self.book_id < other.book_id

    def __gt__(self, other) -> bool:
        # Permite comparar livros usando o ID.
        return self.book_id > other.book_id

    def __eq__(self, other) -> bool:
        # Dois livros são considerados iguais quando possuem o mesmo ID.
        return self.book_id == other.book_id