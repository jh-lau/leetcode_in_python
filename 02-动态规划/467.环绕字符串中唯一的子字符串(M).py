"""
  @Author       : Liujianhan
  @Date         : 20/4/19 21:30
  @FileName     : 467.环绕字符串中唯一的子字符串(M).py
  @ProjectName  : leetcode_in_python
  @Description  : 把字符串 s 看作是“abcdefghijklmnopqrstuvwxyz”的无限环绕字符串，所以 s 看起来是这样的："...zabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcd....". 
    现在我们有了另一个字符串 p 。你需要的是找出 s 中有多少个唯一的 p 的非空子串，尤其是当你的输入是字符串 p ，你需要输出字符串 s 中 p 的不同的非空子串的数目。 
    注意: p 仅由小写的英文字母组成，p 的大小可能超过 10000。
    示例 1:

    输入: "a"
    输出: 1
    解释: 字符串 S 中只有一个"a"子字符。

    示例 2:

    输入: "cac"
    输出: 2
    解释: 字符串 S 中的字符串“cac”只有两个子串“a”、“c”。.

    示例 3:

    输入: "zab"
    输出: 6
    解释: 在字符串 S 中有六个子串“z”、“a”、“b”、“za”、“ab”、“zab”。.
 """
from string import ascii_lowercase


class Solution:
    # 136ms, 13.8MB
    @classmethod
    def find_substring_in_wrap_round_string(cls, p: str) -> int:
        if len(p) == 0:
            return 0
        dp = [0 for _ in range(26)]
        dp[ord(p[0]) - ord('a')] = 1
        k = 1
        for i in range(1, len(p)):
            if (ord(p[i]) - ord(p[i - 1]) + 26) % 26 == 1:
                k += 1
                dp[ord(p[i]) - ord('a')] = max(dp[ord(p[i]) - ord('a')], k)
            else:
                k = 1
                if dp[ord(p[i]) - ord('a')] == 0:
                    dp[ord(p[i]) - ord('a')] = 1

        sum_val = 0
        for i in dp:
            sum_val += i
        return sum_val

    # 100ms, 13.7MB
    @classmethod
    def find_substring_in_wrap_round_string_v2(cls, p: str) -> int:
        if p:
            max_len = dict.fromkeys(ascii_lowercase, 0)
            table = dict(zip(ascii_lowercase, range(26)))
            prev_len, right, p = 1, {1, -25}, p[0] + p
            for i, j in zip(p[1:], p[:-1]):
                if table[i] - table[j] in right:
                    prev_len += 1
                else:
                    prev_len = 1
                max_len[i] = max(max_len[i], prev_len)
            return sum(i for i in max_len.values())
        return 0


if __name__ == '__main__':
    test_cases = ['a', 'cac', 'zab']
    for tc in test_cases:
        print(Solution.find_substring_in_wrap_round_string(tc))
