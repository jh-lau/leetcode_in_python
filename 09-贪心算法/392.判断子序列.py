"""
  @Author       : liujianhan
  @Date         : 2020/7/27 上午11:57
  @Project      : leetcode_in_python
  @FileName     : 392.判断子序列.py
  @Description  : 给定字符串 s 和 t ，判断 s 是否为 t 的子序列。

    你可以认为 s 和 t 中仅包含英文小写字母。字符串 t 可能会很长（长度 ~= 500,000），而 s 是个短字符串（长度 <=100）。

    字符串的一个子序列是原始字符串删除一些（也可以不删除）字符而不改变剩余字符相对位置形成的新字符串。（例如，"ace"是"abcde"的一个子序列，而"aec"不是）。

    示例 1:
    s = "abc", t = "ahbgdc"

    返回 true.

    示例 2:
    s = "axc", t = "ahbgdc"

    返回 false.

    后续挑战 :

    如果有大量输入的 S，称作S1, S2, ... , Sk 其中 k >= 10亿，你需要依次检查它们是否为 T 的子序列。在这种情况下，你会怎样改变代码？
"""


class Solution:
    # 48ms, 13.8MB
    @staticmethod
    def is_subsequence(s: str, t: str) -> bool:
        n, m = len(s), len(t)
        i = j = 0
        while i < n and j < m:
            if s[i] == t[j]:
                i += 1
            j += 1
        return i == n

    # 164ms, 16.5MB
    @staticmethod
    def is_subsequence_v2(s: str, t: str) -> bool:
        n, m = len(s), len(t)
        f = [[0] * 26 for _ in range(m)]
        f.append([m] * 26)

        for i in range(m - 1, -1, -1):
            for j in range(26):
                f[i][j] = i if ord(t[i]) == j + ord('a') else f[i + 1][j]

        add = 0
        for i in range(n):
            if f[add][ord(s[i]) - ord('a')] == m:
                return False
            add = f[add][ord(s[i]) - ord('a')] + 1

        return True


if __name__ == '__main__':
    test_cases = [
        ('abc', 'ahbgdc'),
        ('axc', 'ahbgdc'),
    ]
    for tc in test_cases:
        print(Solution.is_subsequence(*tc))
        print(Solution.is_subsequence_v2(*tc))
