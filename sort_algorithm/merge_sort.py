"""
  Created by PyCharm.
  User: Liujianhan
  Date: 2019/5/31
  Time: 7:56
 """
__author__ = 'liujianhan'


class MergeSort:
    @staticmethod
    def merge_sort(num_list):
        if len(num_list) < 2: return num_list
        mid_index = len(num_list) // 2
        left_list = num_list[:mid_index]
        right_list = num_list[mid_index:]
        left_list = MergeSort.merge_sort(left_list)
        right_list = MergeSort.merge_sort(right_list)

        left_index = 0
        right_index = 0
        all_index = 0

        while left_index < len(left_list) and right_index < len(right_list):
            # 两个字列表都未遍历完
            if left_list[left_index] < right_list[right_index]:
                num_list[all_index] = left_list[left_index]
                left_index += 1
            else:
                num_list[all_index] = right_list[right_index]
                right_index += 1
            all_index += 1

        while left_index < len(left_list):
            # 左列表未遍历完
            num_list[all_index] = left_list[left_index]
            left_index += 1
            all_index += 1

        while right_index < len(right_list):
            # 右列表未遍历完
            num_list[all_index] = right_list[right_index]
            right_index += 1
            all_index += 1
        return num_list


if __name__ == '__main__':
    test = [0, 9, 1, 3, 13, 11, -2, 3120, 441, 9, 132, 90, 1234, 22, -23, -1, 3321]
    test_case = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    test_1 = [1, 0, 3, 4, 5, 9]

    # print(MergeSort.merge_sort(test_1))
    print(MergeSort.merge_sort(test_case))
    # print(MergeSort.merge_sort(test))
