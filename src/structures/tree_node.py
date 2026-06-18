class TreeNode:
    def __init__(self, value):
        # Guarda o valor principal do nó.
        self.value = value

        # Referência para o filho da esquerda.
        # Na árvore binária de busca, aqui ficam os valores menores.
        self.left = None

        # Referência para o filho da direita.
        # Na árvore binária de busca, aqui ficam os valores maiores.
        self.right = None