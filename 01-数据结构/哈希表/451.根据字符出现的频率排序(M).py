"""
  @Author       : liujianhan
  @Date         : 2020/9/18 20:00
  @Project      : leetcode_in_python
  @FileName     : 451.根据字符出现的频率排序(M).py
  @Description  : 定一个字符串，请将字符串里的字符按照出现的频率降序排列。

    示例 1:

    输入:
    "tree"

    输出:
    "eert"

    解释:
    'e'出现两次，'r'和't'都只出现一次。
    因此'e'必须出现在'r'和't'之前。此外，"eetr"也是一个有效的答案。
    示例 2:

    输入:
    "cccaaa"

    输出:
    "cccaaa"

    解释:
    'c'和'a'都出现三次。此外，"aaaccc"也是有效的答案。
    注意"cacaca"是不正确的，因为相同的字母必须放在一起。
    示例 3:

    输入:
    "Aabb"

    输出:
    "bbAa"

    解释:
    此外，"bbaA"也是一个有效的答案，但"Aabb"是不正确的。
    注意'A'和'a'被认为是两种不同的字符。
"""
import heapq
from collections import defaultdict


class Solution:
    # 252ms, 27MB
    @staticmethod
    def frequency_sort(s: str) -> str:
        count_frequency = defaultdict(int)
        for i in s:
            count_frequency[i] += 1
        lst = []
        heapq.heapify(lst)
        for i in count_frequency:
            for j in range(count_frequency[i]):
                heapq.heappush(lst, (-count_frequency[i], i))

        return ''.join([heapq.heappop(lst)[1] for _ in range(len(s))])

    # 84ms, 25MB
    @staticmethod
    def frequency_sort_v2(s: str) -> str:
        ret = []
        count_frequency = defaultdict(int)
        for i in s:
            count_frequency[i] += 1
        buckets = [[] for _ in range(len(s) + 1)]
        for i in count_frequency:
            buckets[count_frequency[i]].extend(i * count_frequency[i])
        for i in buckets[::-1]:
            if (i):
                ret.extend(i)
        return ''.join(ret)


if __name__ == '__main__':
    test_cases = [
        'tree', 'cccaaa', 'Aabb'
    ]
    for tc in test_cases:
        print(Solution.frequency_sort(tc))
        print(Solution.frequency_sort_v2(tc))
