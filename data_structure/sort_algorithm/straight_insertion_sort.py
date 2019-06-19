"""
  Created by PyCharm.
  User: Liujianhan
  Date: 2019/5/31
  Time: 7:56
  将记录插入到已经排好序的有序表中
 """
__author__ = 'liujianhan'
from data_structure.function_process_time import RuntimeTest
from data_structure.sort_algorithm.bubble_sort import BubbleSort
from data_structure.sort_algorithm.straight_selection_sort import SelectionSort


class InsertionSort:
    @staticmethod
    @RuntimeTest()
    def insertion_sort(nums_list):
        for i in range(1, len(nums_list)):
            insert_value = nums_list[i]
            j = i - 1
            while j >= 0:
                if nums_list[j] > insert_value:
                    nums_list[j + 1] = nums_list[j]
                else:
                    nums_list[j + 1] = insert_value
                    break
                j -= 1
            nums_list[j + 1] = insert_value
        return nums_list

    @staticmethod
    @RuntimeTest()
    def insertion_sort_1(nums_list):
        length = len(nums_list)
        count_comp, count_move = 0, 0
        for i in range(1, length):
            insert_value = nums_list[i]
            j = i - 1
            while j >= 0:
                count_comp += 1
                if nums_list[j] > insert_value:
                    nums_list[j+1] = nums_list[j]
                else:
                    nums_list[j+1] = insert_value
                    break
                j -= 1
            count_move += 1
            nums_list[j+1] = insert_value
        print(f"总共进行了 {count_comp} 次比较， 进行了 {count_move} 次移动。")
        return nums_list

    @staticmethod
    @RuntimeTest()
    def insertion_sort_2(nums_list):
        for i in range(1, len(nums_list)):
            j = i
            while j > 0 and nums_list[j-1] > nums_list[j]:
                nums_list[j], nums_list[j-1] = nums_list[j-1], nums_list[j]
                j -= 1
        return nums_list


if __name__ == '__main__':

    test = [0, 9, 1, 3, 13, 11, -2, 3120, 441, 9, 132, 90, 1234, 22, -23, -1, 3321]
    test_1 = [0, 9, 1, 3, 13, 11, -2, 3120, 441, 9, 132, 90, 1234, 22, -23, -1, 3321]
    test_2 = [5, 2, 6, 0, 3, 9, 1, 7, 4, 8]
    test_2_1 = [5, 2, 6, 0, 3, 9, 1, 7, 4, 8]
    test_2_1_1 = [5, 2, 6, 0, 3, 9, 1, 7, 4, 8]
    test_3 = [1, 2, 3, 4, 5, 6, 7, 8]
    test_3_1 = [1, 2, 3, 4, 5, 6, 7, 8]
    test_4 = [1, 1, 2, 3, 4, 5, 8, -1, -2, 0, 3, 5, 8]
    test_4_1 = [1, 1, 2, 3, 4, 5, 8, -1, -2, 0, 3, 5, 8]

    SelectionSort.selection_sort(test_2)
    BubbleSort.bubble_sort(test_2_1)
    InsertionSort.insertion_sort(test_2_1_1)
    # InsertionSort.insertion_sort_2(test_2_1_1)




