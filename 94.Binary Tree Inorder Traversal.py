class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# Approach1: iterative
def inorder1(init_node: TreeNode):
    res = []
    stack = []
    curr = init_node
    while curr is not None or len(stack) > 0:
        while curr is not None:
            stack.push(curr)
            curr = curr.left
        curr = stack.pop()
        res.append(curr.val)
        curr = curr.right
    return res


# Approach2: recursive
def inorder2(init_node: TreeNode, res):
    if init_node is None:
        return
    inorder2(init_node.left, res)
    res.append(init_node.val)
    inorder2(init_node.right, res)


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.right = TreeNode(4)
root.right.left = TreeNode(5)
root.right.right = TreeNode(6)

result = []
inorder2(root, result)
print(result)