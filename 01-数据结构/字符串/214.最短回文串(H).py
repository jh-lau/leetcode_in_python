"""
  @Author       : liujianhan
  @Date         : 2020/6/10 下午7:41
  @Project      : leetcode_in_python
  @FileName     : 214.最短回文串(H).py
  @Description  : 给定一个字符串 s，你可以通过在字符串前面添加字符将其转换为回文串。找到并返回可以用这种方式转换的最短回文串。
    示例 1:
    输入: "aacecaaa"
    输出: "aaacecaaa"
    示例 2:
    输入: "abcd"
    输出: "dcbabcd"
"""


class Solution:
    # 72ms, 13.9MB
    @classmethod
    def shortest_palindrome(cls, s: str) -> str:
        r = s[::-1]
        for i in range(len(s) + 1):
            if s.startswith(r[i:]):
                return r[:i] + s

    # 44ms, 13.7MB
    def shortest_palindrome_v2(self, s: str) -> str:
        j = 0
        for i in range(len(s) - 1, -1, -1):
            if s[i] == s[j]:
                j += 1
        if j == len(s):
            return s
        suffix = s[j:]

        return suffix[::-1] + self.shortest_palindrome_v2(s[0:j]) + suffix


if __name__ == '__main__':
    test_cases = [
        "aacecaaa",
        "abcd"
    ]
    for tc in test_cases:
        print(Solution.shortest_palindrome(tc))
        print(Solution().shortest_palindrome_v2(tc))
