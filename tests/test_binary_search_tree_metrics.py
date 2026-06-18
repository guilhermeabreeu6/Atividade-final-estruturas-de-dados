import os
import sys
import unittest

# Adiciona a pasta src no caminho de importação.
# Isso permite que os testes encontrem os arquivos do projeto.
sys.path.insert(
    0,
    os.path.abspath(os.path.join(os.path.dirname(__file__), "../src"))
)

from models.book import Book
from structures.binary_search_tree import BinarySearchTree


class TestBinarySearchTreeMetrics(unittest.TestCase):
    def create_book(self, book_id: int) -> Book:
        # Cria um livro simples para ser usado nos testes.
        return Book(book_id, f"Book {book_id}", "Test Author", 2026)

    def create_tree_with_books(self) -> BinarySearchTree:
        # Monta uma árvore com altura conhecida.
        tree = BinarySearchTree()

        for book_id in [10, 5, 15, 3, 7, 12, 18]:
            tree.insert(self.create_book(book_id))

        return tree

    def test_count_nodes(self):
        # Testa a quantidade de nós da árvore.
        tree = self.create_tree_with_books()

        self.assertEqual(tree.count(), 7)

    def test_height(self):
        # Testa a altura da árvore.
        tree = self.create_tree_with_books()

        self.assertEqual(tree.height(), 3)

    def test_empty_tree_count_is_zero(self):
        # Testa a contagem de uma árvore vazia.
        tree = BinarySearchTree()

        self.assertEqual(tree.count(), 0)

    def test_empty_tree_height_is_zero(self):
        # Testa a altura de uma árvore vazia.
        tree = BinarySearchTree()

        self.assertEqual(tree.height(), 0)


if __name__ == "__main__":
    unittest.main()