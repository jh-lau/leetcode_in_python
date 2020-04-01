"""
  User: Liujianhan
  Time: 15:51
 """
__author__ = 'liujianhan'


class Solution:
    @staticmethod
    def remove_element(nums, val):
        while val in nums:
            nums.remove(val)
        return len(nums)

    @staticmethod
    def remove_element_2(nums, val):
        k = 0
        for i, num in enumerate(nums):
            if num != val:
                if i != k:
                    nums[k] = num
                    k += 1
                else:
                    k += 1
        return k
