"""
  @Author       : Liujianhan
  @Date         : 20/5/6 22:29
  @FileName     : 094.二叉树的中序遍历(M).py
  @ProjectName  : leetcode_in_python
  @Description  : 给定一个二叉树，返回它的中序 遍历。
    示例:
    输入: [1,null,2,3]
       1
        \
         2
        /
       3

    输出: [1,3,2]
    进阶: 递归算法很简单，你可以通过迭代算法完成吗？
 """

# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 36ms, 13.6MB
    @classmethod
    def inorder_traversal(cls, root: TreeNode) -> List[int]:
        stack, rst = [root], []
        while stack:
            i = stack.pop()
            if isinstance(i, TreeNode):
                stack.extend([i.right, i.val, i.left])
            elif isinstance(i, int):
                rst.append(i)

        return rst
