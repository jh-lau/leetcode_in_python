"""
  @Author       : liujianhan
  @Date         : 2020/5/14 下午12:00
  @Project      : leetcode_in_python
  @FileName     : 145.二叉树的后续遍历(H).py
  @Description  : 给定一个二叉树，返回它的 后序 遍历。
    示例:
    输入: [1,null,2,3]
       1
        \
         2
        /
       3

    输出: [3,2,1]
    进阶: 递归算法很简单，你可以通过迭代算法完成吗？
"""
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 36ms, 13.8MB
    @classmethod
    def postorder_traversal(cls, root: TreeNode) -> List[int]:
        if root is None:
            return []

        stack, output = [root, ], []
        while stack:
            root = stack.pop()
            output.append(root.val)
            if root.left is not None:
                stack.append(root.left)
            if root.right is not None:
                stack.append(root.right)

        return output[::-1]