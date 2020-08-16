"""
  @Author       : Liujianhan
  @Date         : 20/4/4 21:08
  @FileName     : 387.字符串中的第一个唯一字符.py
  @ProjectName  : leetcode_in_python
  @Description  : 给定一个字符串，找到它的第一个不重复的字符，并返回它的索引。如果不存在，则返回 -1。

    s = "leetcode"
    返回 0.

    s = "loveleetcode",
    返回 2.
 """


class Solution:
    # 116ms, 13.7MB
    @classmethod
    def first_uniq_char(cls, s: str) -> int:
        """<哈希表>"""
        s_dict = dict()
        for char in s:
            s_dict[char] = s_dict.get(char, 0) + 1
        unique_dict = [k for k, v in s_dict.items() if v == 1]

        return min([s.index(i) for i in unique_dict]) if unique_dict else -1

    # 84ms, 13.9MB
    @classmethod
    def first_uniq_char_v2(cls, s: str) -> int:
        # 类Counter写法
        s_dict = {c: s.count(c) for c in set(s)}
        for i, c in enumerate(s):
            if s_dict[c] == 1:
                return i

        return -1

    # 36ms, 13.8MB
    @classmethod
    def first_uniq_char_v3(cls, s: str) -> int:
        min_unique_char_index = len(s)

        for c in "abcdefghijklmnopqrstuvwxyz":
            i = s.find(c)
            if i != -1 and i == s.rfind(c):
                min_unique_char_index = min(min_unique_char_index, i)

        return min_unique_char_index if min_unique_char_index != len(s) else -1

    # 172ms, 13.8MB
    @classmethod
    def first_uniq_char_v4(cls, s: str) -> int:
        for c in s:
            if s.find(c) == s.rfind(c):
                return s.find(c)

        return -1


if __name__ == '__main__':
    test_cases = ['', 'aadd', 'leetcode', 'loveleetcode']
    for tc in test_cases:
        print(tc, Solution.first_uniq_char(tc))
        print(tc, Solution.first_uniq_char_v2(tc))
        print(tc, Solution.first_uniq_char_v3(tc))
