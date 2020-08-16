"""
  @Author       : Liujianhan
  @Date         : 20/4/4 15:31
  @FileName     : 172.阶乘后的零.py
  @ProjectName  : leetcode_in_python
  @Description  : 给定一个整数 n，返回 n! 结果尾数中零的数量
    输入: 3
    输出: 0
    解释: 3! = 6, 尾数中没有零。

    输入: 5
    输出: 1
    解释: 5! = 120, 尾数中有 1 个零.
 """


class Solution:
    # 超时， 2391
    @classmethod
    def trailing_zeros(cls, n: int) -> int:
        res = 1
        zeros = 0
        while n > 0:
            res *= n
            n -= 1
        while str(res).endswith('0'):
            zeros += 1
            res //= 10

        return zeros

    # 44ms, 13.7MB
    @classmethod
    def trailing_zeros_v2(cls, n: int) -> int:
        zeros = 0
        while n > 0:
            zeros += n // 5
            n //= 5

        return zeros


if __name__ == '__main__':
    test_cases = [3, 5, 2391]
    for tc in test_cases:
        print(tc, Solution.trailing_zeros(tc))
        print(tc, Solution.trailing_zeros_v2(tc))

