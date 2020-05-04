"""
  @Author       : Liujianhan
  @Date         : 20/5/4 20:58
  @FileName     : 076.最小覆盖子串(H).py
  @ProjectName  : leetcode_in_python
  @Description  : 给你一个字符串 S、一个字符串 T，请在字符串 S 里面找出：包含 T 所有字母的最小子串。
    示例：
    输入: S = "ADOBECODEBANC", T = "ABC"
    输出: "BANC"
    说明：
    如果 S 中不存这样的子串，则返回空字符串 ""。
    如果 S 中存在这样的子串，我们保证它是唯一的答案。
 """
from collections import Counter, defaultdict


class Solution:
    # 856ms, 13.9MB
    @classmethod
    def min_window(cls, s: str, t: str) -> str:
        t = Counter(t)
        lookup = Counter()
        start = end = 0
        min_len = float('inf')
        res = ''
        while end < len(s):
            lookup[s[end]] += 1
            end += 1
            while all(map(lambda x: lookup[x] >= t[x], t.keys())):
                if end - start < min_len:
                    res = s[start:end]
                    min_len = end - start
                lookup[s[start]] -= 1
                start += 1

        return res

    # 76ms, 13.8MB
    @classmethod
    def min_window_v2(cls, s: str, t: str) -> str:
        mem = defaultdict(int)
        for char in t:
            mem[char] += 1
        t_len = len(t)

        min_left, min_right = 0, len(s)
        left = 0

        for right, char in enumerate(s):
            if mem[char] > 0:
                t_len -= 1
            mem[char] -= 1

            if t_len == 0:
                while mem[s[left]] < 0:
                    mem[s[left]] += 1
                    left += 1

                if right - left < min_right - min_left:
                    min_left, min_right = left, right

                mem[s[left]] += 1
                t_len += 1
                left += 1

        return '' if min_right == len(s) else s[min_left:min_right + 1]


if __name__ == '__main__':
    print(Solution.min_window("ADOBECODEBANC", "ABC"))
    print(Solution.min_window_v2("ADOBECODEBANC", "ABC"))
