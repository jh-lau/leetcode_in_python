"""
  User: Liujianhan
  Time: 16:02
 """
__author__ = 'liujianhan'
from collections import defaultdict
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    result = 0
    def path_sum(self, root, sum):
        if not root:
            return 0

        freq = defaultdict(int)
        freq[0] = 1
        self.dfs(root, 0, freq, sum)
        return self.result

    def dfs(self, node, path_sum, freq, sum):
        if node:
            path_sum += node.val
            self.result += freq[path_sum - sum]
            freq[path_sum] += 1

            self.dfs(node.left, path_sum, freq, sum)
            self.dfs(node.right, path_sum, freq, sum)

            freq[path_sum] -= 1
