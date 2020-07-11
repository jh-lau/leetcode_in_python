"""
  @Author       : Liujianhan
  @Date         : 20/7/10 22:16
  @FileName     : 312.戳气球(H).py
  @ProjectName  : leetcode_in_python
  @Description  : 有 n 个气球，编号为0 到 n-1，每个气球上都标有一个数字，这些数字存在数组 nums 中。
    现在要求你戳破所有的气球。如果你戳破气球 i ，就可以获得 nums[left] * nums[i] * nums[right] 个硬币。 这里的 left 和 right 代表和 i 相邻的两个气球的序号。注意当你戳破了气球 i 后，气球 left 和气球 right 就变成了相邻的气球。
    求所能获得硬币的最大数量。
    说明:
    你可以假设 nums[-1] = nums[n] = 1，但注意它们不是真实存在的所以并不能被戳破。
    0 ≤ n ≤ 500, 0 ≤ nums[i] ≤ 100
    示例:
    输入: [3,1,5,8]
    输出: 167
    解释: nums = [3,1,5,8] --> [3,5,8] -->   [3,8]   -->  [8]  --> []
         coins =  3*1*5      +  3*5*8    +  1*3*8      + 1*8*1   = 167
     """
from typing import List


class Solution:
    # 860ms, 14.2MB
    @staticmethod
    def max_coins(nums: List[int]) -> int:
        if not nums:
            return 0

        def getMaxCoins(nums, i, j, memo):
            if i == j - 1:
                return 0
            if memo[i][j] > 0:
                return memo[i][j]

            temp = 0

            for k in range(i + 1, j):
                left = getMaxCoins(nums, i, k, memo)
                right = getMaxCoins(nums, k, j, memo)

                temp = max(temp, left + right + nums[i] * nums[k] * nums[j])

            memo[i][j] = temp

            return temp

        nums = [1, *nums, 1]
        memo = [[0 for i in nums] for n in nums]

        return getMaxCoins(nums, 0, len(nums) - 1, memo)


if __name__ == '__main__':
    print(Solution.max_coins([3, 1, 5, 8]))
