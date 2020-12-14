"""
  @Author       : liujianhan
  @Date         : 20/12/13 13:13
  @Project      : leetcode_in_python
  @FileName     : 693.交替位二进制数.py
  @Description  : 给定一个正整数，检查它的二进制表示是否总是 0、1 交替出现：换句话说，就是二进制表示中相邻两位的数字永不相同。

    示例 1：
    输入：n = 5
    输出：true
    解释：5 的二进制表示是：101

    示例 2：
    输入：n = 7
    输出：false
    解释：7 的二进制表示是：111.

    示例 3：
    输入：n = 11
    输出：false
    解释：11 的二进制表示是：1011.

    示例 4：
    输入：n = 10
    输出：true
    解释：10 的二进制表示是：1010.

    示例 5：
    输入：n = 3
    输出：false
    提示：

    1 <= n <= 231 - 1
"""


class Solution:
    # 44ms, 14.7MB
    @staticmethod
    def has_alternating_bits(n: int) -> bool:
        return n ^ (n >> 1) == 2 ** (len(bin(n)) - 2) - 1

    # 36ms, 14.5MB
    @staticmethod
    def has_alternating_bits_v2(n: int) -> bool:
        tmp = n ^ (n >> 1)
        return tmp & (tmp + 1) == 0


if __name__ == '__main__':
    test_cases = [
        5, 7, 11, 10, 3, 4
    ]
    for tc in test_cases:
        print(tc, bin(tc), Solution.has_alternating_bits(tc))
