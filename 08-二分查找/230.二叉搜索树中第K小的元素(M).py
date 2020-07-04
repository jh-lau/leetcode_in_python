"""
  @Author       : Liujianhan
  @Date         : 20/7/4 21:55
  @FileName     : 230.二叉搜索树中第K小的元素(M).py
  @ProjectName  : leetcode_in_python
  @Description  : 给定一个二叉搜索树，编写一个函数 kthSmallest 来查找其中第 k 个最小的元素。
    说明：
    你可以假设 k 总是有效的，1 ≤ k ≤ 二叉搜索树元素个数。
    示例 1:
    输入: root = [3,1,4,null,2], k = 1
       3
      / \
     1   4
      \
       2
    输出: 1
    示例 2:
    输入: root = [5,3,6,2,4,null,null,1], k = 3
           5
          / \
         3   6
        / \
       2   4
      /
     1
    输出: 3
    进阶：
    如果二叉搜索树经常被修改（插入/删除操作）并且你需要频繁地查找第 k 小的值，你将如何优化 kthSmallest 函数？
 """

# Definition for a binary tree node.
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # 56ms, 17.9MB
    @staticmethod
    def kth_smallest(root: TreeNode, k: int) -> int:
        count = 0
        stack = deque()
        node = root
        while node is not None:
            stack.append(node)
            node = node.left
        while len(stack) != 0:
            node = stack.pop()
            count += 1
            if count == k:
                return node.val
            node = node.right
            while node is not None:
                stack.append(node)
                node = node.left

        return None


if __name__ == '__main__':
    pass
