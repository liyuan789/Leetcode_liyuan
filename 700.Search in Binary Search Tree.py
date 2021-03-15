class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# Method1: Recursive
def searchBST(root: TreeNode, val: int):
    if root is None or root.val == val:
        return root
    if val < root.val:
        return searchBST(root.left, val)
    else:
        return searchBST(root.right, val)


# Method2: Iterative
def searchII(root: TreeNode, val: int):
    cur = root
    while cur is not None and cur.val != val:
        if val < cur.val:
            cur = cur.left
        else:
            cur = cur.right
    return cur


root_node = TreeNode(5)
root_node.left = TreeNode(3)
root_node.right = TreeNode(7)
root_node.left.left = TreeNode(2)
root_node.left.right = TreeNode(4)
root_node.right.left = TreeNode(6)
root_node.right.right = TreeNode(8)

print(searchII(root_node, 7))