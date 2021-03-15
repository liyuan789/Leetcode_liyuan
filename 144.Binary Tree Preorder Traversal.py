class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# Approach1: iterative
# 思路：用stack暂存下一层要被遍历的node,不断的 append 再 pop 出来

def preorder1(init_node: TreeNode):

    if init_node is None:
        return []

    stack = [init_node]  # stack存 下一层要被遍历的 root node
    output = []

    while stack is not None and len(stack) != 0:
        node = stack.pop()
        output.append(node.val)
        if node.right is not None:
            stack.append(node.right)  # 注意 append 的顺序正好跟 pop 的顺序相反
        if node.left is not None:
            stack.append(node.left)

    return output


root = TreeNode(1)
root.right = TreeNode(2)
root.right.left = TreeNode(3)

print(preorder1(root))


# Approach2: recursive

# def preorder2(init_node: TreeNode):
#     res = []
#     helper(init_node, res)
#     return res


def helper(node: TreeNode, res):
    if node is None:
        return
    res.append(node.val)
    helper(node.left, res)
    helper(node.right, res)


root = TreeNode(1)
root.right = TreeNode(2)
root.right.left = TreeNode(3)

result = []
helper(root, result)
print(result)