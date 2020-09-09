"""
  @Author       : Liujianhan
  @Date         : 20/4/19 21:47
  @FileName     : 044.通配符匹配(H).py
  @ProjectName  : leetcode_in_python
  @Description  : 给定一个字符串 (s) 和一个字符模式 (p) ，实现一个支持 '?' 和 '*' 的通配符匹配。
    '?' 可以匹配任何单个字符。
    '*' 可以匹配任意字符串（包括空字符串）。
    两个字符串完全匹配才算匹配成功。
    说明:
    s 可能为空，且只包含从 a-z 的小写字母。
    p 可能为空，且只包含从 a-z 的小写字母，以及字符 ? 和 *。
    示例 1:
    输入:
    s = "aa"
    p = "a"
    输出: false
    解释: "a" 无法匹配 "aa" 整个字符串。
    示例 2:
    输入:
    s = "aa"
    p = "*"
    输出: true
    解释: '*' 可以匹配任意字符串。
    示例 3:
    输入:
    s = "cb"
    p = "?a"
    输出: false
    解释: '?' 可以匹配 'c', 但第二个 'a' 无法匹配 'b'。
    示例 4:
    输入:
    s = "adceb"
    p = "*a*b"
    输出: true
    解释: 第一个 '*' 可以匹配空字符串, 第二个 '*' 可以匹配字符串 "dce".
    示例 5:
    输入:
    s = "acdcb"
    p = "a*c?b"
    输入: false
 """


class Solution:
    # 1580ms, 664.2MB
    @classmethod
    def remove_duplicate_stars(cls, p):
        if p == '':
            return p
        p1 = [p[0], ]
        for x in p[1:]:
            if p1[-1] != '*' or p1[-1] == '*' and x != '*':
                p1.append(x)
        return ''.join(p1)

    @classmethod
    def helper(cls, s, p):
        dp = cls.dp
        if (s, p) in dp:
            return dp[(s, p)]

        if p == s or p == '*':
            dp[(s, p)] = True
        elif p == '' or s == '':
            dp[(s, p)] = False
        elif p[0] == s[0] or p[0] == '?':
            dp[(s, p)] = cls.helper(s[1:], p[1:])
        elif p[0] == '*':
            dp[(s, p)] = cls.helper(s, p[1:]) or cls.helper(s[1:], p)
        else:
            dp[(s, p)] = False

        return dp[(s, p)]

    @classmethod
    def is_match(cls, s: str, p: str) -> bool:
        """动态规划"""
        p = cls.remove_duplicate_stars(p)
        cls.dp = {}
        return cls.helper(s, p)

    # 684ms, 21.7MB
    @classmethod
    def is_match_v2(cls, s: str, p: str) -> bool:
        """动态规划2"""
        s_len = len(s)
        p_len = len(p)

        if p == s or p == '*':
            return True
        if p == '' or s == '':
            return False

        d = [[False] * (s_len + 1) for _ in range(p_len + 1)]
        d[0][0] = True

        for p_idx in range(1, p_len + 1):
            if p[p_idx - 1] == '*':
                s_idx = 1
                while not d[p_idx - 1][s_idx - 1] and s_idx < s_len + 1:
                    s_idx += 1
                d[p_idx][s_idx - 1] = d[p_idx - 1][s_idx - 1]
                while s_idx < s_len + 1:
                    d[p_idx][s_idx] = True
                    s_idx += 1
            elif p[p_idx - 1] == '?':
                for s_idx in range(1, s_len + 1):
                    d[p_idx][s_idx] = d[p_idx - 1][s_idx - 1]
            else:
                for s_idx in range(1, s_len + 1):
                    d[p_idx][s_idx] = \
                        d[p_idx - 1][s_idx - 1] and p[p_idx - 1] == s[s_idx - 1]

        return d[p_len][s_len]

    # 52ms, 13.8MB
    @classmethod
    def is_match_v3(cls, s: str, p: str) -> bool:
        """回溯"""
        s_len, p_len = len(s), len(p)
        s_idx = p_idx = 0
        star_idx = s_tmp_idx = -1

        while s_idx < s_len:
            if p_idx < p_len and p[p_idx] in ['?', s[s_idx]]:
                s_idx += 1
                p_idx += 1
            elif p_idx < p_len and p[p_idx] == '*':
                star_idx = p_idx
                s_tmp_idx = s_idx
                p_idx += 1
            elif star_idx == -1:
                return False
            else:
                p_idx = star_idx + 1
                s_idx = s_tmp_idx + 1
                s_tmp_idx = s_idx

        return all(x == '*' for x in p[p_idx:])

    # 84ms, 13.7MB
    @classmethod
    def is_match_v4(cls, s: str, p: str) -> bool:
        m = len(s)
        n = len(p)

        i = j = 0
        im = jn = -1
        while i < m:
            if j < n and (s[i] == p[j] or p[j] == '?'):
                i += 1
                j += 1
            elif j < n and p[j] == "*":
                # 默认情况，* 不匹配任意字符
                im = i
                j += 1
                jn = j
            elif im > -1:
                # 已经发现一个*
                i = im + 1
                j = jn
                im = i
            else:
                return False

        while j < n and p[j] == "*":
            j += 1

        return j >= n


if __name__ == '__main__':
    test_cases = [
        ('aa', 'a'),
        ('aa', '*'),
        ('cb', '?a'),
        ('adceb', '*a*b'),
        ('acdcb', 'a*c?b')
    ]
    for tc in test_cases:
        print(Solution.is_match(*tc))
        print(Solution.is_match_v2(*tc))
        print(Solution.is_match_v3(*tc))
