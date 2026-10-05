# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        # print("left: ", root.left.val, "right: ", root.right.val)
        # left none + right none => true
        # left none + right not none => false

        stack_in = []
        stack_rev = []
        cur_in = root.left
        cur_rev = root.right

        while cur_in or cur_rev or stack_in or stack_rev:
            while cur_in or cur_rev:
                if (not cur_in and cur_rev) or (not cur_rev and cur_in):
                    return False
                stack_in.append(cur_in)
                cur_in = cur_in.left
                stack_rev.append(cur_rev)
                cur_rev = cur_rev.right

            cur_in = stack_in.pop()
            cur_rev = stack_rev.pop()

            if cur_in.val != cur_rev.val:
                return False

            cur_in = cur_in.right
            cur_rev = cur_rev.left

        return True
