class Node:
    def __init__(self, value, color='RED', left=None, right=None, parent=None):
        self.value = value
        self.color = color
        self.left = left
        self.right = right
        self.parent = parent


def is_red_black_tree(root):
    if not root:
        return True  # Пустое дерево считается RB-сбалансированным

    # Свойство 2: Корень должен быть черным
    if root.color != 'BLACK':
        return False

    # Проверка всех свойств
    black_height = -1
    return check_rb_properties(root, 0, black_height)


def check_rb_properties(node, current_black_height, expected_black_height):
    if node is None:
        # Достигли листа (NIL), проверяем черную высоту
        if expected_black_height == -1:
            expected_black_height = current_black_height
        return current_black_height == expected_black_height

    # Увеличиваем черную высоту, если текущий узел черный
    if node.color == 'BLACK':
        current_black_height += 1
    elif node.color == 'RED':
        # Свойство 4: Оба потомка красного узла должны быть черными
        if (node.left and node.left.color != 'BLACK') or (node.right and node.right.color != 'BLACK'):
            return False
    else:
        # Недопустимый цвет узла
        return False

    # Рекурсивно проверяем левое и правое поддеревья
    left_ok = check_rb_properties(node.left, current_black_height, expected_black_height)
    right_ok = check_rb_properties(node.right, current_black_height, expected_black_height)

    return left_ok and right_ok


if __name__ == '__main__':
    # Пример корректного RB-дерева
    root = Node(10, 'BLACK')
    root.left = Node(5, 'RED')
    root.right = Node(20, 'RED')
    root.left.left = Node(3, 'BLACK')
    root.left.right = Node(7, 'BLACK')
    root.right.left = Node(15, 'BLACK')
    root.right.right = Node(25, 'BLACK')

    print(is_red_black_tree(root))  # True
