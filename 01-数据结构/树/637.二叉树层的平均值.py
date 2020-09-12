"""
  @Author       : liujianhan
  @Date         : 20/9/12 13:57
  @Project      : leetcode_in_python
  @FileName     : 637.二叉树层的平均值.py
  @Description  : 给定一个非空二叉树, 返回一个由每层节点平均值组成的数组。
    示例 1：

    输入：
        3
       / \
      9  20
        /  \
       15   7
    输出：[3, 14.5, 11]
    解释：
    第 0 层的平均值是 3 ,  第1层是 14.5 , 第2层是 11 。因此返回 [3, 14.5, 11] 。

    提示：

    节点值的范围在32位有符号整数范围内。
"""
# Definition for a binary tree node.
from collections import deque
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 60ms, 16MB
    @staticmethod
    def average_of_levels(root: TreeNode) -> List[float]:
        averages = []
        queue = deque([root])
        while queue:
            total = 0
            size = len(queue)
            for _ in range(size):
                node = queue.popleft()
                total += node.val
                left, right = node.left, node.right
                if left:
                    queue.append(left)
                if right:
                    queue.append(right)
            averages.append(total / size)
        return averages


if __name__ == '__main__':
    root = TreeNode(3)
    t1, t2 = TreeNode(9), TreeNode(20)
    t3, t4 = TreeNode(15), TreeNode(7)
    root.left = t1
    root.right = t2
    t2.left, t2.right = t3, t4
    print(Solution.average_of_levels(root))
