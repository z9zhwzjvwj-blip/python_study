class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def isSameTree(p, q):
    def same(x, y):
        if not x and not y:
            return True
        if not x or not y:
            return False

        if x.val == y.val:
            return same(x.left == y.left) and same(x.right == y.right)

        return False

    return same(p, q)
