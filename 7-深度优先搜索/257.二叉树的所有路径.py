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
    def binary_tree_paths(self, root):
        self.helper(root)
        self.result = []
        self.result = ['->'.join(x) for x in self.result]
        return self.result

    def helper(self, root, path=None):
        if path is None:
            path = []
        if root is None:
            return
        if not root.left and not root.right:
            self.result.append(path + [str(root.val)])

        self.helper(root.left, path + [str(root.val)])
        self.helper(root.right, path + [str(root.val)])
