"""
  @Author       : liujianhan
  @Date         : 2020/11/3 11:29
  @Project      : leetcode_in_python
  @FileName     : 941.有效的山脉数组.py
  @Description  : 给定一个整数数组 A，如果它是有效的山脉数组就返回 true，否则返回 false。
    让我们回顾一下，如果 A 满足下述条件，那么它是一个山脉数组：
    A.length >= 3
    在 0 < i < A.length - 1 条件下，存在 i 使得：
    A[0] < A[1] < ... A[i-1] < A[i]
    A[i] > A[i+1] > ... > A[A.length - 1]
    示例 1：

    输入：[2,1]
    输出：false
    示例 2：

    输入：[3,5,5]
    输出：false
    示例 3：

    输入：[0,3,2,1]
    输出：true
    提示：

    0 <= A.length <= 10000
    0 <= A[i] <= 10000 
"""
from typing import List


class Solution:
    # 280ms, 14.9MB
    @staticmethod
    def valid_mountain_array(A: List[int]) -> bool:
        size = len(A)
        if size < 3:
            return False
        index = 0
        ascend_flag, descend_flag = False, False
        while index < size - 1:
            if A[index + 1] == A[index]:
                return False
            if descend_flag:
                if A[index + 1] < A[index]:
                    index += 1
                else:
                    return False
            else:
                if A[index + 1] > A[index]:
                    ascend_flag = True
                    index += 1
                else:
                    descend_flag = True
                    index += 1
        return ascend_flag & descend_flag

    # 224ms, 14.8MB
    @staticmethod
    def valid_mountain_array_v2(A: List[int]) -> bool:
        if not A:
            return False
        top = max(A)
        top_index = A.index(top)
        size = len(A)
        if top_index == 0 or top_index == size - 1:
            return False
        for i, num in enumerate(A[:-1]):
            if i < top_index:
                if num >= A[i+1]:
                    return False
            else:
                if num <= A[i+1]:
                    return False

        return True


if __name__ == '__main__':
    test_cases = [
        [2, 1],
        [3, 5, 5],
        [0, 3, 2, 1],
        [1, 2, 3],
        [1, 2, 1],
        [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
    ]
    for tc in test_cases:
        print(tc, Solution.valid_mountain_array(tc))
        print(tc, Solution.valid_mountain_array_v2(tc))
