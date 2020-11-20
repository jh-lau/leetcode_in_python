"""
  @Author       : liujianhan
  @Date         : 2020/11/20 17:52
  @Project      : leetcode_in_python
  @FileName     : 905.按奇偶排序数组.py
  @Description  : 给定一个非负整数数组 A，返回一个数组，在该数组中， A 的所有偶数元素之后跟着所有奇数元素。
    你可以返回满足此条件的任何数组作为答案。
    示例：
    输入：[3,1,2,4]
    输出：[2,4,3,1]
    输出 [4,2,3,1]，[2,4,1,3] 和 [4,2,1,3] 也会被接受。
    提示：
    1 <= A.length <= 5000
    0 <= A[i] <= 5000
"""
from typing import List


class Solution:
    # 104ms, 14.2MB
    @staticmethod
    def sort_array_by_parity(A: List[int]) -> List[int]:
        even = [s for s in A if not s % 2]
        odd = [s for s in A if s % 2]
        even.extend(odd)

        return even

    # 100ms, 13.9MB
    @staticmethod
    def sort_array_by_parity_v2(A: List[int]) -> List[int]:
        odd = []
        even = []
        for s in A:
            if s % 2:
                odd.append(s)
            else:
                even.append(s)

        even.extend(odd)

        return even

    # 96ms, 14.2MB
    @staticmethod
    def sort_array_by_parity_v3(A: List[int]) -> List[int]:
        result = [0 for _ in range(len(A))]
        end = len(A) - 1
        start = 0
        for s in A:
            if s % 2:
                result[end] = s
                end -= 1
            else:
                result[start] = s
                start += 1

        return result


if __name__ == '__main__':
    test_cases = [
        [3, 1, 2, 4]
    ]
    for tc in test_cases:
        print(Solution.sort_array_by_parity(tc))
        print(Solution.sort_array_by_parity_v2(tc))
        print(Solution.sort_array_by_parity_v3(tc))
