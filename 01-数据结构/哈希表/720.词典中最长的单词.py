"""
  @Author       : liujianhan
  @Date         : 2020/11/26 16:18
  @Project      : leetcode_in_python
  @FileName     : 720.词典中最长的单词.py
  @Description  : 给出一个字符串数组words组成的一本英语词典。从中找出最长的一个单词，
    该单词是由words词典中其他单词逐步添加一个字母组成。若其中有多个可行的答案，则返回答案中字典序最小的单词。
    若无答案，则返回空字符串。
    示例 1：
    输入：
    words = ["w","wo","wor","worl", "world"]
    输出："world"
    解释：
    单词"world"可由"w", "wo", "wor", 和 "worl"添加一个字母组成。
    示例 2：
    输入：
    words = ["a", "banana", "app", "appl", "ap", "apply", "apple"]
    输出："apple"
    解释：
    "apply"和"apple"都能由词典中的单词组成。但是"apple"的字典序小于"apply"。
    提示：
    所有输入的字符串都只包含小写字母。
    words数组长度范围为[1,1000]。
    words[i]的长度范围为[1,30]。
"""
from typing import List


class Solution:
    # 6780ms, 14MB
    @staticmethod
    def longest_word(words: List[str]) -> str:
        words.sort(key=len, reverse=True)
        longest_length = 0
        result = []
        for w in words:
            if len(w) < longest_length:
                break
            if all([w[:i] in set(words) for i in range(1, len(w))]):
                longest_length = max(longest_length, len(w))
                result.append(w)
        return sorted(result)[0] if result else ''

    # 7244ms, 13.8MB
    @staticmethod
    def longest_word_v2(words: List[str]) -> str:
        words.sort(key=len, reverse=True)
        longest_length = 0
        result = []
        for w in words:
            if len(w) < longest_length:
                break
            for i in range(len(w)):
                if w[:i + 1] not in set(words):
                    break
                if i == len(w) - 1:
                    longest_length = max(longest_length, len(w))
                    result.append(w)
        return sorted(result)[0] if result else ''

    # 128ms, 13.8MB
    @staticmethod
    def longest_word_v3(words: List[str]) -> str:
        ans = ''
        words_set = set(words)
        for i in words_set:
            if len(i) > len(ans) or (len(i) == len(ans) and i < ans):
                if all((i[:k] in words_set) for k in range(1, len(i) + 1)):
                    ans = i
        return ans

    # 80ms, 13.MB
    @staticmethod
    def longest_word_v4(words: List[str]) -> str:
        words.sort()
        words.sort(key=len, reverse=True)
        words_set = set(words)
        for w in words:
            flag = False
            for i in range(1, len(w) + 1):
                if w[:i] not in words_set:
                    flag = False
                    break
                else:
                    flag = True
            if flag:
                return w
        return ''


if __name__ == '__main__':
    test_cases = [
        ["w", "wo", "wor", "worl", "world"],
        ["a", "banana", "app", "appl", "ap", "apply", "apple"],
        ["yo", "ew", "fc", "zrc", "yodn", "fcm", "qm", "qmo", "fcmz", "z", "ewq", "yod", "ewqz", "y"],
        ["k", "lg", "it", "oidd", "oid", "oiddm", "kfk", "y", "mw", "kf", "l", "o", "mwaqz", "oi", "ych", "m", "mwa"],
        ["ogz", "eyj", "e", "ey", "hmn", "v", "hm", "ogznkb", "ogzn", "hmnm", "eyjuo", "vuq", "ogznk", "og", "eyjuoi",
         "d"],
        ["ts", "e", "x", "pbhj", "opto", "xhigy", "erikz", "pbh", "opt", "erikzb", "eri", "erik", "xlye", "xhig",
         "optoj", "optoje", "xly", "pb", "xhi", "x", "o"]
    ]
    for tc in test_cases:
        # print(Solution.longest_word(tc))
        # print(Solution.longest_word_v2(tc))
        print(Solution.longest_word_v3(tc))
