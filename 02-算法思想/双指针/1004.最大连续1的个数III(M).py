"""
  @Author       : liujianhan
  @Date         : 21/2/19 10:17
  @Project      : leetcode_in_python
  @FileName     : 1004.最大连续1的个数III(M).py
  @Description  : 给定一个由若干 0 和 1 组成的数组 A，我们最多可以将 K 个值从 0 变成 1 。
    返回仅包含 1 的最长（连续）子数组的长度。
     
    示例 1：
    输入：A = [1,1,1,0,0,0,1,1,1,1,0], K = 2
    输出：6
    解释：
    [1,1,1,0,0,1,1,1,1,1,1]
    粗体数字从 0 翻转到 1，最长的子数组长度为 6。

    示例 2：
    输入：A = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], K = 3
    输出：10
    解释：
    [0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
    粗体数字从 0 翻转到 1，最长的子数组长度为 10。
    提示：
    1 <= A.length <= 20000
    0 <= K <= A.length
    A[i] 为 0 或 1 
"""
from typing import List


class Solution:
    #
    @staticmethod
    def longest_ones(A: List[int], K: int) -> int:
        n = len(A)
        left = lsum = rsum = 0
        ans = 0

        for right in range(n):
            rsum += 1 - A[right]
            while lsum < rsum - K:
                lsum += 1 - A[left]
                left += 1
            ans = max(ans, right - left + 1)

        return ans


if __name__ == '__main__':
    test_cases = [
        ([1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], 2),
        ([0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1], 3),
    ]
    for test_case in test_cases:
        print(Solution.longest_ones(*test_case))
