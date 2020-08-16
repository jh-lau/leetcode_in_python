"""
  @Author       : liujianhan
  @Date         : 2020/6/17 上午9:44
  @Project      : leetcode_in_python
  @FileName     : 1014.最佳观光组合(M).py
  @Description  : 给定正整数数组 A，A[i] 表示第 i 个观光景点的评分，并且两个景点 i 和 j 之间的距离为 j - i。
    一对景点（i < j）组成的观光组合的得分为（A[i] + A[j] + i - j）：景点的评分之和减去它们两者之间的距离。
    返回一对观光景点能取得的最高分。
    示例：
    输入：[8,1,5,2,6]
    输出：11
    解释：i = 0, j = 2, A[i] + A[j] + i - j = 8 + 5 + 0 - 2 = 11
    提示：
    2 <= A.length <= 50000
    1 <= A[i] <= 1000
"""
from typing import List


class Solution:
    # 624ms, 18.9MB
    @classmethod
    def max_score_sightseeing_pair(cls, A: List[int]) -> int:
        res = 0
        pre_max = A[0] + 0
        for j in range(1, len(A)):
            res = max(res, pre_max + A[j] - j)
            pre_max = max(pre_max, A[j] + j)

        return res


if __name__ == '__main__':
    test_cases = [
        [8, 1, 5, 2, 6]
    ]
    for tc in test_cases:
        print(Solution.max_score_sightseeing_pair(tc))
