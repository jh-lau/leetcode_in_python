"""
  @Author       : Liujianhan
  @Date         : 20/5/1 16:37
  @FileName     : 030.串联所有单词的子串(H).py
  @ProjectName  : leetcode_in_python
  @Description  : 给定一个字符串 s 和一些长度相同的单词 words。找出 s 中恰好可以由 words 中所有单词串联形成的子串的起始位置。
    注意子串要与 words 中的单词完全匹配，中间不能有其他字符，但不需要考虑 words 中单词串联的顺序。
    示例 1：
    输入：
      s = "barfoothefoobarman",
      words = ["foo","bar"]
    输出：[0,9]
    解释：
    从索引 0 和 9 开始的子串分别是 "barfoo" 和 "foobar" 。
    输出的顺序不重要, [9,0] 也是有效答案。
    示例 2：
    输入：
      s = "wordgoodgoodgoodbestword",
      words = ["word","good","best","word"]
    输出：[]
 """
from collections import Counter
from typing import List


class Solution:
    # 80ms, 13.9MB
    @classmethod
    def find_substring(cls, s: str, words: List[str]) -> List[int]:
        if not s or not words:
            return []
        one_word = len(words[0])
        word_num = len(words)
        n = len(s)
        if n < one_word:
            return []
        words = Counter(words)
        res = []
        for i in range(0, one_word):
            cur_cnt = 0
            left = i
            right = i
            cur_counter = Counter()
            while right + one_word <= n:
                w = s[right:right + one_word]
                right += one_word
                if w not in words:
                    left = right
                    cur_counter.clear()
                    cur_cnt = 0
                else:
                    cur_counter[w] += 1
                    cur_cnt += 1
                    while cur_counter[w] > words[w]:
                        left_w = s[left:left + one_word]
                        left += one_word
                        cur_counter[left_w] -= 1
                        cur_cnt -= 1
                    if cur_cnt == word_num:
                        res.append(left)

        return res


if __name__ == '__main__':
    test_cases = [
        ("barfoothefoobarman", ['foo', 'bar']),
        ('wordgoodgoodgoodbestword', ["word", "good", "best", "word"])
    ]
    for tc in test_cases:
        print(Solution.find_substring(*tc))
