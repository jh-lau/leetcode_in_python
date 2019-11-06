"""
  User: Liujianhan
  Time: 16:02
 """
__author__ = 'liujianhan'


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def sorted_array_to_BST(self, nums):
        return self._sorted_array_to_BST(nums, 0, len(nums) - 1)

    def _sorted_array_to_BST(self, nums, start, end):
        if start > end:
            return None

        mid = start + (end - start) // 2
        mid_node = TreeNode(nums[mid])
        mid_node.left = self._sorted_array_to_BST(nums, start, mid - 1)
        mid_node.right = self._sorted_array_to_BST(nums, mid + 1, end)
        return mid_node
