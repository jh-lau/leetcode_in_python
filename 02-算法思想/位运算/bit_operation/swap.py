"""
  Created by PyCharm.
  User: Liujianhan
  Date: 2019/6/3
  Time: 15:00
 """
__author__ = 'liujianhan'
from data_structure.function_process_time import print_time


class Solution:
    @staticmethod
    @print_time
    def switch_1(x, y):
        tmp = x
        x = y
        y = tmp
        return x, y

    @staticmethod
    @print_time
    def switch_2(x, y):
        x = x ^ y
        y = x ^ y
        x = x ^ y
        return x, y


if __name__ == '__main__':
    Solution.switch_1(23123123, 3)  # 0.0183ms
    Solution.switch_2(23123123, 3)  # 0.00933ms
