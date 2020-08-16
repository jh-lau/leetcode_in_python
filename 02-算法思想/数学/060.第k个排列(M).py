"""
  @Author       : liujianhan
  @Date         : 2020/4/16 上午10:44
  @Project      : leetcode_in_python
  @FileName     : 060.第k个排列(M).py
  @Description  : 给出集合 [1,2,3,…,n]，其所有元素共有 n! 种排列。
    按大小顺序列出所有排列情况，并一一标记，当 n = 3 时, 所有排列如下：

    "123"
    "132"
    "213"
    "231"
    "312"
    "321"
    给定 n 和 k，返回第 k 个排列。
    说明：

    给定 n 的范围是 [1, 9]。
    给定 k 的范围是[1,  n!]。
    示例 1:

    输入: n = 3, k = 3
    输出: "213"
    示例 2:

    输入: n = 4, k = 9
    输出: "2314"
"""
from itertools import permutations
from math import factorial


class Solution:
    # 2332ms, 57.1MB
    @classmethod
    def get_permutation(cls, n: int, k: int) -> str:
        return ''.join(list(map(str, list(permutations(range(1, n+1)))[k-1])))

    # 56ms, 13.8MB
    @classmethod
    def get_permutation_v2(cls, n: int, k: int) -> str:
        tokens = [str(i) for i in range(1, n+1)]
        res = ''
        k -= 1
        while n:
            n -= 1
            a, k = divmod(k, factorial(n))
            res += tokens.pop(a)

        return res


if __name__ == '__main__':
    test_cases = [(3, 3), (4, 9)]
    for tc in test_cases:
        print(Solution.get_permutation(*tc))
        print(Solution.get_permutation_v2(*tc))
