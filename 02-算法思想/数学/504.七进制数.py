"""
  @Author       : liujianhan
  @Date         : 2020/8/24 10:57
  @Project      : leetcode_in_python
  @FileName     : 504.七进制数.py
  @Description  : 给定一个整数，将其转化为7进制，并以字符串形式输出。

    示例 1:

    输入: 100
    输出: "202"
    示例 2:

    输入: -7
    输出: "-10"
    注意: 输入范围是 [-1e7, 1e7] 。
"""


class Solution:
    # 40ms, 13.8MB
    @staticmethod
    def convert_to_base7(num: int) -> str:
        _num = abs(num)
        base7 = []
        if num < 0:
            flag = 1
            num = -num
        else:
            flag = 0
        while num >= 7:
            fig = str(num % 7)
            base7.append(fig)
            num = num // 7
        base7.append(str(num))
        if flag:
            base7.append('-')
        base7.reverse()
        return ''.join(base7)


if __name__ == '__main__':
    test_cases = [
        100, -7
    ]
    for tc in test_cases:
        print(Solution.convert_to_base7(tc))
