"""
  @Author       : liujianhan
  @Date         : 2020/11/11 11:17
  @Project      : leetcode_in_python
  @FileName     : 412.Fizz Buzz.py
  @Description  : 写一个程序，输出从 1 到 n 数字的字符串表示。
    1. 如果 n 是3的倍数，输出“Fizz”；
    2. 如果 n 是5的倍数，输出“Buzz”；
    3.如果 n 同时是3和5的倍数，输出 “FizzBuzz”。
    示例：

    n = 15,

    返回:
    [
        "1",
        "2",
        "Fizz",
        "4",
        "Buzz",
        "Fizz",
        "7",
        "8",
        "Fizz",
        "Buzz",
        "11",
        "Fizz",
        "13",
        "14",
        "FizzBuzz"
    ]
"""
from typing import List


class Solution:
    # 56ms, 14.4MB
    @staticmethod
    def fizz_buzz(n: int) -> List[str]:
        result = []
        for num in range(1, n+1):
            if not num % 3:
                if not num % 5:
                    result.append('FizzBuzz')
                else:
                    result.append('Fizz')
            elif not num % 5:
                result.append('Buzz')
            else:
                result.append(str(num))

        return result


if __name__ == '__main__':
    test_cases = [
        15, 1
    ]
    for tc in test_cases:
        print(Solution.fizz_buzz(tc))
