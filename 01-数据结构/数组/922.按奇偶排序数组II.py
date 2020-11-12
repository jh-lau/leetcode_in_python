"""
  @Author       : liujianhan
  @Date         : 2020/11/12 11:37
  @Project      : leetcode_in_python
  @FileName     : 922.按奇偶排序数组II.py
  @Description  : 给定一个非负整数数组 A， A 中一半整数是奇数，一半整数是偶数。
    对数组进行排序，以便当 A[i] 为奇数时，i 也是奇数；当 A[i] 为偶数时， i 也是偶数。
    你可以返回任何满足上述条件的数组作为答案。
    示例：

    输入：[4,2,5,7]
    输出：[4,5,2,7]
    解释：[4,7,2,5]，[2,5,4,7]，[2,7,4,5] 也会被接受。
     
    提示：

    2 <= A.length <= 20000
    A.length % 2 == 0
    0 <= A[i] <= 1000
"""
from typing import List


class Solution:
    # 224ms, 15.6MB
    @staticmethod
    def sort_array_by_parity_II(A: List[int]) -> List[int]:
        odd_i = []
        even_i = []
        for i, num in enumerate(A):
            if i % 2 and not num % 2:
                odd_i.append(i)
            elif not i % 2 and num % 2:
                even_i.append(i)

        for a, b in zip(odd_i, even_i):
            A[a], A[b] = A[b], A[a]

        return A


if __name__ == '__main__':
    test_cases = [
        [4, 2, 5, 7],
        [648, 831, 560, 986, 192, 424, 997, 829, 897, 843]
    ]
    for tc in test_cases:
        print(Solution.sort_array_by_parity_II(tc))
