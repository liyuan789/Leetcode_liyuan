class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def deleteNode(root: TreeNode, val: int):
    # if root doesn't exist, just return it
    if root is None:
        return None

    # if key value is less than root value, find the node in the left subtree
    if root.val > val:
        root.left = deleteNode(root.left, val)

    # if key value is greater than root value, find the node in the right subtree
    elif root.val < val:
        root.right = deleteNode(root.right, val)

    # if we found node (root.value == val), start to delete it
    # Once the node is found, have to handle the below 4 cases
    # 1. node doesn't have left or right - return null
    # 2. node only has left subtree- return the left subtree
    # 3. node only has right subtree- return the right subtree
    # 4. node has both left and right - find the minimum value in the right subtree, set that value to the currently found node,
    # then recursively delete the minimum value in the right subtree 用最接近root.val的值替换root
    else:
        if not root.right:  # if it doesn't have right children, we delete the node then new root would be root.left
            return root.left
        if not root.left:   # if it doesn't have left children, we delete the node then new root would be root.right
            return root.right
        temp = root.right
        mini = temp.val
        while temp.left:
            temp = temp.left
            mini = temp.val
        root.val = mini  # replace value
        root.right = deleteNode(root.right, root.val)  # delete the minimum node in right subtree
    return root


root_node = TreeNode(5)
root_node.left = TreeNode(3)
root_node.right = TreeNode(7)
root_node.left.left = TreeNode(2)
root_node.left.right = TreeNode(4)
root_node.right.left = TreeNode(6)
root_node.right.right = TreeNode(8)

print(deleteNode(root_node, 7))
