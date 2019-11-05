"""
  User: Liujianhan
  Time: 16:02
 """
__author__ = 'liujianhan'

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def min_depth(self, root):
        if not root:
            return 0
        if not root.left:
            return self.min_depth(root.right) + 1
        if not root.right:
            return self.min_depth(root.left) + 1

        return min(self.min_depth(root.left), self.min_depth(root.right)) + 1
