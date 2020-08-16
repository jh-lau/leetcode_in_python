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
    def level_order_bottom(root):
        if not root:
            return []
        q, ans = [root], []
        while q:
            ans += [[n.val for n in q]]
            q = [k for n in q for k in ([n.left] if n.left else []) + ([n.right] if n.right else [])]

        return ans[::-1]
