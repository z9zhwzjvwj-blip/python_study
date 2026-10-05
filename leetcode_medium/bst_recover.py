# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def recoverTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: None Do not return anything, modify root in-place instead.
        """
        stack = []
        cur = root
        pre = None
        first = None
        second = None

        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left

            cur = stack.pop()

            if pre and cur.val < pre.val:
                if not first:
                    first = pre
                second = cur

            pre = cur
            cur = cur.right

        first.val, second.val = second.val, first.val

        return root
