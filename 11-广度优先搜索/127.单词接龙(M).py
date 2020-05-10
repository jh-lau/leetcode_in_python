"""
  @Author       : Liujianhan
  @Date         : 20/5/10 15:14
  @FileName     : 127.单词接龙(M).py
  @ProjectName  : leetcode_in_python
  @Description  : 给定两个单词（beginWord 和 endWord）和一个字典，找到从 beginWord 到 endWord 的最短转换序列的长度。转换需遵循如下规则：
    每次转换只能改变一个字母。
    转换过程中的中间单词必须是字典中的单词。
    说明:
    如果不存在这样的转换序列，返回 0。
    所有单词具有相同的长度。
    所有单词只由小写字母组成。
    字典中不存在重复的单词。
    你可以假设 beginWord 和 endWord 是非空的，且二者不相同。
    示例 1:
    输入:
    beginWord = "hit",
    endWord = "cog",
    wordList = ["hot","dot","dog","lot","log","cog"]
    输出: 5
    解释: 一个最短转换序列是 "hit" -> "hot" -> "dot" -> "dog" -> "cog",
         返回它的长度 5。
    示例 2:
    输入:
    beginWord = "hit"
    endWord = "cog"
    wordList = ["hot","dot","dog","lot","log"]
    输出: 0
    解释: endWord "cog" 不在字典中，所以无法进行转换。
 """
from collections import defaultdict
from typing import List


class Solution:
    # 152ms. 17.3MB
    @classmethod
    def ladder_length(cls, begin_word: str, end_word: str, word_list: List[str]) -> int:
        if end_word not in word_list or not end_word or not begin_word or not word_list:
            return 0

        m = len(begin_word)
        all_combo_dict = defaultdict(list)
        for word in word_list:
            for i in range(m):
                all_combo_dict[word[:i] + '*' + word[i + 1:]].append(word)
        queue = [(begin_word, 1)]
        visited = {begin_word: True}
        while queue:
            cur_word, level = queue.pop(0)
            for i in range(m):
                intermediate_word = cur_word[:i] + '*' + cur_word[i + 1:]
                for word in all_combo_dict[intermediate_word]:
                    if word == end_word:
                        return level + 1
                    if word not in visited:
                        visited[word] = True
                        queue.append((word, level + 1))
                all_combo_dict[intermediate_word] = []

        return 0


if __name__ == '__main__':
    test_cases = [
        ('hit', 'cog', ["hot", "dot", "dog", "lot", "log", "cog"]),
        ('hit', 'cog', ["hot", "dot", "dog", "lot", "log"])
    ]
    for tc in test_cases:
        print(Solution.ladder_length(*tc))
