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
    def max_depth(self, root):
        return 0 if not root else max(self.max_depth(root.left), self.max_depth(root.right)) + 1
