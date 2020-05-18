"""
  @Author       : liujianhan
  @Date         : 2020/5/18 上午11:23
  @Project      : leetcode_in_python
  @FileName     : 152.乘积最大子数组(M).py
  @Description  : 给你一个整数数组 nums ，请你找出数组中乘积最大的连续子数组（该子数组中至少包含一个数字），并返回该子数组所对应的乘积。
    示例 1:
    输入: [2,3,-2,4]
    输出: 6
    解释: 子数组 [2,3] 有最大乘积 6。
    示例 2:
    输入: [-2,0,-1]
    输出: 0
    解释: 结果不能为 2, 因为 [-2,-1] 不是子数组。
"""
from typing import List


class Solution:
    # 44ms, 14.6MB
    @classmethod
    def max_product(cls, nums: List[int]) -> int:
        reverse = nums[::-1]
        for i in range(1, len(nums)):
            nums[i] *= nums[i - 1] or 1  # or 1的作用，当nums[i-1]为0时，nums[i]取本身数值，不累乘前面数组，即乘等自身
            reverse[i] *= reverse[i - 1] or 1

        return max(max(nums), max(reverse))

    # 52ms, 13.9MB
    @classmethod
    def max_product_v2(cls, nums: List[int]) -> int:
        """DP"""
        n = len(nums)
        a = b = 1
        ans = float('-inf')

        for i in range(1, n + 1):
            temp = a
            a = max(a * nums[i - 1], b * nums[i - 1], nums[i - 1])
            b = min(temp * nums[i - 1], b * nums[i - 1], nums[i - 1])
            ans = max(ans, a)

        return ans


if __name__ == '__main__':
    test_cases = [
        [2, 3, -2, 4],
        [-2, 0, -1]
    ]
    for tc in test_cases:
        # print(Solution.max_product(tc))
        print(Solution.max_product_v2(tc))
