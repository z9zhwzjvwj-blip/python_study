# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: TreeNode | None) -> int:
        sumNum = 0

        # recursive calls return the path
        def dfs(node, num):

            nonlocal sumNum

            if not node:
                return 0

            num = 10 * num + node.val

            if not node.left and not node.right:
                sumNum += num
                return

            dfs(node.left, num)
            dfs(node.right, num)

        dfs(root, 0)
        return sumNum
