"""
  @Author       : liujianhan
  @Date         : 2020/4/16 上午10:17
  @Project      : leetcode_in_python
  @FileName     : 056.合并区间(M).py
  @Description  : 给出一个区间的集合，请合并所有重叠的区间。
    示例 1:

    输入: [[1,3],[2,6],[8,10],[15,18]]
    输出: [[1,6],[8,10],[15,18]]
    解释: 区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6].
    示例 2:

    输入: [[1,4],[4,5]]
    输出: [[1,5]]
    解释: 区间 [1,4] 和 [4,5] 可被视为重叠区间。
"""
from typing import List


class Solution:
    # 28ms, 14.5MB
    @classmethod
    def merge(cls, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        merged = []
        for interval in intervals:
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                merged[-1][1] = max(merged[-1][1], interval[1])

        return merged


if __name__ == '__main__':
    test_cases = [
        [[1, 3], [2, 6], [15, 18], [8, 10]],
        [[1, 4], [4, 5]]
    ]
    for tc in test_cases:
        print(Solution.merge(tc))
