"""
  @Author       : liujianhan
  @Date         : 2020/7/1 下午7:16
  @Project      : leetcode_in_python
  @FileName     : 718.最长重复子数组(M).py
  @Description  : 给两个整数数组 A 和 B ，返回两个数组中公共的、长度最长的子数组的长度。
    示例：
    输入：
    A: [1,2,3,2,1]
    B: [3,2,1,4,7]
    输出：3
    解释：
    长度最长的公共子数组是 [3, 2, 1] 。
"""
from typing import List


class Solution:
    # 6112ms, 39.1MB
    @staticmethod
    def find_length(A: List[int], B: List[int]) -> int:
        n, m = len(A), len(B)
        dp = [[0] * (m + 1) for _ in range(n + 1)]
        ans = 0
        for i in range(n - 1, -1, -1):
            for j in range(m - 1, -1, -1):
                dp[i][j] = dp[i + 1][j + 1] + 1 if A[i] == B[j] else 0
                ans = max(ans, dp[i][j])
        return ans

    # 364ms, 13.7MB
    @staticmethod
    def find_length_v2(A: List[int], B: List[int]) -> int:
        m, n = len(A), len(B)
        if m > n:
            m, n, A, B = n, m, B, A
        tmp_list = []
        result = 0
        str_B = ',' + ','.join([str(i) for i in B]) + ','

        for r in A:
            tmp_list.append(str(r))

            if ',' + ','.join(tmp_list) + ',' in str_B:
                result = max(result, len(tmp_list))

            else:
                tmp_list = tmp_list[1:]

        return result


if __name__ == '__main__':
    print(Solution.find_length([1, 2, 3, 2, 1], [3, 2, 1, 4, 7]))
    print(Solution.find_length_v2([1, 2, 3, 2, 1], [3, 2, 1, 4, 7]))
