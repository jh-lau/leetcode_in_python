"""
  @Author       : liujianhan
  @Date         : 2020/9/11 19:40
  @Project      : leetcode_in_python
  @FileName     : 413.等差数列划分(M).py
  @Description  : 如果一个数列至少有三个元素，并且任意两个相邻元素之差相同，则称该数列为等差数列。
    例如，以下数列为等差数列:
    1, 3, 5, 7, 9
    7, 7, 7, 7
    3, -1, -5, -9
    以下数列不是等差数列。

    1, 1, 2, 5, 7
    数组 A 包含 N 个数，且索引从0开始。数组 A 的一个子数组划分为数组 (P, Q)，P 与 Q 是整数且满足 0<=P<Q<N 。

    如果满足以下条件，则称子数组(P, Q)为等差数组：

    元素 A[P], A[p + 1], ..., A[Q - 1], A[Q] 是等差的。并且 P + 1 < Q 。

    函数要返回数组 A 中所有为等差数组的子数组个数。

    示例:

    A = [1, 2, 3, 4]

    返回: 3, A 中有三个子等差数组: [1, 2, 3], [2, 3, 4] 以及自身 [1, 2, 3, 4]。
"""
from typing import List


class Solution:
    # 44ms, 13.8MB
    @staticmethod
    def number_of_arithmetic_slices(A: List[int]) -> int:
        if len(A) < 3:
            return 0
        d = A[1]-A[0]
        index = [0]
        res = 0
        k = 0
        for i in range(1, len(A)-1):
            if A[i+1]-A[i] == d:
                k = i+1
                continue
            else:
                d = A[i+1]-A[i]
                index.append(i)
                if index[-1]-index[-2]+1 >= 3:
                    length = index[-1]-index[-2]+1
                    res += (length-2)*(length-1)//2
        if k == len(A)-1:
            index.append(k)
            if index[-1]-index[-2]+1 >= 3:
                length = index[-1]-index[-2]+1
                res += (length-2)*(length-1)//2
        return res

    # 44ms, 13.8MB
    @staticmethod
    def number_of_arithmetic_slices_v2(A: List[int]) -> int:
        if len(A) <= 2:
            return 0
        a_len = []
        i = 2
        delta = A[1] - A[0]
        tmp = 0
        while i < len(A):
            if A[i] - A[i - 1] != delta:
                a_len.append(i - tmp)
                tmp = i - 1
                delta = A[i] - A[i - 1]
            i += 1
        a_len.append(i - tmp)
        res = 0
        for i in a_len:
            if i > 2:
                res += (i - 2) * (i - 1) // 2
        return res


if __name__ == '__main__':
    test_cases = [
        [1, 2, 3, 4]
    ]
    for tc in test_cases:
        print(Solution.number_of_arithmetic_slices(tc))
        print(Solution.number_of_arithmetic_slices_v2(tc))
