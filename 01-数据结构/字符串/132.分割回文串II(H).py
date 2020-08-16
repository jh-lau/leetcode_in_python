"""
  @Author       : Liujianhan
  @Date         : 20/5/12 21:50
  @FileName     : 132.分割回文串II(H).py
  @ProjectName  : leetcode_in_python
  @Description  : 给定一个字符串 s，将 s 分割成一些子串，使每个子串都是回文串。
    返回符合要求的最少分割次数。
    示例:
    输入: "aab"
    输出: 1
    解释: 进行一次分割就可将 s 分割成 ["aa","b"] 这样两个回文子串。
 """


class Solution:
    # 540ms, 30.4MB
    @classmethod
    def min_cut(cls, s: str) -> int:
        min_cut = list(range(len(s)))
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        for j in range(n):
            for i in range(j + 1):
                if s[i] == s[j] and (j - i < 2 or dp[i + 1][j - 1]):
                    dp[i][j] = True
                    if not i:
                        min_cut[j] = 0
                    else:
                        min_cut[j] = min(min_cut[j], min_cut[i - 1] + 1)

        return min_cut[-1]


if __name__ == '__main__':
    print(Solution.min_cut('aab'))
