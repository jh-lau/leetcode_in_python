"""
  @Author       : liujianhan
  @Date         : 2020/11/27 9:34
  @Project      : leetcode_in_python
  @FileName     : 454.四数相加II(M).py
  @Description  : 给定四个包含整数的数组列表 A , B , C , D ,计算有多少个元组 (i, j, k, l) ，使得 A[i] + B[j] + C[k] + D[l] = 0。
    为了使问题简单化，所有的 A, B, C, D 具有相同的长度 N，且 0 ≤ N ≤ 500 。
    所有整数的范围在 -228 到 228 - 1 之间，最终结果不会超过 231 - 1 。
    例如:
    输入:
    A = [ 1, 2]
    B = [-2,-1]
    C = [-1, 2]
    D = [ 0, 2]
    输出:
    2
    解释:
    两个元组如下:
    1. (0, 0, 0, 1) -> A[0] + B[0] + C[0] + D[1] = 1 + (-2) + (-1) + 2 = 0
    2. (1, 1, 0, 0) -> A[1] + B[1] + C[0] + D[0] = 2 + (-1) + (-1) + 0 = 0
"""
from typing import List
from collections import defaultdict, Counter


class Solution:
    # 324ms, 33.9MB
    @staticmethod
    def four_sum_count(A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        ab_sum_dict = defaultdict(int)
        count = 0
        for a in A:
            for b in B:
                ab_sum_dict[a + b] += 1

        for c in C:
            for d in D:
                if -(c + d) in ab_sum_dict:
                    count += ab_sum_dict[-(c + d)]

        return count

    # 320ms, 33.9MB
    @staticmethod
    def four_sum_count_v2(A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        dic = Counter(a + b for a in A for b in B)
        return sum(dic.get(-c - d, 0) for c in C for d in D)


if __name__ == '__main__':
    test_cases = [
        [[1, 2], [-2, -1], [-1, 2], [0, 2]]
    ]
    for tc in test_cases:
        print(Solution.four_sum_count(*tc))
        print(Solution.four_sum_count_v2(*tc))
