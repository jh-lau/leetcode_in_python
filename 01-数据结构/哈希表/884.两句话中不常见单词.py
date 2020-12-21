"""
  @Author       : liujianhan
  @Date         : 20/12/19 0:10
  @Project      : leetcode_in_python
  @FileName     : 884.两句话中不常见单词.py
  @Description  : 给定两个句子 A 和 B 。 （句子是一串由空格分隔的单词。每个单词仅由小写字母组成。）
    如果一个单词在其中一个句子中只出现一次，在另一个句子中却没有出现，那么这个单词就是不常见的。
    返回所有不常用单词的列表。
    您可以按任何顺序返回列表。
     
    示例 1：
    输入：A = "this apple is sweet", B = "this apple is sour"
    输出：["sweet","sour"]

    示例 2：
    输入：A = "apple apple", B = "banana"
    输出：["banana"]

    提示：

    0 <= A.length <= 200
    0 <= B.length <= 200
    A 和 B 都只包含空格和小写字母。
"""
from typing import List
from collections import Counter


class Solution:
    # 24ms, 14.8MB
    @staticmethod
    def uncommon_from_sentences(A: str, B: str) -> List[str]:
        a = A.split()
        b = B.split()
        diff = set(a) ^ set(b)
        a_dict = Counter(a)
        b_dict = Counter(b)
        res = []
        for word in diff:
            if a_dict.get(word, 0) == 1 or b_dict.get(word, 0) == 1:
                res.append(word)

        return res

    # 24ms, 14.7MB
    @staticmethod
    def uncommon_from_sentences_v2(A: str, B: str) -> List[str]:
        count = Counter(A.split() + B.split())
        return [k for k, v in count.items() if v == 1]


if __name__ == '__main__':
    test_cases = [
        ("this apple is sweet", "this apple is sour"),
        ('apple apple', 'banana')
    ]
    for tc in test_cases:
        print(Solution.uncommon_from_sentences(*tc))
        print(Solution.uncommon_from_sentences_v2(*tc))
