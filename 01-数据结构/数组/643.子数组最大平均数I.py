"""
  @Author       : liujianhan
  @Date         : 2020/11/19 11:03
  @Project      : leetcode_in_python
  @FileName     : 643.子数组最大平均数I.py
  @Description  : 给定 n 个整数，找出平均数最大且长度为 k 的连续子数组，并输出该最大平均数。
    示例 1:
    输入: [1,12,-5,-6,50,3], k = 4
    输出: 12.75
    解释: 最大平均数 (12-5-6+50)/4 = 51/4 = 12.75
    注意:
    1 <= k <= n <= 30,000。
    所给数据范围 [-10,000，10,000]。
"""
from typing import List


class Solution:
    # 超时
    @staticmethod
    def find_max_average(nums: List[int], k: int) -> float:
        return max([sum(nums[i:min(i + k, len(nums))]) for i in range(len(nums) - k + 1)]) / k

    # 944ms, 17.4MB
    @staticmethod
    def find_max_average_v2(nums: List[int], k: int) -> float:
        last_sum = sum(nums[:k])
        result = last_sum
        size = len(nums)
        for i in range(1, size - k + 1):
            last_sum += nums[i+k-1] - nums[i-1]
            result = max(result, last_sum)

        return result / k


if __name__ == '__main__':
    test_cases = [
        ([1, 12, -5, -6, 50, 3], 4),
        ([1, 12, -5, -6, 50, 32], 4),
        ([5], 1)
    ]
    for tc in test_cases:
        print(Solution.find_max_average(*tc))
        print(Solution.find_max_average_v2(*tc))
