"""
  User: Liujianhan
 """
__author__ = 'liujianhan'


class Solution:
    @staticmethod
    def longest_palindrome(string):
        size = len(string)
        if size <= 1:
            return string
        dp = [[False for _ in range(size)] for _ in range(size)]

        longest = 1
        res = string[0]

        for r in range(1, size):
            for l in range(r):
                if string[l] == string[r] and (r - l <= 2 or dp[l + 1][r - 1]):
                    dp[l][r] = True
                    cur_len = r - l + 1
                    if cur_len > longest:
                        longest = cur_len
                        res = string[l:r + 1]
        return res


if __name__ == '__main__':
    test_cases = [
        'babad', 'cbbd', 'c', 'cdabababad'
    ]
    for tc in test_cases:
        print(Solution.longest_palindrome(tc))
