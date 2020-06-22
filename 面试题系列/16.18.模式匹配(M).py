"""
  @Author       : liujianhan
  @Date         : 2020/6/22 下午7:45
  @Project      : leetcode_in_python
  @FileName     : 16.18.模式匹配(M).py
  @Description  : 你有两个字符串，即pattern和value。 pattern字符串由字母"a"和"b"组成，用于描述字符串中的模式。例如，字符串"catcatgocatgo"匹配模式"aabab"（其中"cat"是"a"，"go"是"b"），该字符串也匹配像"a"、"ab"和"b"这样的模式。但需注意"a"和"b"不能同时表示相同的字符串。编写一个方法判断value字符串是否匹配pattern字符串。
    示例 1：
    输入： pattern = "abba", value = "dogcatcatdog"
    输出： true
    示例 2：
    输入： pattern = "abba", value = "dogcatcatfish"
    输出： false
    示例 3：
    输入： pattern = "aaaa", value = "dogcatcatdog"
    输出： false
    示例 4：
    输入： pattern = "abba", value = "dogdogdogdog"
    输出： true
    解释： "a"="dogdog",b=""，反之也符合规则
    提示：
    0 <= len(pattern) <= 1000
    0 <= len(value) <= 1000
    你可以假设pattern只包含字母"a"和"b"，value仅包含小写字母。
"""


class Solution:
    # 36ms, 13.8MB
    @classmethod
    def pattern_matching(cls, pattern: str, value: str) -> bool:
        if not pattern:
            return not value
        n = len(value)
        a_cnt, b_cnt = pattern.count('a'), pattern.count('b')
        a_max_l = 0 if a_cnt == 0 else n // a_cnt
        for a_l in range(a_max_l + 1):
            if not b_cnt:
                if n != a_l * a_cnt:
                    continue
                b_l = 0
            else:
                b_total_l = n - a_cnt * a_l
                if b_total_l % b_cnt != 0:
                    continue
                b_l = b_total_l // b_cnt
            a, b = None, None
            i = 0
            for p in pattern:
                if p == 'a':
                    s = value[i:(i + a_l)]
                    i += a_l
                    if a is not None and a != s:
                        break
                    a = s
                else:
                    s = value[i:(i + b_l)]
                    i += b_l
                    if b is not None and b != s:
                        break
                    b = s
            else:
                if a != b:
                    return True
        return False


if __name__ == '__main__':
    test_cases = [
        ('abba', 'dogcatcatdog'),
        ('abba', 'dogcatcatfish'),
        ('aaaa', 'dogcatcatdog'),
        ('abba', 'dogdogdogdog')
    ]
    for tc in test_cases:
        print(Solution.pattern_matching(*tc))
