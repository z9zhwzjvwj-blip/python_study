root = [1, None, 2, 3]


def inorderTraversal(root):
    """
    :type root: Optional[TreeNode]
    :rtype: List[int]
    """
    """trav = []

    def dfs(root):
        if root == None:
            return

        dfs(root.left)
        trav.append(root.val)
        dfs(root.right)
        return

    dfs(root)

    return trav"""
    result = []
    stack = []
    cur = root

    while cur or stack:
        while cur:
            stack.append(cur)
            cur = cur.left

        cur = stack.pop()
        result.append(cur.val)
        cur = cur.right

    return result
