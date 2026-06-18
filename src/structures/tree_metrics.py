def count_nodes(root) -> int:
    # Conta quantos nós existem na árvore.
    if root is None:
        return 0

    return 1 + count_nodes(root.left) + count_nodes(root.right)


def calculate_height(root) -> int:
    # Calcula a altura da árvore.
    if root is None:
        return 0

    left_height = calculate_height(root.left)
    right_height = calculate_height(root.right)

    return 1 + max(left_height, right_height)