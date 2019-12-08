"""
  Created by PyCharm.
  User: Liujianhan
  Date: 2019/5/31
  Time: 7:56
  快速排序首先选择一个值，该值称为基准数。基准数通常使用列表中的第一项。基准数的作用是帮助拆分列表。基准数在一轮遍历后将直接放到最终的位置。
  左标记从左侧开始遍历列表，直到我们找到一个大于基准数的项。
  右标记从右侧开始遍历列表，直到我们找到一个小于基准数的项。
  交换这两个项，随后左右标记继续遍历列表。不断重复这个过程。直到在右标记变得小于左标记的时刻，我们停止。
  此时，右标记所在的项一定小于基准值，因为这是左标记走过的位置；左标记所在的项一定大于基准值，因为这是右标记走过的项。
  右标记所在的项与列表第一项即基准数相交换。此时原数列就别分成了左侧都小于基准数，右侧都大于基准数的两个子序列。进而可以继续对这两个子序列排序。
 """
__author__ = 'liujianhan'


class QuickSort:
    @staticmethod
    def quick_sort(num_list):
        if len(num_list) < 2:
            return num_list
        base_value = num_list[0]
        left_index = 1
        right_index = len(num_list) - 1

        while True:
            while left_index <= right_index:
                if num_list[left_index] <= base_value:
                    left_index += 1
                elif num_list[right_index] >= base_value:
                    right_index -= 1
                else:
                    break

            if left_index <= right_index:
                num_list[left_index], num_list[right_index] = num_list[right_index], num_list[left_index]
                left_index += 1
                right_index -= 1
            else:
                break

        num_list[0] = num_list[right_index]
        num_list[right_index] = base_value

        left_list = num_list[:right_index]
        right_list = num_list[right_index + 1:]

        return QuickSort.quick_sort(left_list) + [num_list[right_index]] + QuickSort.quick_sort(right_list)

    @staticmethod
    def quick_sort_3partition(sorting, left, right):
        if right <= left:
            return
        a = i = left
        b = right
        pivot = sorting[left]
        while i <= b:
            if sorting[i] < pivot:
                sorting[a], sorting[i] = sorting[i], sorting[a]
                a += 1
                i += 1
            elif sorting[i] > pivot:
                sorting[b], sorting[i] = sorting[i], sorting[b]
                b -= 1
            else:
                i += 1
        QuickSort.quick_sort_3partition(sorting, left, a - 1)
        QuickSort.quick_sort_3partition(sorting, b + 1, right)

    @staticmethod
    def quick_sort_more_space(array):
        if len(array) < 2:
            return array
        else:
            pivot = array[0]
            lesser = [i for i in array[1:] if i < pivot]
            greater = [i for i in array[1:] if i > pivot]
            return QuickSort.quick_sort_more_space(lesser) + pivot + QuickSort.quick_sort_more_space(greater)


if __name__ == '__main__':
    test = [0, 9, 1, 3, 13, 11, -2, 3120, 441, 9, 132, 90, 1234, 22, -23, -1, 3321]
    test_case = [321, 54, 26, 93, 17, 77, 31, 44, 55, 20]
    test_1 = [1, 0, 3, 4, 5, 9]

    print(QuickSort.quick_sort(test_case))
    print(QuickSort.quick_sort(test))
    assert QuickSort.quick_sort(test_1) == [0, 1, 3, 4, 5, 9]
    # print(quick_sort(test_case))
