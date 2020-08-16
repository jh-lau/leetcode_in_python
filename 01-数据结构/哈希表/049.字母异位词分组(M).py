"""
  @Author       : Liujianhan
  @Date         : 20/4/25 16:24
  @FileName     : 049.字母异位词分组(M).py
  @ProjectName  : leetcode_in_python
  @Description  : 给定一个字符串数组，将字母异位词组合在一起。字母异位词指字母相同，但排列不同的字符串。
    示例:
    输入: ["eat", "tea", "tan", "ate", "nat", "bat"]
    输出:
    [
      ["ate","eat","tea"],
      ["nat","tan"],
      ["bat"]
    ]
    说明：
    所有输入均为小写字母。
    不考虑答案输出的顺序。
 """
from collections import defaultdict
from typing import List


class Solution:
    # 60ms, 16.7MB
    @classmethod
    def group_anagrams(cls, str_list: List[str]) -> List[List[str]]:
        ans = defaultdict(list)
        for string in str_list:
            ans[tuple(sorted(string))].append(string)

        return list(ans.values())

    # 72ms, 18.7MB
    @classmethod
    def group_anagrams_v2(cls, str_list: List[str]) -> List[List[str]]:
        ans = defaultdict(list)
        for string in str_list:
            count = [0] * 26
            for c in string:
                count[ord(c) - ord('a')] += 1
            ans[tuple(count)].append(string)

        return list(ans.values())


if __name__ == '__main__':
    test_cases = [
        ["eat", "tea", "tan", "ate", "nat", "bat"]
    ]
    for tc in test_cases:
        print(Solution.group_anagrams(tc))
        print(Solution.group_anagrams_v2(tc))
