"""
  @Author       : liujianhan
  @Date         : 2020/9/21 19:51
  @Project      : leetcode_in_python
  @FileName     : 538.把二叉搜索树转换为累加树.py
  @Description  : 给定一个二叉搜索树（Binary Search Tree），把它转换成为累加树（Greater Tree)，
    使得每个节点的值是原来的节点值加上所有大于它的节点值之和。
    例如：

    输入: 原始二叉搜索树:
                  5
                /   \
               2     13

    输出: 转换为累加树:
                 18
                /   \
              20     13
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 72ms, 15.4MB
    @staticmethod
    def convert_BST(root: TreeNode) -> TreeNode:
        bn = None

        def helper(node):
            nonlocal bn
            if node.right:
                helper(node.right)
            if bn:
                node.val += bn.val
            bn = node
            if node.left:
                helper(node.left)
            return node.val

        if root:
            helper(root)
        return root

    # 88ms, 15.5MB
    @staticmethod
    def convert_BST_v2(root: TreeNode) -> TreeNode:
        stack, bn, cur = [], 0, root
        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.right
            if stack:
                this = stack.pop()
                bn += this.val
                this.val = bn
                cur = this.left
        return root
