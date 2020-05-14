"""
  @Author       : liujianhan
  @Date         : 2020/5/14 上午11:49
  @Project      : leetcode_in_python
  @FileName     : 144.二叉树的前序遍历(M).py
  @Description  : 给定一个二叉树，返回它的 前序 遍历。
     示例:
    输入: [1,null,2,3]
       1
        \
         2
        /
       3

    输出: [1,2,3]
    进阶: 递归算法很简单，你可以通过迭代算法完成吗？
"""
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 44ms, 13.6MB
    @classmethod
    def preorder_traversal(cls, root: TreeNode) -> List[int]:
        if root is None:
            return []
        stack, output = [root, ], []
        while stack:
            root = stack.pop()
            if root is not None:
                output.append(root.val)
                if root.right is not None:
                    stack.append(root.right)
                if root.left is not None:
                    stack.append(root.left)

        return output

    # 44ms, 13.4MB
    @classmethod
    def preorder_traversal_v2(cls, root: TreeNode) -> List[int]:
        node, output = root, []
        while node:
            if not node.left:
                output.append(node.val)
                node = node.right
            else:
                predecessor = node.left

                while predecessor.right and predecessor.right is not node:
                    predecessor = predecessor.right

                if not predecessor.right:
                    output.append(node.val)
                    predecessor.right = node
                    node = node.left
                else:
                    predecessor.right = None
                    node = node.right

        return output
