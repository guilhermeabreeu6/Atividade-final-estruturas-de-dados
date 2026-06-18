def in_order(root) -> list:
    # Retorna os valores da árvore em ordem crescente.
    values = []
    _in_order_recursive(root, values)
    return values


def _in_order_recursive(current_node, values: list) -> None:
    # Percurso em ordem: esquerda, raiz e direita.
    if current_node is None:
        return

    _in_order_recursive(current_node.left, values)
    values.append(current_node.value)
    _in_order_recursive(current_node.right, values)