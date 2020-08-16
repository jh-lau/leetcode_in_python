"""
  @Author       : liujianhan
  @Date         : 2020/4/2 下午7:01
  @Project      : leetcode_in_python
  @FileName     : 168.Excel表列名称.py
  @Description  : 给定一个正整数，返回它在 Excel 表中相对应的列名称。
  输入: 1
    输出: "A"
    输入: 28
    输出: "AB"
    输入: 701
    输出: "ZY"
"""


class Solution:
    # 44ms, 13.6MB
    @classmethod
    def convert_to_title(cls, n: int) -> str:
        table = [chr(k) for k in range(65, 91)]
        if n <= 26:
            return table[n - 1]

        return cls.convert_to_title((n - 1) // 26) + table[(n - 1) % 26]

    # 40ms, 13.7MB
    @classmethod
    def convert_to_title_v2(cls, n: int) -> str:
        first, second = n // 26, n % 26
        map_dict = {k - 64: chr(k) for k in range(65, 91)}
        map_dict.update({0: ''})
        if not second:
            return map_dict[first-1] + 'Z'
        while first > 26:
            return cls.convert_to_title_v2(first) + map_dict[second]
        return map_dict[first] + map_dict[second]


if __name__ == '__main__':
    test_cases = [1, 26, 28, 52, 701, 703]
    for tc in test_cases:
        print(tc, Solution.convert_to_title(tc))
        print(tc, Solution.convert_to_title_v2(tc))
        print()
