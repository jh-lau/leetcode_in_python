"""
  @Author       : liujianhan
  @Date         : 2020/4/17 上午11:20
  @Project      : leetcode_in_python
  @FileName     : 1170.比较字符串最小字母出现频次.py
  @Description  : 我们来定义一个函数 f(s)，其中传入参数 s 是一个非空字符串；该函数的功能是统计 s  中（按字典序比较）最小字母的出现频次。
    例如，若 s = "dcce"，那么 f(s) = 2，因为最小的字母是 "c"，它出现了 2 次。
    现在，给你两个字符串数组待查表 queries 和词汇表 words，请你返回一个整数数组 answer 作为答案，其中每个 answer[i] 是满足
     f(queries[i]) < f(W) 的词的数目，W 是词汇表 words 中的词。
    示例 1：
    输入：queries = ["cbd"], words = ["zaaaz"]
    输出：[1]
    解释：查询 f("cbd") = 1，而 f("zaaaz") = 3 所以 f("cbd") < f("zaaaz")。
    示例 2：
    输入：queries = ["bbb","cc"], words = ["a","aa","aaa","aaaa"]
    输出：[1,2]
    解释：第一个查询 f("bbb") < f("aaaa")，第二个查询 f("aaa") 和 f("aaaa") 都 > f("cc")。
    提示：

    1 <= queries.length <= 2000
    1 <= words.length <= 2000
    1 <= queries[i].length, words[i].length <= 10
    queries[i][j], words[i][j] 都是小写英文字母
"""
import bisect
from typing import List


class Solution:
    # 836ms, 14.1MB
    @classmethod
    def num_smaller_by_frequency(cls, queries: List[str], words: List[str]) -> List[int]:
        if not queries and not words:
            return

        query_length = len(queries)
        word_length = len(words)
        word_result = []
        answer = [0] * query_length
        for j in range(word_length):
            sorted_words = sorted(words[j])
            if len(sorted_words) == 0:
                word_result.append(0)
            else:
                word_result.append(sorted_words.count(sorted_words[0]))

        for i in range(query_length):
            sorted_query = sorted(queries[i])
            if len(sorted_query) == 0:
                query_num = 0
            else:
                query_num = sorted_query.count(sorted_query[0])
            answer[i] = sum([1 if c > query_num else 0 for c in word_result])

        return answer

    # 124ms, 13.9MB
    @classmethod
    def num_smaller_by_frequency_v2(cls, queries: List[str], words: List[str]) -> List[int]:
        f = lambda x: x.count(min(x))
        n, ws = len(words), sorted(map(f, words))
        return [n - bisect.bisect(ws, i) for i in map(f, queries)]


if __name__ == '__main__':
    test_cases = [
        (["cbd"], ["zaaaz"]),
        (["bbb", "cc"], ["a", "aa", "aaa", "aaaa"])
    ]
    for tc in test_cases:
        print(Solution.num_smaller_by_frequency(*tc))
        print(Solution.num_smaller_by_frequency_v2(*tc))
