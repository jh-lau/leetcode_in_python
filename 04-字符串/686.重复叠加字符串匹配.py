"""
  @Author       : Liujianhan
  @Date         : 20/4/6 0:05
  @FileName     : 686. 重复叠加字符串匹配.py
  @ProjectName  : leetcode_in_python
  @Description  : 给定两个字符串 A 和 B, 寻找重复叠加字符串A的最小次数，使得字符串B成为叠加后的字符串A的子串，如果不存在则返回 -1。
举个例子，A = "abcd"，B = "cdabcdab"。
答案为 3， 因为 A 重复叠加三遍后为 “abcdabcdabcd”，此时 B 是其子串；A 重复叠加两遍后为"abcdabcd"，B 并不是其子串。
注意:
 A 与 B 字符串的长度在1和10000区间范围内。
 """


class Solution:
    # 136ms, 13.5MB
    @classmethod
    def repeated_string_match(cls, a: str, b: str) -> int:
        max_len = len(2 * a + b)
        i = 1
        c = a
        while len(c) <= max_len:
            if b in c:
                return i
            else:
                i += 1
                c += a
        return -1

    # 40ms, 13.7MB
    @classmethod
    def repeated_string_match_v2(cls, a: str, b: str) -> int:
        if len(set(a)) < len(set(b)):
            return -1
        i = max(1, len(b) // len(a))
        while True:
            c = a * i
            if b in c:
                return i
            if len(c) >= 2 * len(b) and i > 1:
                return -1
            i += 1


if __name__ == '__main__':
    test_cases = [('abcd', 'cdabcdab')]
    for tc in test_cases:
        print(Solution.repeated_string_match(*tc))
        print(Solution.repeated_string_match_v2(*tc))
