"""
  User: Liujianhan
 """
__author__ = 'liujianhan'


class Solution:
    @staticmethod
    def longest_common_sub_sequence(text1, text2):
        m, n = len(text1), len(text2)
        l = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if text1[i - 1] == text2[j - 1]:
                    l[i][j] = l[i - 1][j - 1] + 1
                else:
                    l[i][j] = max(l[i - 1][j], l[i][j - 1])
        return l[-1][-1]
