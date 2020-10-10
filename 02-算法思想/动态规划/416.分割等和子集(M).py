"""
  @Author       : liujianhan
  @Date         : 20/10/11 0:52
  @Project      : leetcode_in_python
  @FileName     : 416.分割等和子集(M).py
  @Description  : 给定一个只包含正整数的非空数组。是否可以将这个数组分割成两个子集，使得两个子集的元素和相等。
    注意:
    每个数组中的元素不会超过 100
    数组的大小不会超过 200
    示例 1:
    输入: [1, 5, 11, 5]
    输出: true
    解释: 数组可以分割成 [1, 5, 5] 和 [11].
    示例 2:
    输入: [1, 2, 3, 5]
    输出: false
    解释: 数组不能分割成两个元素和相等的子集.
"""
from typing import List


class Solution:
    # 2512ms, 28.4MB
    @staticmethod
    def can_partition(nums: List[int]) -> bool:
        n = len(nums)
        if n < 2:
            return False

        total = sum(nums)
        max_num = max(nums)
        if total & 1:
            return False

        target = total // 2
        if max_num > target:
            return False

        dp = [[0] * (target + 1) for _ in range(n)]
        for i in range(n):
            dp[i][0] = True

        dp[0][nums[0]] = True
        for i in range(1, n):
            num = nums[i]
            for j in range(1, target + 1):
                if j >= num:
                    dp[i][j] = dp[i - 1][j] | dp[i - 1][j - num]
                else:
                    dp[i][j] = dp[i - 1][j]

        return bool(dp[n - 1][target])


if __name__ == '__main__':
    test_cases = [
        [1, 5, 11, 5],
        [1, 2, 3, 5]
    ]
    for tc in test_cases:
        print(Solution.can_partition(tc))