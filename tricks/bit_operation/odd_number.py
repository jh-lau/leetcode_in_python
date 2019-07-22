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
    def odd_number_1(n):
        return True if n % 2 == 1 else False

    @staticmethod
    @print_time
    def odd_number_2(n):
        return True if 1 == (n & 1) else False


Solution.odd_number_1(193029103901)
Solution.odd_number_2(193029103901)

