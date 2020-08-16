"""
  @Author       : liujianhan
  @Date         : 2020/4/16 上午10:32
  @Project      : leetcode_in_python
  @FileName     : 057.插入区间(H).py
  @Description  : 给出一个无重叠的 ，按照区间起始端点排序的区间列表。
    在列表中插入一个新的区间，你需要确保列表中的区间仍然有序且不重叠（如果有必要的话，可以合并区间）。
    示例 1:

    输入: intervals = [[1,3],[6,9]], newInterval = [2,5]
    输出: [[1,5],[6,9]]
    示例 2:

    输入: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
    输出: [[1,2],[3,10],[12,16]]
    解释: 这是因为新的区间 [4,8] 与 [3,5],[6,7],[8,10] 重叠。
"""
from typing import List


class Solution:
    # 72ms, 15.2MB
    @classmethod
    def insert(cls, intervals: List[List[int]], new_interval: List[int]) -> List[List[int]]:
        new_start, new_end = new_interval
        idx, n = 0, len(intervals)
        output = []

        while idx < n and new_start > intervals[idx][0]:
            output.append(intervals[idx])
            idx += 1

        if not output or output[-1][1] < new_start:
            output.append(new_interval)
        else:
            output[-1][1] = max(output[-1][1], new_end)

        while idx < n:
            interval = intervals[idx]
            start, end = interval
            idx += 1
            if output[-1][1] < start:
                output.append(interval)
            else:
                output[-1][1] = max(output[-1][1], end)

        return output

    # 48ms, 15.3MB
    @classmethod
    def insert_v2(cls, intervals: List[List[int]], new_interval: List[int]) -> List[List[int]]:
        """复用56题代码"""
        intervals.append(new_interval)
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
        ([[1, 3], [6, 9]], [2, 5]),
        ([[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 8])
    ]
    for tc in test_cases:
        print(Solution.insert_v2(*tc))
