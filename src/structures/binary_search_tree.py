from structures.tree_node import TreeNode
from structures.tree_traversal import in_order
from structures.tree_metrics import count_nodes, calculate_height


class BinarySearchTree:
    def __init__(self):
        # Raiz da árvore. Quando está None, a árvore está vazia.
        self.root = None

    def is_empty(self) -> bool:
        # Verifica se a árvore está vazia.
        return self.root is None

    def insert(self, value) -> None:
        # Insere um novo valor na árvore binária de busca.
        if self.root is None:
            self.root = TreeNode(value)
            return

        self.root = self._insert_recursive(self.root, value)

    def _insert_recursive(self, current_node, value):
        # Encontra a posição correta do novo valor usando recursividade.
        if current_node is None:
            return TreeNode(value)

        if value < current_node.value:
            current_node.left = self._insert_recursive(current_node.left, value)
        elif value > current_node.value:
            current_node.right = self._insert_recursive(current_node.right, value)
        else:
            raise ValueError("This value already exists in the tree.")

        return current_node

    def search(self, value):
        # Busca um valor dentro da árvore.
        return self._search_recursive(self.root, value)

    def _search_recursive(self, current_node, value):
        # Quando chega em None, significa que o valor não foi encontrado.
        if current_node is None:
            return None

        if value == current_node.value:
            return current_node.value

        if value < current_node.value:
            return self._search_recursive(current_node.left, value)

        return self._search_recursive(current_node.right, value)

    def remove(self, value) -> None:
        # Remove um valor da árvore mantendo a regra da árvore binária de busca.
        self.root = self._remove_recursive(self.root, value)

    def _remove_recursive(self, current_node, value):
        # Se o nó atual for None, o valor não existe na árvore.
        if current_node is None:
            raise ValueError("Value not found in the tree.")

        if value < current_node.value:
            current_node.left = self._remove_recursive(current_node.left, value)
            return current_node

        if value > current_node.value:
            current_node.right = self._remove_recursive(current_node.right, value)
            return current_node

        return self._remove_current_node(current_node)

    def _remove_current_node(self, current_node):
        # Caso 1: nó sem filhos.
        if current_node.left is None and current_node.right is None:
            return None

        # Caso 2: nó apenas com filho direito.
        if current_node.left is None:
            return current_node.right

        # Caso 2: nó apenas com filho esquerdo.
        if current_node.right is None:
            return current_node.left

        # Caso 3: nó com dois filhos.
        return self._remove_node_with_two_children(current_node)

    def _remove_node_with_two_children(self, current_node):
        # Substitui o valor removido pelo menor valor da subárvore direita.
        successor = self._find_min(current_node.right)
        current_node.value = successor.value
        current_node.right = self._remove_recursive(
            current_node.right,
            successor.value
        )

        return current_node

    def _find_min(self, current_node):
        # O menor valor sempre fica mais à esquerda.
        while current_node.left is not None:
            current_node = current_node.left

        return current_node

    def in_order(self) -> list:
        # Usa o percurso em ordem separado em outro arquivo.
        return in_order(self.root)

    def count(self) -> int:
        # Usa a contagem de nós separada em outro arquivo.
        return count_nodes(self.root)

    def height(self) -> int:
        # Usa o cálculo de altura separado em outro arquivo.
        return calculate_height(self.root)