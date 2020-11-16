"""
  @Author       : liujianhan
  @Date         : 2020/11/16 10:33
  @Project      : leetcode_in_python
  @FileName     : 589.N叉树的前序遍历.py
  @Description  : 给定一个 N 叉树，返回其节点值的前序遍历。
"""
# Definition for a Node.
from typing import List


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    # 52ms, 15.5MB
    @staticmethod
    def preorder(root: 'Node') -> List[int]:
        if root is None:
            return []
        stack, output = [root, ], []
        while stack:
            root = stack.pop()
            output.append(root.val)
            stack.extend(root.children[::-1])

        return output


if __name__ == '__main__':
    pass
