"""
  Created by PyCharm.
  User: Liujianhan
  Date: 2019/6/3
  Time: 14:35
 """
from data_structure.function_process_time import print_time

__author__ = 'liujianhan'


class Solution:
    """
    求不大于N的最大2的幂指数
    """
    @staticmethod
    @print_time
    def find_n_1(n):
        n |= n >> 1
        n |= n >> 2
        n |= n >> 4
        n |= n >> 8
        return (n + 1) >> 1

    @staticmethod
    @print_time
    def find_n_2(n):
        target = 1
        while 1:
            if 2 * target > n:
                return target
            target *= 2


Solution.find_n_1(634545678451564589787953122423423535)
Solution.find_n_2(634545678451564589787953122423423535)

