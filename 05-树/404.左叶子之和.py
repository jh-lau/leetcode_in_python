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
    def sum_of_left_leaves(self, root):
        result = 0
        if not root:
            return 0

        if root.left and root.left.left is None and root.left.right is None:
            result += root.left.val

        result += self.sum_of_left_leaves(root.left) + self.sum_of_left_leaves(root.right)
        return result
