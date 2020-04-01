"""
  Created by PyCharm.
  User: Liujianhan
  Date: 2019//5//27
  Time: 9:32
 """
__author__ = 'liujianhan'
from data_structure.function_process_time import print_time


class Solution:
    @staticmethod
    @print_time
    def is_palindromic_1(number):
        if not isinstance(number, int):
            return 'wrong type of number, must be int'
        number = str(number)
        rev_number = number[::-1]
        if number == rev_number:
            return True
        return False

    @staticmethod
    @print_time
    def is_palindromic_2(number):
        return False if int(number) < 0 else int(number) == int(str(number)[::-1])

    # 以下两种为数学解法
    @staticmethod
    @print_time
    def is_palindromic_3(number):
        number = int(number)
        div = 1
        if number < 0:
            return False
        while number // div >= 10:
            div *= 10
        while number > 0:
            left = number // div
            right = number % 10
            if left != right:
                return False
            number = (number % div) // 10
            div //= 100
        return True

    @staticmethod
    @print_time
    def is_palindromic_4(number):
        """
        把number分为左右两部分，右半部分逐个逆序组成新整数和左半部分比较
        :param number:
        :return:
        """
        number = int(number)
        reverted = 0
        if number < 0 or ((number % 10 == 0) and number != 0):
            return False
        while number > reverted:
            reverted = reverted * 10 + number % 10
            number //= 10
        return number == reverted or number == reverted // 10

    # 还可以通过双向队列简单实现
    @staticmethod
    @print_time
    def is_palindromic(number):
        number = list(str(number))
        while len(number) > 1:
            left = number.pop(0)
            right = number.pop()
            if left != right:
                return False
        return True


test = 123321
test2 = 1234321
test3 = 1234421
test4 = '12344321'
# print(Solution.is_palindromic(test))
# print(Solution.is_palindromic(test2))
# print(Solution.is_palindromic(test3))
# print(Solution.is_palindromic(test4))
Solution.is_palindromic_1(test4)
Solution.is_palindromic_2(test4)
Solution.is_palindromic_3(test4)
Solution.is_palindromic_4(test4)
Solution.is_palindromic(test4)

