"""
  @Author       : liujianhan
  @Date         : 2020/11/10 10:16
  @Project      : leetcode_in_python
  @FileName     : 485.最大连续1的个数.py
  @Description  : 给定一个二进制数组， 计算其中最大连续1的个数。
    示例 1:
    输入: [1,1,0,1,1,1]
    输出: 3
    解释: 开头的两位和最后的三位都是连续1，所以最大连续1的个数是 3.
    注意：
    输入的数组只包含 0 和1。
    输入数组的长度是正整数，且不超过 10,000。
"""
from typing import List


class Solution:
    # 460ms, 13.8MB
    @staticmethod
    def find_max_consecutive_ones(nums: List[int]) -> int:
        current, duration = 0, 0
        for num in nums:
            if num:
                current += 1
                if current >= duration:
                    duration = current
            else:
                current = 0

        return duration

    # 388ms, 13.6MB
    @staticmethod
    def find_max_consecutive_ones_v2(nums: List[int]) -> int:
        current = duration = 0
        for num in nums:
            if num:
                current += 1
            else:
                duration = max(current, duration)
                current = 0

        return max(current, duration)


if __name__ == '__main__':
    test_cases = [
        [0, 0, 0],
        [1, 0, 0],
        [1, 1, 0, 1, 1, 1],
        [1, 1, 0, 1, 1, 0, 1],
        [1, 1, 0, 1, 1, 1, 1, 1, 0],
        [1, 1, 0, 1, 0, 1, 1],
    ]
    for tc in test_cases:
        print(tc, Solution.find_max_consecutive_ones(tc))
        print(tc, Solution.find_max_consecutive_ones_v2(tc))
