"""
  User: Liujianhan
 """
__author__ = 'liujianhan'


class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children


class Solution:
    def max_depth(self, root) -> int:
        if not root:
            return 0
        depth, temp = 0, [root]
        while temp:
            depth += 1
            temp = [i for node in temp for i in node.children]
        return depth
