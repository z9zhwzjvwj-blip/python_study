# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: List[List[int]]
        """
        paths = []
        if not root:
            return []

        stack = [(root, root.val, [root.val])]

        while stack:
            node, total, path = stack.pop()

            if not node.left and not node.right:
                if total == targetSum:
                    paths.append(path)

            if node.right:
                stack.append(
                    (node.right, total + node.right.val, path + [node.right.val])
                )

            if node.left:
                stack.append((node.left, total + node.left.val, path + [node.left.val]))

        return paths
