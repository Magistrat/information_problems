class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def is_complete(root: TreeNode) -> bool:
    if not root:
        return True

    def depth(node):
        d = 0
        while node:
            d += 1
            node = node.left
        return d

    max_depth = depth(root)

    def check(node, current_depth):
        if not node:
            return current_depth == max_depth - 1

        if current_depth == max_depth - 1:
            # На предпоследнем уровне: листья или один левый ребёнок
            if not node.left and node.right:
                return False
            return True

        return check(node.left, current_depth + 1) and check(node.right, current_depth + 1)

    return check(root, 0)


if __name__ == '__main__':
    # Полное дерево:
    #        1
    #       / \
    #      2   3
    #     / \ /
    #    4  5 6
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)

    print(is_complete(root))  # True

    # Неполное дерево:
    #        1
    #       / \
    #      2   3
    #     / \   \
    #    4  5    7
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.right = TreeNode(7)

    print(is_complete(root))  # False (узел 3 имеет правого ребёнка, но нет левого)
