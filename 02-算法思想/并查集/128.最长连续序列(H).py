"""
  @Author       : Liujianhan
  @Date         : 20/4/19 22:06
  @FileName     : 128.最长连续序列(H).py
  @ProjectName  : leetcode_in_python
  @Description  : 给定一个未排序的整数数组，找出最长连续序列的长度。
    要求算法的时间复杂度为 O(n)。
    示例:

    输入: [100, 4, 200, 1, 3, 2]
    输出: 4
    解释: 最长连续序列是 [1, 2, 3, 4]。它的长度为 4。
 """
from typing import List


class Solution:
    # 40ms, 14.7MB
    @classmethod
    def longest_consecutive(cls, nums: List[int]) -> int:
        longest_streak = 0
        num_set =  set(nums)

        for num in num_set:
            if num - 1 not in num_set:
                current_num = num
                current_streak = 1

                while current_num + 1 in num_set:
                    current_num += 1
                    current_streak += 1

                longest_streak = max(longest_streak, current_streak)

        return longest_streak


if __name__ == '__main__':
    test_cases = [
        [100, 4, 200, 1, 3, 2]
    ]
    for tc in test_cases:
        print(Solution.longest_consecutive(tc))
