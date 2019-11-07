"""
  Created by PyCharm.
  User: Liujianhan
  Date: 2019/5/28
  Time: 6:15
 """
__author__ = 'liujianhan'


class Solution:
    @staticmethod
    def move_zeroes(nums):
        """
        循环时，保证[0..i]中的所有非零元素都在[0...k]中，同时[k...i]为0
        :param nums: list
        :return: None
        """
        k = 0
        for i in range(len(nums)):
            if nums[i]:
                if k != i:
                    nums[k], nums[i] = nums[i], nums[k]
                    k += 1
                else:
                    k += 1


test = [0, 1, 13, 0, 132, 0, 9]
Solution.move_zeroes(test)
print(test)
