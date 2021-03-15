class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def tweak_identical(one: TreeNode, two: TreeNode):
    if one is None and two is None:
        return True
    elif one is None or two is None:
        return False
    elif one.val != two.val:
        return False
    return tweak_identical(one.left, two.left) & tweak_identical(one.right, two.right) \
           | tweak_identical(one.left, two.right) & tweak_identical(one.right, two.left)




