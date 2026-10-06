"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

from collections import deque


class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """

        def dfs(node):
            if not node or not node.left:
                return

            node.left.next = node.right

            if node.next:
                node.right.next = node.next.left

            dfs(node.left)
            dfs(node.right)

        dfs(root)

        return root
