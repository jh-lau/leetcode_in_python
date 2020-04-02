"""
  Created by PyCharm.
  User: Liujianhan
  Date: 2019/3/30
  Time: 13:04
 """
__author__ = 'liujianhan'
from data_structure.function_process_time import RuntimeTest


class Solution:
    @staticmethod
    @RuntimeTest()
    def two_sum(nums, target):
        d = {}
        for i, num in enumerate(nums):
            n = target - num
            if n in d:
                return [d[n], i]
            d[num] = i
        return False


if __name__ == '__main__':
    test_1 = [3, 2, 4, 12, -1, 6]
    test = [3, 3]
    result = Solution().two_sum(test_1, 6)
