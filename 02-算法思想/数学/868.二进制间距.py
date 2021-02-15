"""
  @Author       : liujianhan
  @Date         : 21/2/15 11:53
  @Project      : leetcode_in_python
  @FileName     : 868.二进制间距.py
  @Description  : 给定一个正整数 n，找到并返回 n 的二进制表示中两个 相邻 1 之间的 最长距离 。如果不存在两个相邻的 1，返回 0 。
    如果只有 0 将两个 1 分隔开（可能不存在 0 ），则认为这两个 1 彼此 相邻 。两个 1 之间的距离是它们的二进制表示中位置的绝对差。
    例如，"1001" 中的两个 1 的距离为 3 。

    示例 1：
    输入：n = 22
    输出：2
    解释：
    22 的二进制是 "10110" 。
    在 22 的二进制表示中，有三个 1，组成两对相邻的 1 。
    第一对相邻的 1 中，两个 1 之间的距离为 2 。
    第二对相邻的 1 中，两个 1 之间的距离为 1 。
    答案取两个距离之中最大的，也就是 2 。

    示例 2：
    输入：n = 5
    输出：2
    解释：
    5 的二进制是 "101" 。

    示例 3：
    输入：n = 6
    输出：1
    解释：
    6 的二进制是 "110" 。

    示例 4：
    输入：n = 8
    输出：0
    解释：
    8 的二进制是 "1000" 。
    在 8 的二进制表示中没有相邻的两个 1，所以返回 0 。

    示例 5：
    输入：n = 1
    输出：0
     
    提示：
    1 <= N <= 10^9
"""


class Solution:
    # 28ms, 14.9MB
    @staticmethod
    def binary_gap(n: int) -> int:
        binary = bin(n)[2:]
        pos_index = [i for i, b in enumerate(binary) if b == '1']
        length = len(pos_index)
        if length < 2:
            return 0
        return max([pos_index[i+1] - pos_index[i] for i in range(length-1)])


if __name__ == '__main__':
    test_cases = [
        22,
        5,
        6,
        8,
        1
    ]
    for tc in test_cases:
        print(Solution.binary_gap(tc))
