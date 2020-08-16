"""
  @Author       : Liujianhan
  @Date         : 20/4/25 16:12
  @FileName     : 047.全排列II(M).py
  @ProjectName  : leetcode_in_python
  @Description  : 给定一个可包含重复数字的序列，返回所有不重复的全排列。
    示例:
    输入: [1,1,2]
    输出:
    [
      [1,1,2],
      [1,2,1],
      [2,1,1]
    ]
 """
from itertools import permutations
from typing import List


class Solution:
    # 52ms, 13.8MB
    @classmethod
    def permute_unique(cls, nums: List[int]) -> List[List[int]]:
        return list(set(permutations(nums)))

    # 44ms, 14MB
    @classmethod
    def permute_unique_v2(cls, nums: List[int]) -> List[List[int]]:
        if not nums: return []
        nums.sort()
        res = []

        def backtrack(track, choices):
            if not choices:
                res.append(list(track))  # 直接track不行,因为[]可变
                return
            for i, c in enumerate(choices):
                if i > 0 and c == choices[i - 1]:
                    continue
                track.append(c)
                backtrack(track, choices[:i] + choices[i + 1:])
                track.pop()

        backtrack([], nums)

        return res


if __name__ == '__main__':
    test_cases = [
        [1, 1, 2]
    ]
    for tc in test_cases:
        print(Solution.permute_unique(tc))
        print(Solution.permute_unique_v2(tc))
