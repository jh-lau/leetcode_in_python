"""
  @Author       : Liujianhan
  @Date         : 20/5/11 23:26
  @FileName     : 131.分割回文串(M).py
  @ProjectName  : leetcode_in_python
  @Description  : 给定一个字符串 s，将 s 分割成一些子串，使每个子串都是回文串。
    返回 s 所有可能的分割方案。
    示例:
    输入: "aab"
    输出:
    [
      ["aa","b"],
      ["a","a","b"]
    ]
 """
from typing import List


class Solution:
    # 92ms, 14MB
    @classmethod
    def partition(cls, s: str) -> List[List[str]]:
        res = []

        def helper(s, tmp):
            if not s:
                res.append(tmp)
            for i in range(1, len(s) + 1):
                if s[:i] == s[:i][::-1]:
                    helper(s[i:], tmp + [s[:i]])

        helper(s, [])
        return res


if __name__ == '__main__':
    print(Solution.partition('aab'))