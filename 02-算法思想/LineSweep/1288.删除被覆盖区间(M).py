"""
  @Author       : liujianhan
  @Date         : 2020/4/20 下午2:20
  @Project      : leetcode_in_python
  @FileName     : 1288.删除被覆盖区间(M).py
  @Description  : 给你一个区间列表，请你删除列表中被其他区间所覆盖的区间。
    只有当 c <= a 且 b <= d 时，我们才认为区间 [a,b) 被区间 [c,d) 覆盖。
    在完成所有删除操作后，请你返回列表中剩余区间的数目。
    示例：
    输入：intervals = [[1,4],[3,6],[2,8]]
    输出：2
    解释：区间 [3,6] 被区间 [2,8] 覆盖，所以它被删除了。
    提示：​​​​​​
    1 <= intervals.length <= 1000
    0 <= intervals[i][0] < intervals[i][1] <= 10^5
    对于所有的 i != j：intervals[i] != intervals[j]
"""
from typing import List


class Solution:
    @classmethod
    def remove_covered_intervals(cls, intervals: List[List[int]]) -> int:
        n = len(intervals)
        ans = n
        for i in range(n):
            for j in range(n):
                if i != j and intervals[j][0] <= intervals[i][0] and intervals[i][1] <= intervals[j][1]:
                    ans -= 1
                    break
        return ans


if __name__ == '__main__':
    test_cases = [
        [[1, 4], [3, 6], [2, 8]]
    ]
    for tc in test_cases:
        print(Solution.remove_covered_intervals(tc))

