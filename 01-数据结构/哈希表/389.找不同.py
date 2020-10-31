"""
  @Author       : liujianhan
  @Date         : 2020/10/31 15:55
  @Project      : leetcode_in_python
  @FileName     : 389.找不同.py
  @Description  : 给定两个字符串 s 和 t，它们只包含小写字母。
    字符串 t 由字符串 s 随机重排，然后在随机位置添加一个字母。
    请找出在 t 中被添加的字母。

    示例 1：

    输入：s = "abcd", t = "abcde"
    输出："e"
    解释：'e' 是那个被添加的字母。
    示例 2：

    输入：s = "", t = "y"
    输出："y"
    示例 3：

    输入：s = "a", t = "aa"
    输出："a"
    示例 4：

    输入：s = "ae", t = "aea"
    输出："a"
     

    提示：

    0 <= s.length <= 1000
    t.length == s.length + 1
    s 和 t 只包含小写字母
"""
from collections import defaultdict


class Solution:
    # 44ms, 13.6MB
    @staticmethod
    def find_the_difference(s: str, t: str) -> str:
        lookup = defaultdict(int)
        for char in t:
            lookup[char] += 1
        for char in s:
            lookup[char] -= 1

        return [s for s in lookup.keys() if lookup[s] != 0][0]


if __name__ == '__main__':
    test_cases = [
        ('abcd', 'abcde'),
        ('', 'y'),
        ('a', 'aa'),
        ('ae', 'aea')
    ]
    for tc in test_cases:
        print(Solution.find_the_difference(*tc))
