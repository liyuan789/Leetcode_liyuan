class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def postorder(init_node):
    res = []
    helper(init_node, res)
    return res


def helper(init_node, res):
    if init_node is None:
        return
    helper(init_node.left, res)
    helper(init_node.right, res)
    res.append(init_node.val)


root = TreeNode(2)
root.left = TreeNode(4)
root.right = TreeNode(6)
root.left.right = TreeNode(8)
root.right.right = TreeNode(10)

print(postorder(root))


