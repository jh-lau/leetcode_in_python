"""
  @Author       : liujianhan
  @Date         : 2020/8/19 11:09
  @Project      : leetcode_in_python
  @FileName     : 647.回文子串(M).py
  @Description  : 给定一个字符串，你的任务是计算这个字符串中有多少个回文子串。
    具有不同开始位置或结束位置的子串，即使是由相同的字符组成，也会被视作不同的子串。
    示例 1：

    输入："abc"
    输出：3
    解释：三个回文子串: "a", "b", "c"
    示例 2：

    输入："aaa"
    输出：6
    解释：6个回文子串: "a", "a", "a", "aa", "aa", "aaa"
     
    提示：

    输入的字符串长度不会超过 1000 。
"""


class Solution:
    # 124ms, 13.7MB
    @staticmethod
    def count_substrings(s: str) -> int:
        length = len(s)
        cnt = 0
        # 以某一个元素为中心的奇数长度的回文串的情况
        for center in range(length):
            left = right = center
            while left >= 0 and right < length and s[left] == s[right]:
                cnt += 1
                left -= 1
                right += 1
        # 以某对元素为中心的偶数长度的回文串的情况
        for left in range(length - 1):
            right = left + 1
            while left >= 0 and right < length and s[left] == s[right]:
                cnt += 1
                left -= 1
                right += 1

        return cnt

    # 192ms, 13.7MB
    @staticmethod
    def count_substrings_v2(s: str) -> int:
        n = len(s)
        result = 0

        def helper(i, j):
            while i >= 0 and j < n and s[i] == s[j]:
                i -= 1
                j += 1
                nonlocal result
                result += 1

        for i in range(n):
            helper(i, i)
            helper(i, i + 1)

        return result


if __name__ == '__main__':
    test_cases = [
        'abc', 'aaa'
    ]
    for tc in test_cases:
        print(Solution.count_substrings(tc))
        print(Solution.count_substrings_v2(tc))
