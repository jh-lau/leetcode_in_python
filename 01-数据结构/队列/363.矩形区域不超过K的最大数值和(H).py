"""
  @Author       : liujianhan
  @Date         : 20/8/23 16:10
  @Project      : leetcode_in_python
  @FileName     : 363.矩形区域不超过K的最大数值和(H).py
  @Description  : 给定一个非空二维矩阵 matrix 和一个整数 k，找到这个矩阵内部不大于 k 的最大矩形和。
    示例:
    输入: matrix = [[1,0,1],[0,-2,3]], k = 2
    输出: 2
    解释: 矩形区域 [[0, 1], [-2, 3]] 的数值和是 2，且 2 是不超过 k 的最大数字（k = 2）。
    说明：

    矩阵内的矩形区域面积必须大于 0。
    如果行数远大于列数，你将如何解答呢？
"""
from typing import List
import bisect


class Solution:
    # 1060ms, 14.6MB
    @staticmethod
    def max_sum_submatrix(matrix: List[List[int]], k: int) -> int:
        m, n = len(matrix), len(matrix[0])
        preSum = [[0 for _ in range(n + 1)] for _ in range(m)]

        for i in range(m):
            for j in range(1, n + 1):
                preSum[i][j] = preSum[i][j - 1] + matrix[i][j - 1]

        res = float('-inf')
        for colA in range(1, n + 1):
            for colB in range(colA, n + 1):
                slist, cur = [0], 0
                for row in range(m):
                    cur += preSum[row][colB] - preSum[row][colA - 1]
                    idx = bisect.bisect_left(slist, cur - k)
                    if idx < len(slist):
                        res = max(res, cur - slist[idx])
                    bisect.insort(slist, cur)
        return res

    def bsearch(self, nums, target):
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) >> 1
            if nums[mid] >= target:
                r = mid - 1
            else:
                l = mid + 1
        return l


if __name__ == '__main__':
    test_cases = [
        ([[1, 0, 1], [0, -2, 3]], 2)
    ]
    for tc in test_cases:
        print(Solution.max_sum_submatrix(*tc))
