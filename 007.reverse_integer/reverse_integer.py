"""
  User: Liujianhan
  Time: 13:30
 """
__author__ = 'liujianhan'


class Solution:
    @staticmethod
    def reverse(x: int) -> int:
        range_ = range(-2 ** 31, 2 ** 31)
        temp, flag = 0, 0
        if x not in range_: return 0
        x_ = -x if x < 0 else x
        while x_:
            digit = x_ % 10
            if digit or flag:
                flag = 1
                temp = temp * 10 + digit
            x_ = x_ // 10
        overflow = 0 if temp in range_ else 1
        if overflow:
            return 0
        return temp if x > 0 else -temp
