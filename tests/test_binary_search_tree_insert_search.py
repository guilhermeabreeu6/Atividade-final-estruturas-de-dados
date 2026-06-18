import os
import sys
import unittest

# Adiciona a pasta src no caminho de importação.
# Assim os testes conseguem acessar os arquivos do projeto.
sys.path.insert(
    0,
    os.path.abspath(os.path.join(os.path.dirname(__file__), "../src"))
)

from models.book import Book
from structures.binary_search_tree import BinarySearchTree


class TestBinarySearchTreeInsertSearch(unittest.TestCase):
    def create_book(self, book_id: int) -> Book:
        # Cria um livro simples para ser usado nos testes.
        return Book(book_id, f"Book {book_id}", "Test Author", 2026)

    def test_insert_and_search_book(self):
        # Testa se um livro inserido pode ser encontrado na árvore.
        tree = BinarySearchTree()
        book = self.create_book(10)

        tree.insert(book)
        result = tree.search(self.create_book(10))

        self.assertIsNotNone(result)
        self.assertEqual(result.book_id, 10)

    def test_search_book_not_found(self):
        # Testa a busca por um livro que não existe.
        tree = BinarySearchTree()
        tree.insert(self.create_book(10))

        result = tree.search(self.create_book(99))

        self.assertIsNone(result)

    def test_insert_duplicate_book_id_raises_error(self):
        # Testa se a árvore impede cadastro com ID duplicado.
        tree = BinarySearchTree()

        tree.insert(self.create_book(10))

        with self.assertRaises(ValueError):
            tree.insert(self.create_book(10))


if __name__ == "__main__":
    unittest.main()