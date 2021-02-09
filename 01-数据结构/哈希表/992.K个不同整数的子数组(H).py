"""
  @Author       : liujianhan
  @Date         : 21/2/9 23:04
  @Project      : leetcode_in_python
  @FileName     : 992.K个不同整数的子数组(H).py
  @Description  : 给定一个正整数数组 A，如果 A 的某个子数组中不同整数的个数恰好为 K，则称 A 的这个连续、不一定不同的子数组为好子数组。
    （例如，[1,2,3,1,2] 中有 3 个不同的整数：1，2，以及 3。）
    返回 A 中好子数组的数目。

    示例 1：
    输入：A = [1,2,1,2,3], K = 2
    输出：7
    解释：恰好由 2 个不同整数组成的子数组：[1,2], [2,1], [1,2], [2,3], [1,2,1], [2,1,2], [1,2,1,2].

    示例 2：
    输入：A = [1,2,1,3,4], K = 3
    输出：3
    解释：恰好由 3 个不同整数组成的子数组：[1,2,1,3], [2,1,3], [1,3,4].

    提示：
    1 <= A.length <= 20000
    1 <= A[i] <= A.length
    1 <= K <= A.length
"""
from typing import List


class Solution:
    # 384ms, 17.3MB
    @staticmethod
    def sub_arrays_with_k_distinct(A: List[int], K: int) -> int:
        counter = {}
        res = i = diff_num = left_forward = 0

        for j in range(len(A)):

            if A[j] not in counter:
                diff_num += 1
                counter[A[j]] = 1
            else:
                counter[A[j]] += 1

            if diff_num == K:
                if A[i - 1] != A[j] and i > 0:
                    left_forward = 0
                while diff_num == K:
                    if counter[A[i]] == 1:
                        diff_num -= 1
                        del counter[A[i]]
                    else:
                        counter[A[i]] -= 1
                    i += 1
                    left_forward += 1
            res += left_forward

        return res


if __name__ == '__main__':
    test_cases = [
        ([1, 2, 1, 2, 3], 2),
        ([1, 2, 1, 3, 4], 3),
    ]
    for tc in test_cases:
        print(Solution.sub_arrays_with_k_distinct(*tc))
