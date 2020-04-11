"""
  @Author       : liujianhan
  @Date         : 2020/4/8 下午5:26
  @Project      : leetcode_in_python
  @FileName     : 01.04.回文排列.py
  @Description  : 给定一个字符串，编写一个函数判定其是否为某个回文串的排列之一。
    回文串是指正反两个方向都一样的单词或短语。排列是指字母的重新排列。
    回文串不一定是字典当中的单词。

    示例1：

    输入："tactcoa"
    输出：true（排列有"tacocat"、"atcocta"，等等）
"""


class Solution:
    # 44ms, 13.4MB
    @classmethod
    def can_permute_palindrome(cls, s: str) -> bool:
        dic = {k: s.count(k) for k in s}
        # 全为偶数，或者奇数只有一个的情况为真，其他均为假
        return bool(sum([1 for value in dic.values() if value % 2]) < 2)


if __name__ == '__main__':
    test_cases = ['tactcoa', 'abcba', 'abbccd', 'aa']
    for tc in test_cases:
        print(Solution.can_permute_palindrome(tc))