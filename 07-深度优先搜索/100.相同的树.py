"""
  User: Liujianhan
  Time: 15:51
 """
__author__ = 'liujianhan'


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def is_same_tree(self, p, q):
        if p and q:
            return p.val == q.val and self.is_same_tree(p.left, q.left) and \
            self.is_same_tree(q.right, p.right)
        if p is None and q is None:
            return True
        else:
            return False