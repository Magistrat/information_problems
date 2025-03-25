class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def is_balanced(root: TreeNode) -> bool:
    def check_height(node):
        if not node:
            return 0

        left_height = check_height(node.left)
        if left_height == -1:
            return -1

        right_height = check_height(node.right)
        if right_height == -1:
            return -1

        if abs(left_height - right_height) > 1:
            return -1

        return max(left_height, right_height) + 1

    return check_height(root) != -1


if __name__ == '__main__':
    # Сбалансированное дерево:
    #       1
    #      / \
    #     2   3
    #    / \
    #   4   5
    root = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3))
    print(is_balanced(root))  # True

    # Несбалансированное дерево:
    #       1
    #      /
    #     2
    #    /
    #   3
    root = TreeNode(1, TreeNode(2, TreeNode(3)))
    print(is_balanced(root))  # False
