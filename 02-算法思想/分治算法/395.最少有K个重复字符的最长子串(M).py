"""
  @Author       : liujianhan
  @Date         : 21/2/27 10:12
  @Project      : leetcode_in_python
  @FileName     : 395.最少有K个重复字符的最长子串(M).py
  @Description  : 给你一个字符串 s 和一个整数 k ，请你找出 s 中的最长子串， 要求该子串中的每一字符出现次数都不少于 k 。返回这一子串的长度。

    示例 1：
    输入：s = "aaabb", k = 3
    输出：3
    解释：最长子串为 "aaa" ，其中 'a' 重复了 3 次。

    示例 2：
    输入：s = "ababbc", k = 2
    输出：5
    解释：最长子串为 "ababb" ，其中 'a' 重复了 2 次， 'b' 重复了 3 次。
     
    提示：
    1 <= s.length <= 104
    s 仅由小写英文字母组成
    1 <= k <= 105
"""


class Solution:
    # 40ms, 15MB
    @staticmethod
    def longest_substring(s: str, k: int) -> int:
        stack = [s]
        ans = 0
        while stack:
            cur = stack.pop()
            for c in set(cur):
                if cur.count(c) < k:
                    stack.extend([t for t in cur.split(c)])
                    break
            else:
                ans = max(ans, len(cur))
        return ans


if __name__ == '__main__':
    test_cases = [
        ("aaabb", 3),
        ("ababbc", 2),
    ]
    for test_case in test_cases:
        print(Solution.longest_substring(*test_case))
