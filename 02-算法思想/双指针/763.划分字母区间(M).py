"""
  @Author       : liujianhan
  @Date         : 2020/10/22 14:08
  @Project      : leetcode_in_python
  @FileName     : 763.划分字母区间(M).py
  @Description  : 字符串 S 由小写字母组成。我们要把这个字符串划分为尽可能多的片段，同一个字母只会出现在其中的一个片段。
    返回一个表示每个字符串片段的长度的列表。
    示例 1：
    输入：S = "ababcbacadefegdehijhklij"
    输出：[9,7,8]
    解释：
    划分结果为 "ababcbaca", "defegde", "hijhklij"。
    每个字母最多出现在一个片段中。
    像 "ababcbacadefegde", "hijhklij" 的划分是错误的，因为划分的片段数较少。
    提示：
    S的长度在[1, 500]之间。
    S只包含小写字母 'a' 到 'z' 。
"""
from typing import List


class Solution:
    # 60ms, 13.4MB
    @staticmethod
    def partition_labels(S: str) -> List[int]:
        last = [0] * 26
        for i, ch in enumerate(S):
            last[ord(ch) - ord("a")] = i

        partition = list()
        start = end = 0
        for i, ch in enumerate(S):
            end = max(end, last[ord(ch) - ord("a")])
            if i == end:
                partition.append(end - start + 1)
                start = end + 1

        return partition

    # 40ms, 13.5MB
    @staticmethod
    def partition_labels_v2(S: str) -> List[int]:
        dic = {}
        for i, s1 in enumerate(S):
            dic[s1] = i
        result = []
        cur = dic[S[0]]
        for i, s1 in enumerate(S):
            if dic[s1] > cur:
                cur = dic[s1]
            if i == cur:
                result.append(cur - sum(result) + 1)
        return result



if __name__ == '__main__':
    test_cases = [
        'ababcbacadefegdehijhklij',
    ]
    for tc in test_cases:
        print(Solution.partition_labels(tc))
        print(Solution.partition_labels_v2(tc))
