class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def tree_height(root: TreeNode) -> int:
    if not root:
        return 0  # или -1, если считать по рёбрам
    left_height = tree_height(root.left)
    right_height = tree_height(root.right)
    return 1 + max(left_height, right_height)


if __name__ == '__main__':
    # Пример дерева:
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

    print(tree_height(root))  # Output: 3 (по узлам: 1→2→4)
