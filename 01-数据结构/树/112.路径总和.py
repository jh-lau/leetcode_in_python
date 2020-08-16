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
    def has_path_sum(self, root, result):
        if not root:
            return False

        if not (root.left or root.right):
            return result == root.val

        return self.has_path_sum(root.left, result - root.val) or self.has_path_sum(root.right, result - root.val)
