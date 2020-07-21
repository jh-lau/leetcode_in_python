"""
  @Author       : liujianhan
  @Date         : 2020/7/21 上午11:45
  @Project      : leetcode_in_python
  @FileName     : 561.数组拆分I.py
  @Description  : 给定长度为 2n 的数组, 你的任务是将这些数分成 n 对, 例如 (a1, b1), (a2, b2), ..., (an, bn) ，使得从1 到 n 的 min(ai, bi) 总和最大。
    示例 1:
    输入: [1,4,3,2]
    输出: 4
    解释: n 等于 2, 最大总和为 4 = min(1, 2) + min(3, 4).
    提示:
    n 是正整数,范围在 [1, 10000].
    数组中的元素范围在 [-10000, 10000].
"""
from typing import List


class Solution:
    # 336ms, 16MB
    @staticmethod
    def array_pair_sum(nums: List[int]) -> int:
        return sum(sorted(nums)[::2])


if __name__ == '__main__':
    test_cases = [
        [1, 4, 3, 2]
    ]
    for tc in test_cases:
        print(Solution.array_pair_sum(tc))
