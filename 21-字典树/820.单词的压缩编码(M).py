"""
  @Author       : Liujianhan
  @Date         : 20/3/28 18:09
  @FileName     : 820.单词的压缩编码.py
  @ProjectName  : leetcode_in_python
  @Description  : 给定一个单词列表，我们将这个列表编码成一个索引字符串 S 与一个索引列表 A。
    例如，如果这个列表是 ["time", "me", "bell"]，我们就可以将其表示为 S = "time#bell#" 和 indexes = [0, 2, 5]。
    对于每一个索引，我们可以通过从字符串 S 中索引的位置开始读取字符串，直到 "#" 结束，来恢复我们之前的单词列表。
    那么成功对给定单词列表进行编码的最小字符串长度是多少呢？

输入: words = ["time", "me", "bell"]
    输出: 10
    说明: S = "time#bell#" ， indexes = [0, 2, 5] 。
 """
from typing import List


class Solution:
    # 168ms, 14.3MB
    @classmethod
    def minimum_length_encoding(cls, words: List[str]) -> int:
        word_set = set(words)
        for word in words:
            sub_words = set([word[i:] for i in range(1, len(word))])
            word_set -= sub_words

        return sum([len(s) for s in word_set]) + len(word_set)

    # 384ms, 17MB
    @classmethod
    def minimum_length_encoding_trie(cls, words: List[str]) -> int:
        class Node:
            def __init__(self, layer):
                self.layer = layer
                self.children = {}

        root = Node(0)

        def build(t, w):
            if not w:
                return
            if w[-1] not in t.children:
                t.children[w[-1]] = Node(t.layer + 1)
            build(t.children[w[-1]], w[:-1])

        for w in words:
            build(root, w)
        ans = [0]

        def vis(t):
            if not len(t.children):
                if t.layer > 0:
                    ans[0] += t.layer + 1
            for c in t.children.values():
                vis(c)
        vis(root)

        return ans[0]


if __name__ == '__main__':
    test_case = [
        ['time', 'me', 'bell']
    ]
    for tc in test_case:
        print(Solution.minimum_length_encoding(tc))
        print(Solution.minimum_length_encoding_trie(tc))
