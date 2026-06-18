from services.library_service import LibraryService
from utils.input_helper import read_int, read_text
from views.menu_view import MenuView


class LibraryController:
    def __init__(self):
        # Controller liga a entrada do usuário com as regras do sistema.
        self.service = LibraryService()
        self.view = MenuView()

    def handle_add_book(self) -> None:
        # Coleta os dados e solicita o cadastro ao service.
        book_id = read_int("Book ID: ")
        title = read_text("Title: ")
        author = read_text("Author: ")
        year = read_int("Year: ")

        try:
            self.service.add_book(book_id, title, author, year)
            self.view.show_message("Book added successfully.")
        except ValueError as error:
            self.view.show_message(str(error))

    def handle_search_book(self) -> None:
        # Busca um livro pelo ID.
        book_id = read_int("Book ID to search: ")
        book = self.service.find_book_by_id(book_id)

        if book is None:
            self.view.show_message("Book not found.")
            return

        self.view.show_message("Book found:")
        self.view.show_book(book)

    def handle_edit_book(self) -> None:
        # Edita os dados de um livro existente.
        book_id = read_int("Book ID to edit: ")

        title = read_text("New title: ")
        author = read_text("New author: ")
        year = read_int("New year: ")

        updated = self.service.update_book(book_id, title, author, year)

        if not updated:
            self.view.show_message("Book not found.")
            return

        self.view.show_message("Book updated successfully.")

    def handle_remove_book(self) -> None:
        # Remove um livro usando a função remove da árvore.
        book_id = read_int("Book ID to remove: ")
        removed = self.service.remove_book(book_id)

        if not removed:
            self.view.show_message("Book not found.")
            return

        self.view.show_message("Book removed successfully.")

    def handle_list_books(self) -> None:
        # Lista todos os livros usando percurso em ordem.
        books = self.service.list_books()
        self.view.show_book_list(books)

    def handle_tree_information(self) -> None:
        # Mostra informações sobre a árvore.
        total_books = self.service.count_books()
        tree_height = self.service.tree_height()

        self.view.show_tree_information(total_books, tree_height)