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
    def invert_tree(self, root):
        if not root:
            return root
        self.invert_tree(root.left)
        self.invert_tree(root.right)
        root.left, root.right = root.right, root.left
        return root
