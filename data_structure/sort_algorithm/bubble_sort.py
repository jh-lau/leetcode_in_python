"""
  Created by PyCharm.
  User: Liujianhan
  Date: 2019/5/31
  Time: 7:56
 """
__author__ = 'liujianhan'
from data_structure.function_process_time import RuntimeTest


class BubbleSort:
    @staticmethod
    @RuntimeTest()
    def bubble_sort(num_list):
        epochs = len(num_list) - 1
        for epoch in range(epochs):
            exchanged = False
            for i in range(len(num_list) - 1 - epoch):
                if num_list[i] > num_list[i+1]:
                    num_list[i], num_list[i+1] = num_list[i+1], num_list[i]
                    exchanged = True
            if not exchanged:
                return num_list

    @staticmethod
    @RuntimeTest()
    def bubble_sort_1(nums):
        length = len(nums) - 1
        count_comp, count_move = 0, 0
        for i in range(length):
            swapped = False
            for j in range(length - 1, i - 1, -1):
                # 将小的数往左边冒泡
                count_comp += 1
                if nums[j] > nums[j+1]:
                    count_move += 1
                    nums[j+1], nums[j] = nums[j], nums[j+1]
                    # swapped没改变说明已经排好，无需继续遍历
                    swapped = True
            if not swapped:
                break
        print(f"总共进行了 {count_comp} 次比较， 进行了 {count_move} 次移动。")
        return nums

    @staticmethod
    @RuntimeTest()
    def sort_2(num_list):
        epochs = len(num_list) - 1
        count_comp, count_move = 0, 0
        for epoch in range(epochs):
            exchanged = False
            for i in range(len(num_list) - 1 - epoch):
                # 将大的数往右边冒泡
                # for i in range(epoch, len(num_list) - 1):
                # 注意这种写法错误的原因与正确写法的对比：区别在于正确的写法排除了最大值，错误写法
                # 排除了最早比较的值，不一定是最大或最小值
                count_comp += 1
                if num_list[i] > num_list[i+1]:
                    count_move += 1
                    temp = num_list[i]
                    num_list[i] = num_list[i + 1]
                    num_list[i + 1] = temp
                    exchanged = True
            if not exchanged:
                print(f"总共进行了 {count_comp} 次比较， 进行了 {count_move} 次移动。")
                return num_list


if __name__ == '__main__':
    test = [0, 9, 1, 3, 13, 11, -2, 3120, 441, 9, 132, 90, 1234, 22, -23, -1, 3321]
    test_1 = [0, 9, 1, 3, 13, 11, -2, 3120, 441, 9, 132, 90, 1234, 22, -23, -1, 3321]
    test_2 = [5, 2, 6, 0, 3, 9, 1, 7, 4, 8]
    test_2_1 = [5, 2, 6, 0, 3, 9, 1, 7, 4, 8]
    test_3 = [1, 2, 3, 4, 5, 6, 7, 8]
    test_3_1 = [1, 2, 3, 4, 5, 6, 7, 8]
    test_4 = [1, 1, 2, 3, 4, 5, 8, -1, -2, 0, 3, 5, 8]

    BubbleSort.bubble_sort([0, 5, 3, 1, 2])
    # BubbleSort.sort_2(test_1)
    # BubbleSort.bubble_sort(test_2)
    # BubbleSort.sort_2(test_2_1)
    # # BubbleSort.sort(test_3)
    # # BubbleSort.sort_2(test_3_1)
    # BubbleSort.bubble_sort(test_4)
