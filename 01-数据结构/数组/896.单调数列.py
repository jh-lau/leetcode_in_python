"""
  @Author       : liujianhan
  @Date         : 20/11/7 10:59
  @Project      : leetcode_in_python
  @FileName     : 896.单调数列.py
  @Description  : 如果数组是单调递增或单调递减的，那么它是单调的。
    如果对于所有 i <= j，A[i] <= A[j]，那么数组 A 是单调递增的。 如果对于所有 i <= j，A[i]> = A[j]，那么数组 A 是单调递减的。
    当给定的数组 A 是单调数组时返回 true，否则返回 false。
    示例 1：

    输入：[1,2,2,3]
    输出：true
    示例 2：

    输入：[6,5,4,4]
    输出：true
    示例 3：

    输入：[1,3,2]
    输出：false
    示例 4：

    输入：[1,2,4,5]
    输出：true
    示例 5：

    输入：[1,1,1]
    输出：true
     
    提示：

    1 <= A.length <= 50000
    -100000 <= A[i] <= 100000
"""
from typing import List


class Solution:
    # 544ms, 19.6MB
    @staticmethod
    def is_monotonic(A: List[int]) -> bool:
        descend_flag, ascend_flag = False, False
        for i, num in enumerate(A[:-1]):
            if num == A[i + 1]:
                continue
            elif num > A[i + 1]:
                descend_flag = True
            elif num < A[i + 1]:
                ascend_flag = True

        return not (descend_flag & ascend_flag)


if __name__ == '__main__':
    test_cases = [
        [1, 2, 2, 3],
        [6, 5, 4, 4],
        [1, 3, 2],
        [1, 2, 4, 5],
        [1, 1, 1]
    ]
    for tc in test_cases:
        print(tc, ' --> ', Solution.is_monotonic(tc))
