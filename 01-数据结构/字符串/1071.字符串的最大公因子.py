"""
  @Author       : liujianhan
  @Date         : 2020/4/17 上午11:03
  @Project      : leetcode_in_python
  @FileName     : 1071.字符串的最大公因子.py
  @Description  : 对于字符串 S 和 T，只有在 S = T + ... + T（T 与自身连接 1 次或多次）时，我们才认定 “T 能除尽 S”。
    返回最长字符串 X，要求满足 X 能除尽 str1 且 X 能除尽 str2。
    示例 1：

    输入：str1 = "ABCABC", str2 = "ABC"
    输出："ABC"
    示例 2：

    输入：str1 = "ABABAB", str2 = "ABAB"
    输出："AB"
    示例 3：

    输入：str1 = "LEET", str2 = "CODE"
    输出：""
    提示：

    1 <= str1.length <= 1000
    1 <= str2.length <= 1000
    str1[i] 和 str2[i] 为大写英文字母
"""
from math import gcd


class Solution:
    # 56ms, 13.6MB
    @classmethod
    def gcd_of_strings(cls, str1: str, str2: str) -> str:
        candidate_len = gcd(len(str1), len(str2))
        candidate = str1[: candidate_len]
        if str1 + str2 == str2 + str1:
            return candidate

        return ''


if __name__ == '__main__':
    test_cases = [
        ('ABCABC', 'ABC'),
        ('ABABAB', 'ABAB'),
        ('LEFT', 'CODE')
    ]
    for tc in test_cases:
        print(Solution.gcd_of_strings(*tc))
