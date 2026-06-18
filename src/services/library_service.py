from models.book import Book
from repositories.book_repository import BookRepository
from structures.binary_search_tree import BinarySearchTree


class LibraryService:
    def __init__(self):
        # Repositório responsável por salvar e carregar os livros em arquivo.
        self.repository = BookRepository()

        # Árvore binária de busca usada como estrutura principal do projeto.
        self.book_tree = BinarySearchTree()

        # Carrega os livros salvos anteriormente e insere na árvore.
        self._load_books_into_tree()

    def _load_books_into_tree(self) -> None:
        # Insere na árvore todos os livros encontrados no arquivo JSON.
        books = self.repository.load_books()

        for book in books:
            self.book_tree.insert(book)

    def _save_current_books(self) -> None:
        # Salva no arquivo os livros atualmente armazenados na árvore.
        books = self.book_tree.in_order()
        self.repository.save_books(books)

    def add_book(self, book_id: int, title: str, author: str, year: int) -> None:
        # Cria um livro, insere na árvore e salva no arquivo.
        book = Book(book_id, title, author, year)
        self.book_tree.insert(book)
        self._save_current_books()

    def find_book_by_id(self, book_id: int):
        # Cria uma chave temporária para buscar usando o ID.
        search_key = Book(book_id, "", "", 0)
        return self.book_tree.search(search_key)

    def update_book(self, book_id: int, title: str, author: str, year: int) -> bool:
        # Busca o livro e atualiza seus dados se ele existir.
        book = self.find_book_by_id(book_id)

        if book is None:
            return False

        book.title = title
        book.author = author
        book.year = year

        self._save_current_books()
        return True

    def remove_book(self, book_id: int) -> bool:
        # Busca o livro antes de remover para evitar erro.
        book = self.find_book_by_id(book_id)

        if book is None:
            return False

        self.book_tree.remove(book)
        self._save_current_books()
        return True

    def list_books(self) -> list:
        # Retorna os livros ordenados pelo ID.
        return self.book_tree.in_order()

    def count_books(self) -> int:
        # Retorna a quantidade de livros na árvore.
        return self.book_tree.count()

    def tree_height(self) -> int:
        # Retorna a altura atual da árvore.
        return self.book_tree.height()