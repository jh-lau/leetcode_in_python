"""
  @Author       : liujianhan
  @Date         : 2020/8/4 下午7:36
  @Project      : leetcode_in_python
  @FileName     : 242.有效的字母异位词.py
  @Description  : 给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的字母异位词。

    示例 1:

    输入: s = "anagram", t = "nagaram"
    输出: true
    示例 2:

    输入: s = "rat", t = "car"
    输出: false
    说明:
    你可以假设字符串只包含小写字母。

    进阶:
    如果输入字符串包含 unicode 字符怎么办？你能否调整你的解法来应对这种情况？
"""


class Solution:
    # 84ms, 13.6MB
    @staticmethod
    def is_anagram(s: str, t: str) -> bool:
        if set(s) != set(t):
            return False
        dic = {}
        for ch in s:
            dic[ch] = dic.get(ch, 0) + 1
        for ch in t:
            dic[ch] = dic.get(ch, -1) - 1

        return True if all([s == 0 for s in dic.values()]) else False

    # 40ms, 13.8MB
    @staticmethod
    def is_anagram_v2(s: str, t: str) -> bool:
        s1, t1 = set(s), set(t)
        if s1 == t1:
            for i in s1:
                if s.count(i) != t.count(i):
                    return False
            return True
        return False


if __name__ == '__main__':
    test_cases = [
        ('anagram', 'nagaram'),
        ('rat', 'car'),
        ('a', 'ab'),
        ('ab', 'a'),
        ('aa', 'a')
    ]
    for tc in test_cases:
        print(Solution.is_anagram(*tc))
        print(Solution.is_anagram_v2(*tc))
