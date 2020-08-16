"""
  @Author       : liujianhan
  @Date         : 2020/7/17 上午10:01
  @Project      : leetcode_in_python
  @FileName     : 290.单词规律.py
  @Description  : 给定一种规律 pattern 和一个字符串 str ，判断 str 是否遵循相同的规律。
    这里的 遵循 指完全匹配，例如， pattern 里的每个字母和字符串 str 中的每个非空单词之间存在着双向连接的对应规律。
    示例1:
    输入: pattern = "abba", str = "dog cat cat dog"
    输出: true
    示例 2:
    输入:pattern = "abba", str = "dog cat cat fish"
    输出: false
    示例 3:
    输入: pattern = "aaaa", str = "dog cat cat dog"
    输出: false
    示例 4:
    输入: pattern = "abba", str = "dog dog dog dog"
    输出: false
    说明:
    你可以假设 pattern 只包含小写字母， str 包含了由单个空格分隔的小写字母。    
"""


class Solution:
    # 32ms, 13.6MB
    @staticmethod
    def word_pattern(pattern: str, str: str) -> bool:
        if len(pattern) != len(str.split()):
            return False
        for l in zip(*set(zip(pattern, str.split()))):
            if len(l) != len(set(l)):
                return False
        return True


if __name__ == '__main__':
    test_cases = [
        ("abba", "dog cat cat dog"),
        ("abba", "dog cat cat fish"),
        ("aaaa", "dog cat cat dog"),
        ("abba", "dog dog dog dog"),
        ("aba", "cat cat cat dog"),
        ("aba", "dog cat cat"),
    ]
    for tc in test_cases:
        print(Solution.word_pattern(*tc))
