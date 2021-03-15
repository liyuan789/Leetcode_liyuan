class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def getRange(root: TreeNode, mini: int, maxi: int):
    res = []
    Range(root, mini, maxi, res)
    return res


def Range(root: TreeNode, low, high, res):
    if root is None:
        return

    # determine if left subtree should be traversed
    # when root.val > low
    if root.val > low:
        Range(root.left, low, high, res)

    # determine if root should be traversed
    if low <= root.val <= high:
        res.append(root.val)

    # determine if right subtree should be traversed
    # when root.val < high
    if root.val < high:
        Range(root.right, low, high, res)


root_node = TreeNode(5)
root_node.left = TreeNode(3)
root_node.right = TreeNode(7)
root_node.left.left = TreeNode(2)
root_node.left.right = TreeNode(4)
root_node.right.left = TreeNode(6)
root_node.right.right = TreeNode(8)

print(getRange(root_node, 2, 5))