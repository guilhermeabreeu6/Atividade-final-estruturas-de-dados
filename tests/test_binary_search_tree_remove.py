import os
import sys
import unittest

# Adiciona a pasta src no caminho de importação.
# Isso permite importar as classes do projeto nos testes.
sys.path.insert(
    0,
    os.path.abspath(os.path.join(os.path.dirname(__file__), "../src"))
)

from models.book import Book
from structures.binary_search_tree import BinarySearchTree


class TestBinarySearchTreeRemove(unittest.TestCase):
    def create_book(self, book_id: int) -> Book:
        # Cria um livro simples para ser usado nos testes.
        return Book(book_id, f"Book {book_id}", "Test Author", 2026)

    def create_tree_with_books(self) -> BinarySearchTree:
        # Monta uma árvore para testar os casos de remoção.
        tree = BinarySearchTree()

        for book_id in [10, 5, 15, 3, 7, 12, 18]:
            tree.insert(self.create_book(book_id))

        return tree

    def get_book_ids(self, books: list) -> list:
        # Retorna apenas os IDs para facilitar a comparação.
        return [book.book_id for book in books]

    def test_remove_leaf_node(self):
        # Remove um nó folha, ou seja, sem filhos.
        tree = self.create_tree_with_books()

        tree.remove(self.create_book(3))

        self.assertEqual(
            self.get_book_ids(tree.in_order()),
            [5, 7, 10, 12, 15, 18]
        )

    def test_remove_node_with_one_child(self):
        # Remove um nó com apenas um filho.
        tree = BinarySearchTree()

        for book_id in [10, 5, 15, 3]:
            tree.insert(self.create_book(book_id))

        tree.remove(self.create_book(5))

        self.assertEqual(
            self.get_book_ids(tree.in_order()),
            [3, 10, 15]
        )

    def test_remove_node_with_two_children(self):
        # Remove um nó com dois filhos.
        # Esse é o caso mais importante da remoção.
        tree = self.create_tree_with_books()

        tree.remove(self.create_book(10))

        self.assertEqual(
            self.get_book_ids(tree.in_order()),
            [3, 5, 7, 12, 15, 18]
        )

    def test_remove_not_found_raises_error(self):
        # Testa se remover um livro inexistente gera erro.
        tree = self.create_tree_with_books()

        with self.assertRaises(ValueError):
            tree.remove(self.create_book(99))


if __name__ == "__main__":
    unittest.main()