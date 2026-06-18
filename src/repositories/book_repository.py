import json
import os

from models.book import Book


class BookRepository:
    def __init__(self, file_path: str = "data/books.json"):
        # Caminho do arquivo onde os livros serão salvos.
        self.file_path = file_path

        # Garante que a pasta data exista antes de salvar ou carregar.
        self._ensure_data_folder_exists()

    def _ensure_data_folder_exists(self) -> None:
        # Cria a pasta data caso ela ainda não exista.
        folder = os.path.dirname(self.file_path)

        if folder and not os.path.exists(folder):
            os.makedirs(folder)

    def load_books(self) -> list:
        # Carrega os livros salvos no arquivo JSON.
        if not os.path.exists(self.file_path):
            return []

        with open(self.file_path, "r", encoding="utf-8") as file:
            content = file.read().strip()

            if content == "":
                return []

            books_data = json.loads(content)

        return [Book.from_dict(book_data) for book_data in books_data]

    def save_books(self, books: list) -> None:
        # Salva a lista de livros no arquivo JSON.
        books_data = [book.to_dict() for book in books]

        with open(self.file_path, "w", encoding="utf-8") as file:
            json.dump(books_data, file, indent=4, ensure_ascii=False)