"""
  @Author       : liujianhan
  @Date         : 2020/3/19 上午10:01
  @Project      : leetcode_in_python
  @FileName     : 69.x的平方根.py
  @Description  : 实现 int sqrt(int x) 函数。
    计算并返回 x 的平方根，其中 x 是非负整数。
    由于返回类型是整数，结果只保留整数的部分，小数部分将被舍去。
"""


class Solution:
    # 52ms, 13.6MB --> 38.42%, 5.18%
    @classmethod
    def my_sqrt(cls, x: int) -> int:
        left, right = 0, x // 2 + 1
        while left <= right:
            mid = left + ((right - left) >> 1)
            tmp = mid ** 2
            if tmp == x:
                return mid
            elif tmp < x:
                left = mid + 1
            else:
                right = mid - 1
        return right

    # 44ms, 13.6MB
    @classmethod
    def my_sqrt_newton(cls, x: int) -> int:
        root = x
        while root ** 2 > x:
            root = (root + x // root) >> 1
        return root


if __name__ == '__main__':
    for x in range(10):
        print('binary:', x, Solution.my_sqrt(x))
        print('newton:', x, Solution.my_sqrt_newton(x))
