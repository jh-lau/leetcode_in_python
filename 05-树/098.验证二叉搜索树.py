"""
  User: Liujianhan
 """
__author__ = 'liujianhan'


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def is_valid_BST(self, root):
        def in_order(root):
            if not root:
                return []
            left = in_order(root.left)
            right = in_order(root.right)
            return left + [root.val] + right

        in_order_list = in_order(root)
        for i in range(len(in_order_list) - 1):
            if in_order_list[i] >= in_order_list[i + 1]:
                return False
        return True
