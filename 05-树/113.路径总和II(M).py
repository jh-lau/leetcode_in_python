"""
  @Author       : Liujianhan
  @Date         : 20/5/8 22:15
  @FileName     : 113.路径总和II(M).py
  @ProjectName  : leetcode_in_python
  @Description  : 给定一个二叉树和一个目标和，找到所有从根节点到叶子节点路径总和等于给定目标和的路径。
    说明: 叶子节点是指没有子节点的节点。
    示例:
    给定如下二叉树，以及目标和 sum = 22，

                  5
                 / \
                4   8
               /   / \
              11  13  4
             /  \    / \
            7    2  5   1
    返回:
    [
       [5,4,11,2],
       [5,8,4,5]
    ]
 """
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 60ms, 18.9MB
    @classmethod
    def path_sum(cls, root: TreeNode, sum_: int) -> List[List[int]]:
        res = []

        def dfs(root, tmp, sum_):
            if not root:
                return
            if not root.left and not root.right and root.val == sum_:
                tmp += [root.val]
                nonlocal res
                res.append(tmp)
            dfs(root.left, tmp + [root.val], sum_ - root.val)
            dfs(root.right, tmp + [root.val], sum_ - root.val)

        dfs(root, [], sum_)

        return res
