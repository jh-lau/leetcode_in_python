"""
  @Author       : liujianhan
  @Date         : 2020/4/7 下午2:16
  @Project      : leetcode_in_python
  @FileName     : 01.02.判定是否互为字符重排.py
  @Description  : 给定两个字符串 s1 和 s2，请编写一个程序，确定其中一个字符串的字符重新排列后，能否变成另一个字符串。
    
    示例 1：
    
    输入: s1 = "abc", s2 = "bca"
    输出: true 
    示例 2：
    
    输入: s1 = "abc", s2 = "bad"
    输出: false
    说明：
    
    0 <= len(s1) <= 100
    0 <= len(s2) <= 100
"""


class Solution:
    # 44ms, 13.6MB
    @classmethod
    def check_permutation(cls, s1: str, s2: str) -> bool:
        dic_1 = {s: s1.count(s) for s in s1}
        dic_2 = {s: s2.count(s) for s in s2}
        return dic_1 == dic_2


if __name__ == '__main__':
    test_cases = [('abc', 'bca'), ('abc', 'bad')]
    for tc in test_cases:
        print(Solution.check_permutation(*tc))

