"""
  @Author       : liujianhan
  @Date         : 2020/4/7 下午2:12
  @Project      : leetcode_in_python
  @FileName     : 01.01.判定字符是否唯一.py
  @Description  : 实现一个算法，确定一个字符串 s 的所有字符是否全都不同。

    示例 1：

    输入: s = "leetcode"
    输出: false
    示例 2：

    输入: s = "abc"
    输出: true
    限制：

    0 <= len(s) <= 100
    如果你不使用额外的数据结构，会很加分。
"""


class Solution:
    # 24ms, 13.7MB
    @classmethod
    def is_unique(cls, astr: str) -> bool:
        return len(astr) == len(set(astr))


if __name__ == '__main__':
    test_cases = ['leetcode', 'abc']
    for tc in test_cases:
        print(Solution.is_unique(tc))
