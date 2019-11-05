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
    def is_symmetric(self, root):
        if not root:
            return True
        return self.helper(root.left, root.right)

    def helper(self, left, right):
        if bool(left is None) != bool(right is None):
            return False
        elif left is None and right is None:
            return True
        elif left.val != right.val:
            return False

        return self.helper(left.left, right.right) and \
                self.helper(left.right, right.left)
