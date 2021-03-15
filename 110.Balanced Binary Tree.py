class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# Method1: O(n*log(n)) worst case: is balanced tree

def getHeight(root: TreeNode):
    if root is None:
        return 0
    return max(getHeight(root.left), getHeight(root.right)) + 1


def isBalanced1(root: TreeNode):
    # base case
    if root is None:
        return True
    # recursive rule
    left_height = getHeight(root.left)
    right_height = getHeight(root.right)
    if abs(left_height - right_height) > 1:   # check if root is balanced
        return False
    return isBalanced1(root.left) & isBalanced1(root.right)  # check root.left and root.right


# Method2: O(n)
def height(root: TreeNode):
    if root is None:
        return 0
    left_height = height(root.left)
    if left_height == -1:
        return -1
    right_height = height(root.right)
    if right_height == -1:
        return -1
    if abs(left_height - right_height) > 1:
        return -1
    return max(left_height, right_height) + 1


def isBalanced2(root: TreeNode):
    # base case
    if root is None:
        return True
    return height(root) != -1


root_node = TreeNode(10)
root_node.left = TreeNode(5)
root_node.right = TreeNode(15)
root_node.left.left = TreeNode(2)

print(isBalanced2(root_node))