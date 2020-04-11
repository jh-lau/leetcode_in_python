"""
  @Author       : liujianhan
  @Date         : 2020/4/9 上午10:49
  @Project      : leetcode_in_python
  @FileName     : 859.亲密字符串.py
  @Description  : 给定两个由小写字母构成的字符串 A 和 B ，只要我们可以通过交换 A 中的两个字母得到与 B 相等的结果，就返回 true ；否则返回 false 。
    示例 1：
    输入： A = "ab", B = "ba"
    输出： true

    示例 2：
    输入： A = "ab", B = "ab"
    输出： false

    示例 3:
    输入： A = "aa", B = "aa"
    输出： true

    示例 4：
    输入： A = "aaaaaaabc", B = "aaaaaaacb"
    输出： true

    示例 5：
    输入： A = "", B = "aa"
    输出： false

    示例 6：
    输入： A = "abab", B = "abab"
    输出： true
     
    提示：
    0 <= A.length <= 20000
    0 <= B.length <= 20000
    A 和 B 仅由小写字母构成。
"""


class Solution:
    # 36ms, 13.8MB
    @classmethod
    def buddy_strings(cls, a: str, b: str) -> bool:
        if len(a) != len(b):
            return False
        if a == b:
            seen = set()
            for i in a:
                if i in seen:
                    return True
                seen.add(i)
            return False

        pairs = []
        for i, j in zip(a, b):
            if i != j:
                pairs.append((i, j))
            if len(pairs) > 3:
                return False

        return len(pairs) == 2 and pairs[0] == pairs[1][::-1]


if __name__ == '__main__':
    test_cases = [('ab', 'ba'),
                  ('ab', 'ab'),
                  ('aa', 'aa'),
                  ('abab', 'abab'),
                  ('aaaaaaabc', 'aaaaaaacb'),
                  ('', 'aa')]
    for tc in test_cases:
        print(tc, Solution.buddy_strings(*tc))
