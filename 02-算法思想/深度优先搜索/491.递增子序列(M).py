"""
  @Author       : liujianhan
  @Date         : 2020/8/25 19:48
  @Project      : leetcode_in_python
  @FileName     : 491.递增子序列(M).py
  @Description  : 给定一个整型数组, 你的任务是找到所有该数组的递增子序列，递增子序列的长度至少是2。
    示例:
    输入: [4, 6, 7, 7]
    输出: [[4, 6], [4, 7], [4, 6, 7], [4, 6, 7, 7], [6, 7], [6, 7, 7], [7,7], [4,7,7]]
    说明:
    给定数组的长度不会超过15。
    给定数组中可能包含重复数字，相等的数字应该被视为递增的一种情况。
"""
from collections import deque
from typing import List


class Solution:
    # 80ms, 20MB
    @staticmethod
    def find_ubsequences(nums: List[int]) -> List[List[int]]:
        res = []

        def dfs(nums: List[int], tmp: List[int]) -> None:
            if len(tmp) > 1:
                res.append(tmp)
            curPres = set()
            for inx, i in enumerate(nums):
                if i in curPres:
                    continue
                if not tmp or i >= tmp[-1]:
                    curPres.add(i)
                    dfs(nums[inx + 1:], tmp + [i])

        dfs(nums, [])
        return res

    # 112ms, 20.1MB
    @staticmethod
    def find_ubsequences_v2(nums: List[int]) -> List[List[int]]:
        res = []
        d = deque([(nums, [])])
        while d:
            cur, new = d.popleft()
            if len(new) > 1:
                res.append(new)
            curPres = set()
            for inx, i in enumerate(cur):
                if i in curPres:
                    continue
                if not new or i >= new[-1]:
                    curPres.add(i)
                    d.append((cur[inx + 1:], new + [i]))
        return res


if __name__ == '__main__':
    test_cases = [
        [4, 6, 7, 7]
    ]
    for tc in test_cases:
        print(Solution.find_ubsequences(tc))
        print(Solution.find_ubsequences_v2(tc))
