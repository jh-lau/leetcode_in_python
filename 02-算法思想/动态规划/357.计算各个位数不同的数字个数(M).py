"""
  @Author       : liujianhan
  @Date         : 2020/8/14 下午8:01
  @Project      : leetcode_in_python
  @FileName     : 357.计算各个位数不同的数字个数(M).py
  @Description  : 给定一个非负整数 n，计算各位数字都不同的数字 x 的个数，其中 0 ≤ x < 10n 。

    示例:

    输入: 2
    输出: 91
    解释: 答案应为除去 11,22,33,44,55,66,77,88,99 外，在 [0,100) 区间内的所有数字。
"""


class Solution:
    # 40ms, 113.6MB
    @staticmethod
    def count_numbers_with_unique_digits(n: int) -> int:
        counts = [9, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        res, product = 1, 1

        # 超过10位的, 均会重复
        n = n if n <= 10 else 10
        for i in range(n):
            product *= counts[i]
            res += product

        return res


if __name__ == '__main__':
    print(Solution.count_numbers_with_unique_digits(2))
