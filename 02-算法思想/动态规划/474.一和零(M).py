"""
  @Author       : liujianhan
  @Date         : 2020/9/29 10:11
  @Project      : leetcode_in_python
  @FileName     : 474.一和零(M).py
  @Description  : 在计算机界中，我们总是追求用有限的资源获取最大的收益。
    现在，假设你分别支配着 m 个 0 和 n 个 1。另外，还有一个仅包含 0 和 1 字符串的数组。
    你的任务是使用给定的 m 个 0 和 n 个 1 ，找到能拼出存在于数组中的字符串的最大数量。每个 0 和 1 至多被使用一次。

    示例 1:

    输入: strs = ["10", "0001", "111001", "1", "0"], m = 5, n = 3
    输出: 4
    解释: 总共 4 个字符串可以通过 5 个 0 和 3 个 1 拼出，即 "10","0001","1","0" 。
    示例 2:

    输入: strs = ["10", "0", "1"], m = 1, n = 1
    输出: 2
    解释: 你可以拼出 "10"，但之后就没有剩余数字了。更好的选择是拼出 "0" 和 "1" 。
     
    提示：
    1 <= strs.length <= 600
    1 <= strs[i].length <= 100
    strs[i] 仅由 '0' 和 '1' 组成
    1 <= m, n <= 100
"""
from typing import List


class Solution:
    # 3840ms, 13.4MB
    @staticmethod
    def find_max_form(strs: List[str], m: int, n: int) -> int:
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for item in strs:
            count_0 = item.count("0")
            count_1 = item.count("1")
            for i in range(m, count_0 - 1, -1):
                for j in range(n, count_1 - 1, -1):
                    dp[i][j] = max(dp[i][j], 1 + dp[i - count_0][j - count_1])
        return dp[m][n]


if __name__ == '__main__':
    test_cases = [
        (["10", "0001", "111001", "1", "0"], 5, 3),
        (["10", "0", "1"], 1, 1)
    ]
    for tc in test_cases:
        print(Solution.find_max_form(*tc))
