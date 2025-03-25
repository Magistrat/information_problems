class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def is_avl_balanced(root: TreeNode) -> bool:
    def check_avl(node):
        if not node:
            return (True, 0)  # (is_balanced, height)

        left_balanced, left_height = check_avl(node.left)
        if not left_balanced:
            return (False, 0)

        right_balanced, right_height = check_avl(node.right)
        if not right_balanced:
            return (False, 0)

        if abs(left_height - right_height) > 1:
            return (False, 0)

        current_height = max(left_height, right_height) + 1
        return (True, current_height)

    is_balanced, _ = check_avl(root)
    return is_balanced


if __name__ == '__main__':
    # Пример 1: АВЛ-сбалансированное дерево
    #       10
    #      /  \
    #     5    20
    #    / \
    #   2   7
    root = TreeNode(10, TreeNode(5, TreeNode(2), TreeNode(7)), TreeNode(20))
    print(is_avl_balanced(root))  # True

    # Пример 2: Не АВЛ-сбалансированное дерево
    #       10
    #      /
    #     5
    #    /
    #   2
    root = TreeNode(10, TreeNode(5, TreeNode(2)))
    print(is_avl_balanced(root))  # False
