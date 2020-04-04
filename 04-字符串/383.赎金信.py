"""
  @Author       : Liujianhan
  @Date         : 20/4/4 20:57
  @FileName     : 383.赎金信.py
  @ProjectName  : leetcode_in_python
  @Description  : 给定一个赎金信 (ransom) 字符串和一个杂志(magazine)字符串，判断第一个字符串ransom能不能由第二个字符串magazines里面的字符构成。如果可以构成，返回 true ；否则返回 false。
    (题目说明：为了不暴露赎金信字迹，要从杂志上搜索各个需要的字母，组成单词来表达意思。)
    注意：
    你可以假设两个字符串均只含有小写字母。
    canConstruct("a", "b") -> false
    canConstruct("aa", "ab") -> false 杂志中的每个字母只能用一次
    canConstruct("aa", "aab") -> true
 """
from collections import Counter


class Solution:
    # 56ms, 13.8MB
    @classmethod
    def can_construct(cls, ransom_note: str, magazine: str) -> bool:
        return Counter(ransom_note) & Counter(magazine) == Counter(ransom_note)


if __name__ == '__main__':
    test_cases = [('a', 'b'), ('aa', 'ab'), ('aa', 'aab')]
    for tc in test_cases:
        print(Solution.can_construct(*tc))

