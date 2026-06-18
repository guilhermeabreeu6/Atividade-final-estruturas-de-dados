from controllers.library_controller import LibraryController
from utils.input_helper import read_int
from views.menu_view import MenuView


class LibraryApp:
    def __init__(self):
        # Cria o controller responsável pelas ações do sistema.
        self.controller = LibraryController()
        self.view = MenuView()

    def run(self) -> None:
        # Mantém o sistema rodando até o usuário escolher sair.
        while True:
            self.view.show_main_menu()
            option = read_int("Choose an option: ")

            if option == 1:
                self.controller.handle_add_book()
            elif option == 2:
                self.controller.handle_search_book()
            elif option == 3:
                self.controller.handle_edit_book()
            elif option == 4:
                self.controller.handle_remove_book()
            elif option == 5:
                self.controller.handle_list_books()
            elif option == 6:
                self.controller.handle_tree_information()
            elif option == 0:
                self.view.show_message("Exiting application...")
                break
            else:
                self.view.show_message("Invalid option. Try again.")