"""
  @Author       : Liujianhan
  @Date         : 20/5/10 15:04
  @FileName     : 126.单词接龙II(H).py
  @ProjectName  : leetcode_in_python
  @Description  : 给定两个单词（beginWord 和 endWord）和一个字典 wordList，找出所有从 beginWord 到 endWord 的最短转换序列。转换需遵循如下规则：
    每次转换只能改变一个字母。
    转换过程中的中间单词必须是字典中的单词。
    说明:
    如果不存在这样的转换序列，返回一个空列表。
    所有单词具有相同的长度。
    所有单词只由小写字母组成。
    字典中不存在重复的单词。
    你可以假设 beginWord 和 endWord 是非空的，且二者不相同。
    示例 1:
    输入:
    beginWord = "hit",
    endWord = "cog",
    wordList = ["hot","dot","dog","lot","log","cog"]
    输出:
    [
      ["hit","hot","dot","dog","cog"],
      ["hit","hot","lot","log","cog"]
    ]
    示例 2:
    输入:
    beginWord = "hit"
    endWord = "cog"
    wordList = ["hot","dot","dog","lot","log"]
    输出: []
    解释: endWord "cog" 不在字典中，所以不存在符合要求的转换序列。
 """
from collections import defaultdict, deque
from typing import List


class Solution:
    # 136ms, 17.9MB
    @classmethod
    def find_ladders(cls, begin_word: str, end_word: str, word_list: List[str]) -> List[List[str]]:
        word_list.append(begin_word)
        buckets = defaultdict(list)
        for word in word_list:
            for i in range(len(begin_word)):
                match = word[:i] + '_' + word[i + 1:]
                buckets[match].append(word)
        pre_words = defaultdict(list)
        to_seen = deque([(begin_word, 1)])
        be_found = {begin_word: 1}
        while to_seen:
            cur_word, level = to_seen.popleft()
            for i in range(len(begin_word)):
                match = cur_word[:i] + '_' + cur_word[i + 1:]
                for word in buckets[match]:
                    if word not in be_found:
                        be_found[word] = level + 1
                        to_seen.append((word, level + 1))
                    if be_found[word] == level + 1:
                        pre_words[word].append(cur_word)
            if end_word in be_found and level + 1 > be_found[end_word]:
                break

        if end_word in be_found:
            res = [[end_word]]
            while res[0][0] != begin_word:
                res = [[word] + r for r in res for word in pre_words[r[0]]]
            return res
        else:
            return []


if __name__ == '__main__':
    test_cases = [
        ('hit', 'cog', ["hot", "dot", "dog", "lot", "log", "cog"]),
        ('hit', 'cog', ["hot", "dot", "dog", "lot", "log"]),
    ]
    for tc in test_cases:
        print(Solution.find_ladders(*tc))
