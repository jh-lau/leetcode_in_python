"""
  Created by PyCharm.
  User: Liujianhan
  Date: 2019/5/31
  Time: 7:56
 """
__author__ = 'liujianhan'
from data_structure.function_process_time import RuntimeTest
from sort_algorithm.bubble_sort import BubbleSort


class SelectionSort:
    @staticmethod
    @RuntimeTest()
    def selection_sort(nums_list):
        for i in range(len(nums_list) - 1):
            low_index = i
            for j in range(i+1, len(nums_list)):
                if nums_list[j] < nums_list[low_index]:
                    low_index = j
            if low_index != i:
                nums_list[low_index], nums_list[i] = nums_list[i], nums_list[low_index]
        return nums_list

    @staticmethod
    @RuntimeTest()
    def selection_sort_1(nums_list):
        count_comp, count_move = 0, 0
        length = len(nums_list)
        for i in range(length - 1):
            low_index = i
            for j in range(i+1, length):
                # 每一趟找出最小值
                count_comp += 1
                if nums_list[j] < nums_list[low_index]:
                    low_index = j

            if low_index != i:
                count_move += 1
                nums_list[low_index], nums_list[i] = nums_list[i], nums_list[low_index]
        print(f"总共进行了 {count_comp} 次比较， 进行了 {count_move} 次移动。")
        return nums_list


if __name__ == '__main__':

    test = [0, 9, 1, 3, 13, 11, -2, 3120, 441, 9, 132, 90, 1234, 22, -23, -1, 3321]
    test_1 = [0, 9, 1, 3, 13, 11, -2, 3120, 441, 9, 132, 90, 1234, 22, -23, -1, 3321]
    test_2 = [5, 2, 6, 0, 3, 9, 1, 7, 4, 8]
    test_2_1 = [5, 2, 6, 0, 3, 9, 1, 7, 4, 8]
    test_3 = [1, 2, 3, 4, 5, 6, 7, 8]
    test_3_1 = [1, 2, 3, 4, 5, 6, 7, 8]
    test_4 = [1, 1, 2, 3, 4, 5, 8, -1, -2, 0, 3, 5, 8]
    test_4_1 = [1, 1, 2, 3, 4, 5, 8, -1, -2, 0, 3, 5, 8]

    SelectionSort.selection_sort(test_2)
    BubbleSort.bubble_sort(test_2_1)

    SelectionSort.selection_sort(test)
    BubbleSort.bubble_sort(test_1)

    SelectionSort.selection_sort(test_4)
    BubbleSort.bubble_sort(test_4_1)
