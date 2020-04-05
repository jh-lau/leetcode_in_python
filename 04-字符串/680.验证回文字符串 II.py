"""
  @Author       : Liujianhan
  @Date         : 20/4/5 19:11
  @FileName     : 680.验证回文字符串 II.py
  @ProjectName  : leetcode_in_python
  @Description  : 给定一个非空字符串 s，最多删除一个字符。判断是否能成为回文字符串。
    示例 1:

    输入: "aba"
    输出: True
    示例 2:

    输入: "abca"
    输出: True
    解释: 你可以删除c字符。
 """


class Solution:
    # 108ms, 14.2MB
    @classmethod
    def valid_palindrome(cls, s: str) -> bool:
        left, right = 0, len(s) - 1
        while left < right:
            if s[left] != s[right]:
                new_left, new_right = s[left:right], s[left + 1: right + 1]
                return new_left == new_left[::-1] or new_right == new_right[::-1]
            left, right = left + 1, right - 1

        return True


if __name__ == '__main__':
    test_cases = ['aba', 'abca']
    for tc in test_cases:
        print(tc, Solution.valid_palindrome(tc))
