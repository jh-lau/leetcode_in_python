"""
  @Author       : liujianhan
  @Date         : 21/2/28 11:54
  @Project      : leetcode_in_python
  @FileName     : 1160.拼写单词.py
  @Description  : 给你一份『词汇表』（字符串数组） words 和一张『字母表』（字符串） chars。
    假如你可以用 chars 中的『字母』（字符）拼写出 words 中的某个『单词』（字符串），那么我们就认为你掌握了这个单词。
    注意：每次拼写（指拼写词汇表中的一个单词）时，chars 中的每个字母都只能用一次。
    返回词汇表 words 中你掌握的所有单词的 长度之和。

    示例 1：
    输入：words = ["cat","bt","hat","tree"], chars = "atach"
    输出：6
    解释：
    可以形成字符串 "cat" 和 "hat"，所以答案是 3 + 3 = 6。

    示例 2：
    输入：words = ["hello","world","leetcode"], chars = "welldonehoneyr"
    输出：10
    解释：
    可以形成字符串 "hello" 和 "world"，所以答案是 5 + 5 = 10。
     
    提示：
    1 <= words.length <= 1000
    1 <= words[i].length, chars.length <= 100
    所有字符串中都仅包含小写英文字母
"""
from typing import List
from collections import Counter


class Solution:
    # 400ms, 15.4MB
    @staticmethod
    def count_characters(words: List[str], chars: str) -> int:
        res = 0
        for word in words:
            char_counter = Counter(chars)
            char_counter.subtract(Counter(word))
            if all([v >= 0 for v in char_counter.values()]):
                res += len(word)

        return res

    # 120ms, 15.1MB
    @staticmethod
    def count_characters_v2(words: List[str], chars: str) -> int:
        res = 0
        d = Counter(chars)
        for word in words:
            for s in word:
                if word.count(s) > d[s]:
                    break
            else:  # for的else 只有 for正常执行完才执行
                res += len(word)
        return res


if __name__ == '__main__':
    test_cases = [
        (["cat", "bt", "hat", "tree"], "atach"),
        (["hello", "world", "leetcode"], "welldonehoneyr"),
    ]
    for test_case in test_cases:
        print(Solution.count_characters(*test_case))
