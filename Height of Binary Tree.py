class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def find_height(root: TreeNode):
    if root is None:
        return 0
    return max(find_height(root.left), find_height(root.right)) + 1


root_node = TreeNode(10)
root_node.left = TreeNode(5)
root_node.right = TreeNode(15)
root_node.left.left = TreeNode(2)

print(find_height(root_node))