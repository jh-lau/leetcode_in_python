"""
  @Author       : liujianhan
  @Date         : 2020/3/23 上午10:21
  @Project      : leetcode_in_python
  @FileName     : 125.验证回文串.py
  @Description  : 给定一个字符串，验证它是否是回文串，只考虑字母和数字字符，可以忽略字母的大小写。（我们将空字符串定义为有效的回文串。）
"""


class Solution:
    # 40ms, 14.4MB
    @classmethod
    def is_palindrome(cls, s: str) -> bool:
        if s == '':
            return True
        new_s = ''.join([char for char in s if char.isalnum()]).lower()
        return new_s == new_s[::-1]

    # 40ms, 13.8MB
    @classmethod
    def is_palindrome_v2(cls, s: str) -> bool:
        s = s.lower()
        left, right = 0, len(s) - 1
        while left < right:
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1

        return True


if __name__ == '__main__':
    test_case = ["A man, a plan, a canal: Panama", "race a car"]
    for tc in test_case:
        print(tc, Solution.is_palindrome(tc))
        print(tc, Solution.is_palindrome_v2(tc))
