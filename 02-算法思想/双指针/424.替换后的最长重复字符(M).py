"""
  @Author       : liujianhan
  @Date         : 2021/2/2 9:33
  @Project      : leetcode_in_python
  @FileName     : 424.替换后的最长重复字符(M).py
  @Description  : 给你一个仅由大写英文字母组成的字符串，你可以将任意位置上的字符替换成另外的字符，总共可最多替换 k 次。在执行上述操作后，找到包含重复字母的最长子串的长度。
    注意：字符串长度 和 k 不会超过 104。
     
    示例 1：
    输入：s = "ABAB", k = 2
    输出：4
    解释：用两个'A'替换为两个'B',反之亦然。

    示例 2：
    输入：s = "AABABBA", k = 1
    输出：4
    解释：
    将中间的一个'A'替换为'B',字符串变为 "AABBBBA"。
    子串 "BBBB" 有最长重复字母, 答案为 4。
"""
from collections import defaultdict


class Solution:
    # 88ms, 15.5MB
    @staticmethod
    def character_replacement(s: str, k: int) -> int:
        d = defaultdict(list)
        for i, c in enumerate(s):
            d[c].append(i)
        m = 0
        for a in d.values():
            i = 0
            for j in range(m + 1, len(a)):
                if j - i <= m:
                    continue
                t = a[j] - j - k
                while a[i] - i < t:
                    i += 1
                m = max(m, j - i)
        return min(len(s), m + k + 1)


if __name__ == '__main__':
    test_cases = [
        ("ABAB", 2),
        ("AABABBA", 1),
    ]
    for tc in test_cases:
        print(Solution.character_replacement(*tc))
