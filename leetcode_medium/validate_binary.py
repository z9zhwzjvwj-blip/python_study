def isValidBST(self, root):
    """
    :type root: Optional[TreeNode]
    :rtype: bool
    """

    stack = [root]
    cur = root
    prev = None

    while cur or stack:
        while cur:
            stack.append(cur)
            cur = cur.left

        cur = stack.pop()
        if prev is not None and cur.val <= prev:
            return False

        prev = cur.val
        cur = cur.right

    return True
