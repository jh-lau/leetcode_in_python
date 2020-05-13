"""
  @Author       : liujianhan
  @Date         : 2020/5/13 上午11:34
  @Project      : leetcode_in_python
  @FileName     : 140.单词拆分II(H).py
  @Description  : 给定一个非空字符串 s 和一个包含非空单词列表的字典 wordDict，在字符串中增加空格来构建一个句子，使得句子中所有的单词都在词典中。返回所有这些可能的句子。

    说明：
    分隔时可以重复使用字典中的单词。
    你可以假设字典中没有重复的单词。
    示例 1：

    输入:
    s = "catsanddog"
    wordDict = ["cat", "cats", "and", "sand", "dog"]
    输出:
    [
      "cats and dog",
      "cat sand dog"
    ]
    示例 2：

    输入:
    s = "pineapplepenapple"
    wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]
    输出:
    [
      "pine apple pen apple",
      "pineapple pen apple",
      "pine applepen apple"
    ]
    解释: 注意你可以重复使用字典中的单词。
    示例 3：

    输入:
    s = "catsandog"
    wordDict = ["cats", "dog", "sand", "and", "cat"]
    输出:
    []
"""
from typing import List


class Solution:
    # 60ms, 13.8MB
    @classmethod
    def word_break(cls, s: str, word_dict: List[str]) -> List[str]:
        def dfs(idx):
            if idx not in cache:
                result = []
                for i in range(idx + 1, len(s) + 1):
                    if s[idx:i] in word_set:
                        for sub in dfs(i):
                            if sub:
                                result.append(s[idx:i] + " " + sub)
                            else:
                                result.append(s[idx:i])
                cache[idx] = result
            return cache[idx]

        cache = {len(s): [""]}
        word_set = set(word_dict)
        return dfs(0)

    # 52ms, 13.7MB
    @classmethod
    def word_break_v2(cls, s: str, word_dict: List[str]) -> List[str]:
        words = set(word_dict)
        n = len(s)
        dp1 = [False] * (n + 1)
        dp1[0] = True
        for i in range(1, n + 1):
            for j in range(i - 1, -1, -1):
                if dp1[j] and s[j:i] in words:
                    dp1[i] = True
                    break

        dp = [[] for _ in range(n + 1)]
        if dp1[-1]:
            dp[0] = [""]
            for i in range(1, n + 1):
                for j in range(i - 1, -1, -1):
                    if s[j:i] in words:
                        for sub in dp[j]:
                            if sub:
                                dp[i].append(sub + " " + s[j:i])
                            else:
                                dp[i].append(s[j:i])
        return dp[-1]


if __name__ == '__main__':
    test_cases = [
        ('catsanddog', ["cat", "cats", "and", "sand", "dog"]),
        ('pineapplepenapple', ["apple", "pen", "applepen", "pine", "pineapple"]),
        ('catsandog', ["cats", "dog", "sand", "and", "cat"])
    ]
    for tc in test_cases:
        print(Solution.word_break(*tc))
        print(Solution.word_break_v2(*tc))
