class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# Method1: Recursive
def insertBST(root: TreeNode, val: int):
    if root is None:
        return TreeNode(val)
    if val < root.val:
        root.left = insertBST(root.left, val)
    elif val > root.val:
        root.right = insertBST(root.right, val)
    return root


# Method2: Iterative
def insertBSTII(root: TreeNode, val: int):
    if root is None:
        return TreeNode(val)
    cur = root
    while cur.val != val:
        if val < cur.val:
            if cur.left is None:
                cur.left = TreeNode(val)
            cur = cur.left
        else:
            if cur.right is None:
                cur.right = TreeNode(val)
            cur = cur.right
    return root


root_node = TreeNode(5)
root_node.left = TreeNode(3)
root_node.right = TreeNode(7)
root_node.left.left = TreeNode(2)
root_node.left.right = TreeNode(4)
root_node.right.left = TreeNode(6)
root_node.right.right = TreeNode(8)

insertBST(root_node, 9)

