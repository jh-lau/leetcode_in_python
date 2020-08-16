"""
  Created by PyCharm.
  User: Liujianhan
  Date: 2019/5/31
  Time: 7:56
  o(n*logn)
 """
__author__ = 'liujianhan'
from data_structure.function_process_time import RuntimeTest


class ShellSort:
    @staticmethod
    def shell_insertion_sort(num_list, start_index, increment):
        for inserting_index in range(start_index+increment, len(num_list), increment):
            inserting_value = num_list[inserting_index]
            i = inserting_index - increment
            while i >= start_index:
                if num_list[i] > inserting_value:
                    num_list[i+increment] = num_list[i]
                else:
                    num_list[i+increment] = inserting_value
                    break
                i -= increment
            num_list[i+increment] = inserting_value
        return num_list

    @staticmethod
    @RuntimeTest()
    def shell_sort(num_list):
        increment = len(num_list) // 2
        while increment > 0:
            for start_index in range(0, increment):
                ShellSort.shell_insertion_sort(num_list, start_index, increment)
            increment = increment // 2
        return num_list


if __name__ == '__main__':
    test_case = [54, 26, 93, 17, 77, 31, 44, 55, 20]

    ShellSort.shell_sort(test_case)



