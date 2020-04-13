"""
  @Author       : liujianhan
  @Date         : 2020/4/13 上午11:22
  @Project      : leetcode_in_python
  @FileName     : 198.打家劫舍.py
  @Description  : 你是一个专业的小偷，计划偷窃沿街的房屋。每间房内都藏有一定的现金，影响你偷窃的唯一制约因素就是相邻的房屋装有相互连通的
    防盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警。
    给定一个代表每个房屋存放金额的非负整数数组，计算你在不触动警报装置的情况下，能够偷窃到的最高金额。
    示例 1:

    输入: [1,2,3,1]
    输出: 4
    解释: 偷窃 1 号房屋 (金额 = 1) ，然后偷窃 3 号房屋 (金额 = 3)。
         偷窃到的最高金额 = 1 + 3 = 4 。
    示例 2:

    输入: [2,7,9,3,1]
    输出: 12
    解释: 偷窃 1 号房屋 (金额 = 2), 偷窃 3 号房屋 (金额 = 9)，接着偷窃 5 号房屋 (金额 = 1)。
         偷窃到的最高金额 = 2 + 9 + 1 = 12 。
"""
from typing import List


class Solution:
    # 36ms, 13.6MB
    @classmethod
    def rob(cls, nums: List[int]) -> int:
        last, now = 0, 0
        for i in nums:
            last, now = now, max(last + i, now)

        return now

    # 40ms, 13.6MB
    @classmethod
    def rob_v2(cls, nums: List[int]) -> int:
        n = len(nums)
        if not nums:
            return 0

        dp =[0] * (n + 1)
        dp[0], dp[1] = 0, nums[0]
        for i in range(2, n+1):
            dp[i] = max(dp[i-1], dp[i-2]+nums[i-1])

        return dp[n]


if __name__ == '__main__':
    test_cases = [
        [1, 2, 3, 1],
        [2, 7, 9, 3, 1],
        [2, 1, 1, 2]
    ]
    for tc in test_cases:
        print(Solution.rob(tc))
        print(Solution.rob_v2(tc))
