"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""


class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """

        def dfs(node):
            if not node:
                return

            if node.left and node.right:
                node.left.next = node.right

            child = node.right if node.right else node.left

            if child:
                p = node.next
                while p:
                    if p.left:
                        child.next = p.left
                        break
                    if p.right:
                        child.next = p.right
                        break
                    p = p.next

            dfs(node.right)
            dfs(node.left)

        dfs(root)

        return root
