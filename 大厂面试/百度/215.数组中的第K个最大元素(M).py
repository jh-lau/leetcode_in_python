"""
  @Author       : Liujianhan
  @Date         : 20/6/19 21:33
  @FileName     : 215.数组中的第K个最大元素(M).py
  @ProjectName  : leetcode_in_python
  @Description  : 在未排序的数组中找到第 k 个最大的元素。请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。
    示例 1:
    输入: [3,2,1,5,6,4] 和 k = 2
    输出: 5
    示例 2:
    输入: [3,2,3,1,2,4,5,5,6] 和 k = 4
    输出: 4
    说明:
    你可以假设 k 总是有效的，且 1 ≤ k ≤ 数组的长度。
 """
import heapq
from typing import List


class Solution:
    # 56ms, 14.1MB
    @classmethod
    def find_kth_largest(cls, nums: List[int], k: int) -> int:
        return heapq.nlargest(k, nums)[-1]


if __name__ == '__main__':
    test_cases = [
        ([3, 2, 1, 5, 6, 4], 2),
        ([3, 2, 3, 1, 2, 4, 5, 5, 6], 4),
    ]
    for tc in test_cases:
        print(Solution.find_kth_largest(*tc))
