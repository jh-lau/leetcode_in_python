"""
  @Author       : Liujianhan
  @Date         : 20/5/5 16:37
  @FileName     : 087.扰乱字符串(H).py
  @ProjectName  : leetcode_in_python
  @Description  : 给定一个字符串 s1，我们可以把它递归地分割成两个非空子字符串，从而将其表示为二叉树。
    下图是字符串 s1 = "great" 的一种可能的表示形式。
        great
       /    \
      gr    eat
     / \    /  \
    g   r  e   at
               / \
              a   t
    在扰乱这个字符串的过程中，我们可以挑选任何一个非叶节点，然后交换它的两个子节点。
    例如，如果我们挑选非叶节点 "gr" ，交换它的两个子节点，将会产生扰乱字符串 "rgeat" 。
        rgeat
       /    \
      rg    eat
     / \    /  \
    r   g  e   at
               / \
              a   t
    我们将 "rgeat” 称作 "great" 的一个扰乱字符串。
        rgtae
       /    \
      rg    tae
     / \    /  \
    r   g  ta  e
           / \
          t   a
    我们将 "rgtae” 称作 "great" 的一个扰乱字符串。
    给出两个长度相等的字符串 s1 和 s2，判断 s2 是否是 s1 的扰乱字符串。
    示例 1:
    输入: s1 = "great", s2 = "rgeat"
    输出: true
    示例 2:
    输入: s1 = "abcde", s2 = "caebd"
    输出: false
 """


class Solution:
    # 292ms, 13.7MB
    @classmethod
    def is_scramble(cls, s1: str, s2: str) -> bool:
        """动态规划"""
        l = len(s1)
        if l != len(s2): return False
        dp = [[None for _ in range(l)] for _ in range(l)]
        for i in range(l):
            for j in range(l):
                dp[i][j] = [False] * (min(l - i, l - j) + 1)
        for i in range(l):
            for j in range(l):
                dp[i][j][1] = s1[i] == s2[j]
        for length in range(2, l + 1):
            for i in range(l - length + 1):
                for j in range(l - length + 1):
                    for sep in range(1, length):
                        if dp[i][j][sep] and dp[i + sep][j + sep][length - sep]:
                            dp[i][j][length] = True
                            break
                        if dp[i][j + length - sep][sep] and dp[i + sep][j][length - sep]:
                            dp[i][j][length] = True
                            break

        return dp[0][0][l]

    # 52ms, 13.5MB
    @classmethod
    def is_scramble_v2(cls, s1: str, s2: str) -> bool:
        """递归"""
        if len(s1) != len(s2):
            return False
        if s1 == s2:
            return True
        if sorted(s1) != sorted(s2):
            return False

        for i in range(1, len(s1)):
            if cls.is_scramble_v2(s1[:i], s2[:i]) and cls.is_scramble_v2(s1[i:], s2[i:]) \
                    or cls.is_scramble_v2(s1[:i], s2[-i:]) and cls.is_scramble_v2(s1[i:], s2[:-i]):
                return True

        return False


if __name__ == '__main__':
    test_cases = [
        ('great', 'rgeat'),
        ('abcde', 'caebd')
    ]
    for tc in test_cases:
        print(Solution.is_scramble(*tc))
        print(Solution.is_scramble_v2(*tc))
