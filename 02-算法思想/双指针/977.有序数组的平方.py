"""
  @Author       : liujianhan
  @Date         : 2020/10/16 10:15
  @Project      : leetcode_in_python
  @FileName     : 977.有序数组的平方.py
  @Description  : 给定一个按非递减顺序排序的整数数组 A，返回每个数字的平方组成的新数组，要求也按非递减顺序排序。
    示例 1：
    输入：[-4,-1,0,3,10]
    输出：[0,1,9,16,100]

    示例 2：
    输入：[-7,-3,2,3,11]
    输出：[4,9,9,49,121]

    提示：
    1 <= A.length <= 10000
    -10000 <= A[i] <= 10000
    A 已按非递减顺序排序。
"""
from typing import List


class Solution:
    # 240ms, 15.6MB
    @staticmethod
    def sorted_squares(int_list: List[int]) -> List[int]:
        return sorted(list(map(lambda x: x ** 2, int_list)))

    # 296ms, 15.6MB
    @staticmethod
    def sorted_squares_v2(int_list: List[int]) -> List[int]:
        """双指针"""
        size = len(int_list)
        ans = [0] * size

        i, j, pos = 0, size-1, size-1
        while i <= j:
            if int_list[i] ** 2 > int_list[j] ** 2:
                ans[pos] = int_list[i] ** 2
                i += 1
            else:
                ans[pos] = int_list[j] ** 2
                j -= 1
            pos -= 1

        return ans


if __name__ == '__main__':
    test_cases = [
        [-4, -1, 0, 3, 10],
        [-7, -3, 2, 3, 11]
    ]
    for tc in test_cases:
        print(Solution.sorted_squares(tc))
        print(Solution.sorted_squares_v2(tc))
