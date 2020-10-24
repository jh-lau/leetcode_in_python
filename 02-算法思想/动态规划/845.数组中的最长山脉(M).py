"""
  @Author       : liujianhan
  @Date         : 20/10/25 0:21
  @Project      : leetcode_in_python
  @FileName     : 845.数组中的最长山脉(M).py
  @Description  : 我们把数组 A 中符合下列属性的任意连续子数组 B 称为 “山脉”：
    B.length >= 3
    存在 0 < i < B.length - 1 使得 B[0] < B[1] < ... B[i-1] < B[i] > B[i+1] > ... > B[B.length - 1]
    （注意：B 可以是 A 的任意子数组，包括整个数组 A。）
    给出一个整数数组 A，返回最长 “山脉” 的长度。
    如果不含有 “山脉” 则返回 0。

    示例 1：
    输入：[2,1,4,7,3,2,5]
    输出：5
    解释：最长的 “山脉” 是 [1,4,7,3,2]，长度为 5。

    示例 2：
    输入：[2,2,2]
    输出：0
    解释：不含 “山脉”。

    提示：
    0 <= A.length <= 10000
    0 <= A[i] <= 10000
    SOLUTION:
    https://leetcode-cn.com/problems/longest-mountain-in-array/solution/shu-zu-zhong-de-zui-chang-shan-mai-by-leetcode-sol/
"""
from typing import List


class Solution:
    # 44ms, 14.3MB
    @staticmethod
    def longest_mountain(A: List[int]) -> int:
        """双指针"""
        n = len(A)
        ans = left = 0
        while left + 2 < n:
            right = left + 1
            if A[left] < A[left + 1]:
                while right + 1 < n and A[right] < A[right + 1]:
                    right += 1
                if right < n - 1 and A[right] > A[right + 1]:
                    while right + 1 < n and A[right] > A[right + 1]:
                        right += 1
                    ans = max(ans, right - left + 1)
                else:
                    right += 1
            left = right
        return ans

    # 84ms, 14.2MB
    @staticmethod
    def longest_mountain_v2(A: List[int]) -> int:
        """dp"""
        if not A:
            return 0

        n = len(A)
        left = [0] * n
        for i in range(1, n):
            left[i] = (left[i - 1] + 1 if A[i - 1] < A[i] else 0)

        right = [0] * n
        for i in range(n - 2, -1, -1):
            right[i] = (right[i + 1] + 1 if A[i + 1] < A[i] else 0)

        ans = 0
        for i in range(n):
            if left[i] > 0 and right[i] > 0:
                ans = max(ans, left[i] + right[i] + 1)

        return ans


if __name__ == '__main__':
    test_cases = [
        [2, 1, 4, 7, 3, 2, 5],
        [2, 2, 2]
    ]
    for tc in test_cases:
        print(Solution.longest_mountain(tc))
        print(Solution.longest_mountain_v2(tc))
