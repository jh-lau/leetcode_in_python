"""
  @Author       : liujianhan
  @Date         : 2020/9/25 9:48
  @Project      : leetcode_in_python
  @FileName     : 652.寻找重复的子树(M).py
  @Description  : 给定一棵二叉树，返回所有重复的子树。对于同一类的重复子树，你只需要返回其中任意一棵的根结点即可。
    两棵树重复是指它们具有相同的结构以及相同的结点值。
    示例 1：

            1
           / \
          2   3
         /   / \
        4   2   4
           /
          4
    下面是两个重复的子树：

          2
         /
        4
    和

        4
    因此，你需要以列表的形式返回上述重复子树的根结点。
"""

# Definition for a binary tree node.
from typing import List
from collections import defaultdict, Counter


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # 76ms, 16.9MB
    @staticmethod
    def find_duplicate_subtrees(root: TreeNode) -> List[TreeNode]:
        trees = defaultdict()
        trees.default_factory = trees.__len__
        count = Counter()
        ans = []

        def lookup(node):
            if node:
                uid = trees[node.val, lookup(node.left), lookup(node.right)]
                count[uid] += 1
                if count[uid] == 2:
                    ans.append(node)
                return uid

        lookup(root)
        return ans
