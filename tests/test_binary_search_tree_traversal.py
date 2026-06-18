import os
import sys
import unittest

# Adiciona a pasta src no caminho de importação.
# Isso permite importar os módulos da aplicação.
sys.path.insert(
    0,
    os.path.abspath(os.path.join(os.path.dirname(__file__), "../src"))
)

from models.book import Book
from structures.binary_search_tree import BinarySearchTree


class TestBinarySearchTreeTraversal(unittest.TestCase):
    def create_book(self, book_id: int) -> Book:
        # Cria um livro simples para o teste.
        return Book(book_id, f"Book {book_id}", "Test Author", 2026)

    def get_book_ids(self, books: list) -> list:
        # Extrai apenas os IDs dos livros.
        return [book.book_id for book in books]

    def test_in_order_returns_books_ordered_by_id(self):
        # Testa se o percurso em ordem retorna os livros ordenados pelo ID.
        tree = BinarySearchTree()

        for book_id in [10, 5, 15, 3, 7, 12, 18]:
            tree.insert(self.create_book(book_id))

        self.assertEqual(
            self.get_book_ids(tree.in_order()),
            [3, 5, 7, 10, 12, 15, 18]
        )

    def test_in_order_empty_tree_returns_empty_list(self):
        # Testa se uma árvore vazia retorna uma lista vazia.
        tree = BinarySearchTree()

        self.assertEqual(tree.in_order(), [])


if __name__ == "__main__":
    unittest.main()