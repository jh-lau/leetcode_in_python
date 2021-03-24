"""
  @Author       : liujianhan
  @Date         : 21/3/24 9:16
  @Project      : leetcode_in_python
  @FileName     : 456.132模式(M).py
  @Description  : 给定一个整数序列：a1, a2, ..., an，一个132模式的子序列 ai, aj, ak 被定义为：当 i < j < k 时，ai < ak < aj。
  设计一个算法，当给定有 n 个数字的序列时，验证这个序列中是否含有132模式的子序列。
    注意：n 的值小于15000。

    示例1:
    输入: [1, 2, 3, 4]
    输出: False
    解释: 序列中不存在132模式的子序列。

    示例 2:
    输入: [3, 1, 4, 2]
    输出: True
    解释: 序列中有 1 个132模式的子序列： [1, 4, 2].

    示例 3:
    输入: [-1, 3, 2, 0]
    输出: True
    解释: 序列中有 3 个132模式的的子序列: [-1, 3, 2], [-1, 3, 0] 和 [-1, 2, 0].
"""
from typing import List


class Solution:
    # 60ms, 15.6MB
    @staticmethod
    def find_132_pattern(nums: List[int]) -> bool:
        n = len(nums)
        candidate_k = [nums[n - 1]]
        max_k = float("-inf")

        for i in range(n - 2, -1, -1):
            if nums[i] < max_k:
                return True
            while candidate_k and nums[i] > candidate_k[-1]:
                max_k = candidate_k[-1]
                candidate_k.pop()
            if nums[i] > max_k:
                candidate_k.append(nums[i])

        return False


if __name__ == '__main__':
    test_cases =[
        [1, 2, 3, 4],
        [3, 1, 4, 2],
        [-1, 3, 2, 0]
    ]
    for test_case in test_cases:
        print(Solution.find_132_pattern(test_case))
