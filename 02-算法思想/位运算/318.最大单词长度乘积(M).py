"""
  @Author       : liujianhan
  @Date         : 2020/9/7 18:54
  @Project      : leetcode_in_python
  @FileName     : 318.最大单词长度乘积(M).py
  @Description  : 给定一个字符串数组 words，找到 length(word[i]) * length(word[j]) 的最大值，
  并且这两个单词不含有公共字母。你可以认为每个单词只包含小写字母。如果不存在这样的两个单词，返回 0。
    示例 1:

    输入: ["abcw","baz","foo","bar","xtfn","abcdef"]
    输出: 16
    解释: 这两个单词为 "abcw", "xtfn"。
    示例 2:

    输入: ["a","ab","abc","d","cd","bcd","abcd"]
    输出: 4
    解释: 这两个单词为 "ab", "cd"。
    示例 3:

    输入: ["a","aa","aaa","aaaa"]
    输出: 0
    解释: 不存在这样的两个单词。
"""
from collections import defaultdict
from typing import List


class Solution:
    # 176ms, 13.9MB
    @staticmethod
    def max_product(words: List[str]) -> int:
        lookup = defaultdict(int)
        for i in range(len(words)):
            mask = 0
            for alp in words[i]:
                mask |= 1 << (ord(alp) - 97)
            lookup[mask] = max(lookup[mask], len(words[i]))
        return max([lookup[x] * lookup[y] for x in lookup for y in lookup if not x & y] or [0])


if __name__ == '__main__':
    test_cases = [
        ["abcw", "baz", "foo", "bar", "xtfn", "abcdef"],
        ["a", "ab", "abc", "d", "cd", "bcd", "abcd"],
        ["a", "aa", "aaa", "aaaa"]
    ]
    for tc in test_cases:
        print(Solution.max_product(tc))
