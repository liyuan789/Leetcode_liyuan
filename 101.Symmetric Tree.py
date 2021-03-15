class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def symmetric(root: TreeNode):
    if root is None:
        return True
    return is_symmetric(root.left, root.right)


def is_symmetric(one: TreeNode, two: TreeNode):
    if one is None and two is None:
        return True
    elif one is None or two is None:
        return False
    elif one.val != two.val:
        return False
    return is_symmetric(one.left, two.right) & is_symmetric(one.right, two.left)


root_node = TreeNode(2)
root_node.left = TreeNode(4)
root_node.right = TreeNode(4)
root_node.left.right = TreeNode(8)
root_node.right.left = TreeNode(8)

print(symmetric(root_node))