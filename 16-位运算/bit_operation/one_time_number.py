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
    def find_n_1(array):
        length = len(array)
        for i in range(length):
            out = array.pop()
            if out not in array:
                return out

    @staticmethod
    @print_time
    def find_n_2(array):
        target = array[0]
        length = len(array)
        for i in range(1, length):
            target = target ^ array[i]
        return target

    @staticmethod
    @print_time
    def find_n_3(array):
        target = array[0]
        array.pop(0)
        for num in array:
            target = target ^ num
        return target


test_1 = [1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1]
test_2 = [1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1]
test_3 = [1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1]
Solution.find_n_1(test_1)
Solution.find_n_2(test_2)
Solution.find_n_3(test_3)
