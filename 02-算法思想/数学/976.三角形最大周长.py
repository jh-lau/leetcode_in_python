"""
  @Author       : liujianhan
  @Date         : 20/11/29 15:10
  @Project      : leetcode_in_python
  @FileName     : 976.三角形最大周长.py
  @Description  : 给定由一些正数（代表长度）组成的数组 A，返回由其中三个长度组成的、面积不为零的三角形的最大周长。
    如果不能形成任何面积不为零的三角形，返回 0。
    示例 1：
    输入：[2,1,2]
    输出：5
    示例 2：
    输入：[1,2,1]
    输出：0
    示例 3：
    输入：[3,2,3,4]
    输出：10
    示例 4：
    输入：[3,6,2,3]
    输出：8
    提示：
    3 <= A.length <= 10000
    1 <= A[i] <= 10^6
"""
from typing import List


class Solution:
    # 208ms, 14.8MB
    @staticmethod
    def largest_perimeter(A: List[int]) -> int:
        if len(A) < 3:
            return 0
        A.sort(reverse=True)
        for i in range(len(A)-2):
            if A[i+1] + A[i+2] > A[i]:
                return sum(A[i:i+3])
        return 0


if __name__ == '__main__':
    test_cases = [
        [2, 1, 2],
        [1, 2, 1],
        [3, 2, 3, 4],
        [3, 6, 2, 3]
    ]
    for tc in test_cases:
        print(Solution.largest_perimeter(tc))
