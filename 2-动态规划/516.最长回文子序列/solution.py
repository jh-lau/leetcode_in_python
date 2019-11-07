"""
  User: Liujianhan
 """
__author__ = 'liujianhan'


class Solution:
    @staticmethod
    def longest_sub_palindrome_sub_sequence(s):
        length = len(s)
        dp = [[0] * length for _ in range(length)]
        for i in range(length):
            dp[i][i] = 1
        for i in range(length - 1, -1, -1):
            for j in range(i + 1, length):
                if s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1] + 2
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
        return dp[0][-1]
    
    @staticmethod
    def method_2(s):
        from functools import lru_cache
        
        @lru_cache(None)
        def helper(s):
            if len(s) <= 1:
                return len(s)
            if s[0] == s[-1]:
                return helper(s[1:-1]) + 2
            else:
                return max(helper(s[1:]), helper(s[:-1]))
        return helper(s)


if __name__ == '__main__':
    print(Solution().longest_sub_palindrome_sub_sequence('bbbab'))
    print(Solution().method_2('bbbab'))
    print(Solution().longest_sub_palindrome_sub_sequence('cbbd'))
    print(Solution().method_2('cbbd'))