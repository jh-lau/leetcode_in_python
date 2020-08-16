"""
  @Author       : Liujianhan
  @Date         : 20/8/2 0:50
  @FileName     : 590.N叉树的后序遍历.py
  @ProjectName  : leetcode_in_python
  @Description  : 给定一个 N 叉树，返回其节点值的后序遍历。
    例如，给定一个 3叉树 :
    返回其后序遍历: [5,6,3,2,4,1].
    说明: 递归法很简单，你可以使用迭代法完成此题吗?
 """

# Definition for a Node.
from typing import List


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    # 72ms, 15.6MB
    @staticmethod
    def post_order(root: 'Node') -> List[int]:
        if not root:
            return []
        stack, output = [root, ], []
        while stack:
            root = stack.pop()
            if root is not None:
                output.append(root.val)
            for c in root.children:
                stack.append(c)

        return output[::-1]
