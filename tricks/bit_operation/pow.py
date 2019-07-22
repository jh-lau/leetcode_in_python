"""
  Created by PyCharm.
  User: Liujianhan
  Date: 2019/6/3
  Time: 15:00
 """
__author__ = 'liujianhan'
from data_structure.function_process_time import print_time
from data_structure.function_process_time import RuntimeTest


class Solution:
    @staticmethod
    @print_time
    def pow_test_1(m, n):
        return m ** n

    @staticmethod
    @print_time
    def pow_test_2(m, n):
        target = 1
        while n > 0:
            target *= m
            n -= 1
        return target

    @staticmethod
    @RuntimeTest()
    def pow_test_3(m, n):
        target = 1
        tmp = m
        while n > 0:
            if 1 == n & 1:
                target *= tmp
            n = n >> 1
            tmp *= tmp
        return target

    @staticmethod
    @print_time
    def pow_test_4(m, n):
        target = 1
        tmp = m
        while n > 0:
            if 1 == n & 1:
                target *= tmp
            n = n >> 1
            tmp *= tmp
        return target


Solution.pow_test_1(5, 10)
Solution.pow_test_2(5, 10)
Solution.pow_test_3(5, 10)
Solution.pow_test_4(5, 10)

