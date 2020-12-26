"""
  @Author       : liujianhan
  @Date         : 2020/12/26 9:57
  @Project      : leetcode_in_python
  @FileName     : 744.寻找比目标字母大的最小字母.py
  @Description  : 给你一个排序后的字符列表 letters ，列表中只包含小写英文字母。另给出一个目标字母 target，请你寻找在这一有序列表里比目标字母大的最小字母。
    在比较时，字母是依序循环出现的。举个例子：
    如果目标字母 target = 'z' 并且字符列表为 letters = ['a', 'b']，则答案返回 'a'

    示例：
    输入:
    letters = ["c", "f", "j"]
    target = "a"
    输出: "c"

    输入:
    letters = ["c", "f", "j"]
    target = "c"
    输出: "f"

    输入:
    letters = ["c", "f", "j"]
    target = "d"
    输出: "f"

    输入:
    letters = ["c", "f", "j"]
    target = "g"
    输出: "j"

    输入:
    letters = ["c", "f", "j"]
    target = "j"
    输出: "c"

    输入:
    letters = ["c", "f", "j"]
    target = "k"
    输出: "c"

    提示：
    letters长度范围在[2, 10000]区间内。
    letters 仅由小写字母组成，最少包含两个不同的字母。
    目标字母target 是一个小写字母。
"""
from typing import List
from bisect import bisect


class Solution:
    # 112ms, 15.3MB
    @staticmethod
    def next_greatest_letter(letters: List[str], target: str) -> str:
        index = bisect(letters, target)
        return letters[index % len(letters)]


if __name__ == '__main__':
    test_cases = [
        (["c", "f", "j"], 'a'),
        (["c", "f", "j"], 'c'),
        (["c", "f", "j"], 'd'),
        (["c", "f", "j"], 'g'),
        (["c", "f", "j"], 'j'),
        (["c", "f", "j"], 'k'),
    ]
    for tc in test_cases:
        print(Solution.next_greatest_letter(*tc))
