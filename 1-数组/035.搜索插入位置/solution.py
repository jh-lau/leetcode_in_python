"""
  User: Liujianhan
 """
__author__ = 'liujianhan'


class Solution:
    @staticmethod
    def search_insert(nums, target):
        try:
            return nums.index(target)
        except ValueError:
            for i, num in enumerate(nums):
                if num > target:
                    return i
            return len(nums)
