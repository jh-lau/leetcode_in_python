"""
  @Author       : liujianhan
  @Date         : 2020/1/23 下午2:28
  @Project      : leetcode_in_python
  @FileName     : 067.二进制求和.py
  @Description  : 给定两个二进制字符串，返回他们的和（用二进制表示）。输入为非空字符串且只包含数字 1 和 0。
"""


class Solution:
    # 32ms, 13MB
    @staticmethod
    def add_binary(a: str, b: str) -> str:
        return bin(eval(f'0b{a}') + eval(f'0b{b}'))[2:]


if __name__ == '__main__':
    a, b = '11', '1'
    c, d = '1010', '1011'
    print(Solution().add_binary(a, b))
    print(Solution().add_binary(c, d))