"""
  User: Liujianhan
 """
__author__ = 'liujianhan'


class Solution:
    @staticmethod
    def max_sub_array(nums):
        for i in range(1, len(nums)):
            if nums[i - 1] > 0:
                nums[i] += nums[i - 1]
        print(nums)
        return max(nums)


test = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(Solution().max_sub_array(test))
