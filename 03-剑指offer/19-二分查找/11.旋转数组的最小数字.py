"""
  @Author       : liujianhan
  @Date         : 2020/7/22 下午7:56
  @Project      : leetcode_in_python
  @FileName     : 11.旋转数组的最小数字.py
  @Description  : 把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。输入一个递增排序的数组的一个旋转，输出旋转数组的最小元素。例如，数组 [3,4,5,1,2] 为 [1,2,3,4,5] 的一个旋转，该数组的最小值为1。  

    示例 1：

    输入：[3,4,5,1,2]
    输出：1
    示例 2：

    输入：[2,2,2,0,1]
    输出：0
"""
from typing import List


class Solution:
    # 48ms, 13.9MB
    @staticmethod
    def min_array(numbers: List[int]) -> int:
        start, end = 0, len(numbers) - 1
        if end == 0:
            return numbers[0]

        while start <= end:
            mid = (start + end) >> 1
            if numbers[mid] < numbers[mid - 1]:
                return numbers[mid]
            if numbers[start] > numbers[end]:
                if numbers[mid] >= numbers[start]:
                    start = mid + 1
                else:
                    end = mid - 1
            else:
                end -= 1

        return numbers[end]


if __name__ == '__main__':
    test_cases = [
        [1, 3, 5], [2, 2, 2, 0, 1]
    ]
    for tc in test_cases:
        print(Solution.min_array(tc))