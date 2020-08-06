"""
  @Author       : liujianhan
  @Date         : 2020/8/6 上午9:28
  @Project      : leetcode_in_python
  @FileName     : 336.回文对(H).py
  @Description  : 给定一组唯一的单词， 找出所有不同 的索引对(i, j)，使得列表中的两个单词， words[i] + words[j] ，可拼接成回文串。

    示例 1:

    输入: ["abcd","dcba","lls","s","sssll"]
    输出: [[0,1],[1,0],[3,2],[2,4]]
    解释: 可拼接成的回文串为 ["dcbaabcd","abcddcba","slls","llssssll"]
    示例 2:

    输入: ["bat","tab","cat"]
    输出: [[0,1],[1,0]]
    解释: 可拼接成的回文串为 ["battab","tabbat"]
"""
from typing import List


class Solution:
    # 708ms, 15MB
    @staticmethod
    def palindrome_pairs(words: List[str]) -> List[List[int]]:
        def find_word(s: str, left: int, right: int) -> int:
            return indices.get(s[left:right + 1], -1)

        def is_palindrome(s: str, left: int, right: int) -> bool:
            sub = s[left:right + 1]
            return sub == sub[::-1]

        indices = {word[::-1]: i for i, word in enumerate(words)}

        ret = list()
        for i, word in enumerate(words):
            m = len(word)
            for j in range(m + 1):
                if is_palindrome(word, j, m - 1):
                    left_id = find_word(word, 0, j - 1)
                    if left_id != -1 and left_id != i:
                        ret.append([i, left_id])
                if j and is_palindrome(word, 0, j - 1):
                    right_id = find_word(word, j, m - 1)
                    if right_id != -1 and right_id != i:
                        ret.append([right_id, i])

        return ret


if __name__ == '__main__':
    test_cases = [
        ["abcd", "dcba", "lls", "s", "sssll"],
        ["bat", "tab", "cat"]
    ]
    for tc in test_cases:
        print(Solution.palindrome_pairs(tc))
