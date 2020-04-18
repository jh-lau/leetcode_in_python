"""
  @Author       : liujianhan
  @Date         : 2020/4/18 上午11:17
  @Project      : leetcode_in_python
  @FileName     : 844.比较含退格的字符串.py
  @Description  : 给定 S 和 T 两个字符串，当它们分别被输入到空白的文本编辑器后，判断二者是否相等，并返回结果。 # 代表退格字符。
    注意：如果对空文本输入退格字符，文本继续为空。
    示例 1：
    输入：S = "ab#c", T = "ad#c"
    输出：true
    解释：S 和 T 都会变成 “ac”。
    示例 2：
    输入：S = "ab##", T = "c#d#"
    输出：true
    解释：S 和 T 都会变成 “”。
    示例 3：
    输入：S = "a##c", T = "#a#c"
    输出：true
    解释：S 和 T 都会变成 “c”。
    示例 4：
    输入：S = "a#c", T = "b"
    输出：false
    解释：S 会变成 “c”，但 T 仍然是 “b”。
    提示：
    1 <= S.length <= 200
    1 <= T.length <= 200
    S 和 T 只含有小写字母以及字符 '#'。
"""
import itertools


class Solution:
    # 40ms, 13.4MB
    @classmethod
    def backspace_compare(cls, s: str, t: str) -> bool:
        def build(S):
            ans = []
            for c in S:
                if c != '#':
                    ans.append(c)
                elif ans:
                    ans.pop()
            return "".join(ans)

        return build(s) == build(t)

    # 52ms, 13.8MB
    @classmethod
    def backspace_compare_v2(cls, s: str, t: str) -> bool:
        def F(S):
            skip = 0
            for x in reversed(S):
                if x == '#':
                    skip += 1
                elif skip:
                    skip -= 1
                else:
                    yield x

        return all(x == y for x, y in itertools.zip_longest(F(s), F(t)))


if __name__ == '__main__':
    test_cases = [
        ('ab#c', 'ad#c'),
        ('ab##', 'c#d#'),
        ('a##c', '#a#c'),
        ('a#c', 'b'),
        ('#', '')
    ]
    for tc in test_cases:
        print(Solution.backspace_compare(*tc))
        print(Solution.backspace_compare_v2(*tc))
