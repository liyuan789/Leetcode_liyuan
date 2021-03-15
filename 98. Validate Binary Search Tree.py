import math


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# Approach1: Recursive Traversal with Valid Range
def isValidBST(root: TreeNode):
    low = -math.inf
    high = math.inf
    return validate(root, low, high)


def validate(root: TreeNode, mini, maxi) -> bool:

    # Empty trees are valid BSTs
    if root is None:
        return True

    # The current node's value must be between min and max
    if root.val <= mini or root.val >= maxi:
        return False

    # The left and right subtree must also be valid
    return validate(root.left, mini, root.val) and validate(root.right, root.val, maxi)


root_node = TreeNode(5)
root_node.left = TreeNode(1)
root_node.right = TreeNode(4)
root_node.right.left = TreeNode(3)
root_node.right.right = TreeNode(6)

print(isValidBST(root_node))


# Approach2: iterative traversal with valid range
def validBST(root: TreeNode):
    if root is None:
        return True
    stack = [(root, -math.inf, math.inf)]
    while stack:
        root, lower, upper = stack.pop()
        if root is None:
            continue
        if root.val <= lower or root.val >= upper:
            return False
        stack.append((root.right, root.val, upper))
        stack.append((root.left, lower, root.val))
    return True



