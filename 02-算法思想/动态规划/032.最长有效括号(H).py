"""
  @Author       : Liujianhan
  @Date         : 20/4/19 21:39
  @FileName     : 032.最长有效括号(H).py
  @ProjectName  : leetcode_in_python
  @Description  : 给定一个只包含 '(' 和 ')' 的字符串，找出最长的包含有效括号的子串的长度。
    示例 1:

    输入: "(()"
    输出: 2
    解释: 最长有效括号子串为 "()"
    示例 2:

    输入: ")()())"
    输出: 4
    解释: 最长有效括号子串为 "()()"
 """


class Solution:
    # 76ms, 13.8MB
    @classmethod
    def longest_valid_parentheses(cls, s: str) -> int:
        max_ans = 0
        dp = [0] * len(s)
        for i in range(len(s)):
            if s[i] == ')':
                if i - 1 < 0:
                    continue
                if s[i - 1] == '(':
                    dp[i] = (dp[i - 2] if i >= 2 else 0) + 2
                elif i - dp[i - 1] > 0 and s[i - dp[i - 1] - 1] == "(":
                    dp[i] = dp[i - 1] + (dp[i - dp[i - 1] - 2] if i - dp[i - 1] >= 2 else 0) + 2
                max_ans = max(max_ans, dp[i])

        return max_ans

    # 52ms, 13.9MB
    @classmethod
    def longest_valid_parentheses_v2(cls, s: str) -> int:
        stack = [0]
        longest = 0

        for c in s:
            if c == "(":
                stack.append(0)
            else:
                if len(stack) > 1:
                    val = stack.pop()
                    stack[-1] += val + 2
                    longest = max(longest, stack[-1])
                else:
                    stack = [0]

        return longest


if __name__ == '__main__':
    test_cases = ['(()', ')()())']
    for tc in test_cases:
        print(Solution.longest_valid_parentheses(tc))
        print(Solution.longest_valid_parentheses_v2(tc))
