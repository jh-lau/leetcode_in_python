"""
  Created by PyCharm.
  User: Liujianhan
  Date: 2019/6/11
  Time: 19:25
 """
__author__ = 'liujianhan'
import random


class CountingSort:
    @staticmethod
    def _max(num_list):
        largest = num_list[0]
        for num in num_list:
            if num > largest:
                largest = num
        return largest

    @staticmethod
    def _min(num_list):
        smallest = num_list[0]
        for num in num_list:
            if num < smallest:
                smallest = num
        return smallest

    @staticmethod
    def counting_sort(num_list):
        length = len(num_list)
        b = [0] * length
        c = [0] * (length+1)
        for number in num_list:
            c[number] += 1
        for number in range(1, length+1):
            c[number] = c[number-1] + c[number]
        for number in num_list:
            b[c[number]-1] = number
            c[number] -= 1
        return b


if __name__ == '__main__':
    test_1 = [random.randint(0, 20) for i in range(10)]
    print(test_1)
    assert CountingSort.counting_sort(test_1) == sorted(test_1)
