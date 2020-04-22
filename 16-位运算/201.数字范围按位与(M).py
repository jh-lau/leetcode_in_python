"""
  @Author       : liujianhan
  @Date         : 2020/4/22 上午11:20
  @Project      : leetcode_in_python
  @FileName     : 201.数字范围按位与(M).py
  @Description  : 给定范围 [m, n]，其中 0 <= m <= n <= 2147483647，返回此范围内所有数字的按位与（包含 m, n 两端点）。
    示例 1: 

    输入: [5,7]
    输出: 4
    示例 2:

    输入: [0,1]
    输出: 0
"""


class Solution:
    # 120ms, 13.7MB
    @classmethod
    def range_bitwise_and(cls, m: int, n: int) -> int:
        """
        考虑范围[m, n]，如果n比m二进制位数高的话，在累计按位与的过程中，数字的每一个二进制位数必然都出现过0，所以一旦出现位数不同的情况，
        结果必然为0。程序中，m, n在向右移位的过程中，如果m, n相等了，就说明累计按位与的左边肯定等于m, n此时的状态，
        这时候就可以向左移回来了，相当于右边所有位数都补0，相等的部分照旧。如果m, n位数不相等，肯定会移到底，两者都为0时才会相等停止循环，
        这时候再向左移多少结果都是0。
        """
        t = 0
        while m != n:
            m >>= 1
            n >>= 1
            t += 1

        return n << t


if __name__ == '__main__':
    test_cases = [
        [5, 7], [0, 1]
    ]
    for tc in test_cases:
        print(Solution.range_bitwise_and(*tc))
