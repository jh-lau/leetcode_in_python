"""
  @Author       : liujianhan
  @Date         : 2020/11/10 10:10
  @Project      : leetcode_in_python
  @FileName     : 461.汉明距离.py
  @Description  : 两个整数之间的汉明距离指的是这两个数字对应二进制位不同的位置的数目。
    给出两个整数 x 和 y，计算它们之间的汉明距离。
    注意：
    0 ≤ x, y < 2**31.
    示例:
    输入: x = 1, y = 4
    输出: 2
    解释:
    1   (0 0 0 1)
    4   (0 1 0 0)
           ↑   ↑
    上面的箭头指出了对应二进制位不同的位置。
"""


class Solution:
    # 40ms, 13.5MB
    @staticmethod
    def hamming_distance(x: int, y: int) -> int:
        return bin(x ^ y).count('1')


if __name__ == '__main__':
    test_cases = [
        (1, 4)
    ]
    for tc in test_cases:
        print(Solution.hamming_distance(*tc))
