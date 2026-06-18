class MenuView:
    def show_main_menu(self) -> None:
        # Exibe as opções principais do sistema.
        print("\n==== LIBRARY MANAGER BST ====")
        print("1 - Add book")
        print("2 - Search book")
        print("3 - Edit book")
        print("4 - Remove book")
        print("5 - List books")
        print("6 - Show tree information")
        print("0 - Exit")

    def show_book(self, book) -> None:
        # Exibe um livro na tela.
        print(book)

    def show_book_list(self, books: list) -> None:
        # Exibe a lista de livros ordenados pelo ID.
        if len(books) == 0:
            print("No books registered.")
            return

        print("\n-- Book list ordered by ID --")

        for book in books:
            print(book)

    def show_tree_information(self, total_books: int, tree_height: int) -> None:
        # Exibe informações básicas da árvore.
        print("\n-- Tree information --")
        print(f"Total books: {total_books}")
        print(f"Tree height: {tree_height}")

    def show_message(self, message: str) -> None:
        # Exibe uma mensagem simples para o usuário.
        print(message)