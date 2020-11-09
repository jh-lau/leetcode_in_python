"""
  @Author       : liujianhan
  @Date         : 2020/11/9 11:12
  @Project      : leetcode_in_python
  @FileName     : 628.三个数的最大乘积.py
  @Description  : 给定一个整型数组，在数组中找出由三个数组成的最大乘积，并输出这个乘积。

    示例 1:

    输入: [1,2,3]
    输出: 6
    示例 2:

    输入: [1,2,3,4]
    输出: 24
    注意:

    给定的整型数组长度范围是[3,104]，数组中所有的元素范围是[-1000, 1000]。
    输入的数组中任意三个数的乘积不会超出32位有符号整数的范围。
"""
from typing import List


class Solution:
    # 88ms, 14.6MB
    @staticmethod
    def maximum_product(nums: List[int]) -> int:
        if len(nums) == 3:
            return nums[0] * nums[1] * nums[2]
        negative = [s for s in nums if s < 0]
        negative.sort()
        positive = [s for s in nums if s >= 0]
        positive.sort()
        if not positive:
            return negative[-3] * negative[-1] * negative[-2]
        elif len(positive) > 2:
            temp_max = positive[-3] * positive[-1] * positive[-2]
            if len(negative) > 1:
                fac = negative[1] * negative[0]
                return max(fac * positive[-1], temp_max)
            else:
                return temp_max

        else:
            fac = negative[0] * negative[1]
            return positive[-1] * fac

    # 68ms, 14.4MB
    @staticmethod
    def maximum_product_v2(nums: List[int]) -> int:
        nums.sort()
        if nums[-1] <= 0:
            return nums[-3]*nums[-2]*nums[-1]
        else:
            return max(nums[0]*nums[1], nums[-3]*nums[-2]) * nums[-1]


if __name__ == '__main__':
    test_cases = [
        [1, 2, 3],
        [-1, -2, -3, -4],
        [1, 2, 3, 4],
        [1, 2, -3, -4],
        [-1, 0, -3, -5],
        [1, 2, -3, -5],
        [1, 1, 2, -3, -5],
    ]
    for tc in test_cases:
        print(tc, Solution.maximum_product(tc))
        print(tc, Solution.maximum_product_v2(tc))
