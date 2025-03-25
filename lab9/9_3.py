class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def is_perfect(root: TreeNode) -> bool:
    def depth(node):
        if not node:
            return 0
        return 1 + depth(node.left)  # Все листья на одном уровне ⇒ достаточно левой ветви

    def check(node, current_depth, target_depth):
        if not node:
            return current_depth == target_depth
        if not node.left and not node.right:
            return current_depth + 1 == target_depth
        if not node.left or not node.right:
            return False
        return (check(node.left, current_depth + 1, target_depth) and
                check(node.right, current_depth + 1, target_depth))

    if not root:
        return True
    target_depth = depth(root)
    return check(root, 0, target_depth)


if __name__ == '__main__':
    # Идеальное дерево:
    #        1
    #       / \
    #      2   3
    #     / \ / \
    #    4  5 6 7
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)

    print(is_perfect(root))  # True

    # Неидеальное дерево:
    #        1
    #       / \
    #      2   3
    #     / \
    #    4   5
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)

    print(is_perfect(root))  # False