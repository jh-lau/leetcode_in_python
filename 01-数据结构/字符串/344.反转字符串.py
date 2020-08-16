"""
  Created by PyCharm.
  User: Liujianhan
  Date: 2019/5/28
  Time: 5:51
 """
__author__ = 'liujianhan'


class Solution:
    @staticmethod
    def reverse_string(strings):
        """
        Do not return anything, modify strings in-place instead.
        :param strings: list
        :return: None
        """
        i, j = 0, len(strings) - 1
        while i < j:
            strings[i], strings[j] = strings[j], strings[i]
            i += 1
            j -= 1


test = ['h', 'e', 'l', 'l', 'o']
Solution.reverse_string(test)
print(test)
