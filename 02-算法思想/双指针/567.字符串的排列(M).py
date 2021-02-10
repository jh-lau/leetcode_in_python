"""
  @Author       : liujianhan
  @Date         : 21/2/10 22:26
  @Project      : leetcode_in_python
  @FileName     : 567.字符串的排列(M).py
  @Description  : 给定两个字符串 s1 和 s2，写一个函数来判断 s2 是否包含 s1 的排列。
    换句话说，第一个字符串的排列之一是第二个字符串的子串。

    示例1:
    输入: s1 = "ab" s2 = "eidbaooo"
    输出: True
    解释: s2 包含 s1 的排列之一 ("ba").

    示例2:
    输入: s1= "ab" s2 = "eidboaoo"
    输出: False
    注意：

    输入的字符串只包含小写字母
    两个字符串的长度都在 [1, 10,000] 之间
"""
from collections import defaultdict


class Solution:
    #
    @staticmethod
    def check_inclusion(s1: str, s2: str) -> bool:
        n1, n2 = len(s1), len(s2)
        if n1 > n2:
            return False
        d1 = defaultdict(int)
        d2 = defaultdict(int)
        for c in s1:
            d1[c] += 1
        for i in range(n1):
            d2[s2[i]] += 1
        if d1 == d2:
            return True
        for i in range(n1, n2):
            d2[s2[i - n1]] -= 1
            if d2[s2[i - n1]] == 0:
                del d2[s2[i - n1]]
            d2[s2[i]] += 1
            if d1 == d2:
                return True
        return False


if __name__ == '__main__':
    test_cases = [
        ("ab", "eidbaooo"),
        ("ab", "eidboaoo"),
    ]
    for tc in test_cases:
        print(Solution.check_inclusion(*tc))
