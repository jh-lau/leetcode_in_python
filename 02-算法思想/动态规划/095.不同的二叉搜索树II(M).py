"""
  @Author       : Liujianhan
  @Date         : 20/5/6 22:33
  @FileName     : 095.不同的二叉搜索树II(M).py
  @ProjectName  : leetcode_in_python
  @Description  : 给定一个整数 n，生成所有由 1 ... n 为节点所组成的二叉搜索树。
    示例:
    输入: 3
    输出:
    [
      [1,null,3,2],
      [3,2,null,1],
      [3,1,null,null,2],
      [2,1,3],
      [1,null,2,null,3]
    ]
    解释:
    以上的输出对应以下 5 种不同结构的二叉搜索树：

       1         3     3      2      1
        \       /     /      / \      \
         3     2     1      1   3      2
        /     /       \                 \
       2     1         2                 3
 """

# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 72ms, 15.1MB
    @classmethod
    def generate_trees(cls, n: int) -> List[TreeNode]:
        def helper(start, end):
            if start > end:
                return [None, ]
            all_trees = []
            for i in range(start, end + 1):
                left_trees = helper(start, i - 1)
                right_trees = helper(i + 1, end)

                for l in left_trees:
                    for r in right_trees:
                        current_tree = TreeNode(i)
                        current_tree.left = l
                        current_tree.right = r
                        all_trees.append(current_tree)

            return all_trees

        return helper(1, n) if n else []
