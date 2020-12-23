"""
  @Author       : liujianhan
  @Date         : 2020/12/23 10:02
  @Project      : leetcode_in_python
  @FileName     : 961.重复N次的元素.py
  @Description  : 在大小为 2N 的数组 A 中有 N+1 个不同的元素，其中有一个元素重复了 N 次。
    返回重复了 N 次的那个元素。

    示例 1：
    输入：[1,2,3,3]
    输出：3

    示例 2：
    输入：[2,1,2,5,3,2]
    输出：2

    示例 3：
    输入：[5,1,5,2,5,3,5,4]
    输出：5
"""
from typing import List
from collections import Counter


class Solution:
    # 3816ms, 16.1MB
    @staticmethod
    def repeated_N_times(A: List[int]) -> int:
        N = len(A) // 2
        for num in set(A):
            if A.count(num) == N:
                return num

    # 52ms, 15.7MB
    @staticmethod
    def repeated_N_times_v2(A: List[int]) -> int:
        count = Counter(A)
        for k, v in count.items():
            if v == len(A) // 2:
                return k

    # 64ms, 15.6MB
    @staticmethod
    def repeated_N_times_v3(A: List[int]) -> int:
        dic = {}
        for item in A:
            if item in dic:
                return item
            else:
                dic[item] = 1


if __name__ == '__main__':
    test_cases = [
        [1, 2, 3, 3],
        [2, 1, 2, 5, 3, 2],
        [5, 1, 5, 2, 5, 3, 5, 4]
    ]
    for tc in test_cases:
        print(Solution.repeated_N_times(tc))
        print(Solution.repeated_N_times_v2(tc))