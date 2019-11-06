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
    @staticmethod
    def lowest_common_ancestor(root, p, q):
        while root:
            if p.val < root.val > q.val:
                root = root.left
            elif p.val > root.val < q.val:
                root = root.right
            else:
                return root
            

        