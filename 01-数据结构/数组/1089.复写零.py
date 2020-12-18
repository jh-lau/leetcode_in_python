"""
  @Author       : liujianhan
  @Date         : 2020/12/18 10:16
  @Project      : leetcode_in_python
  @FileName     : 1089.复写零.py
  @Description  : 给你一个长度固定的整数数组 arr，请你将该数组中出现的每个零都复写一遍，并将其余的元素向右平移。
    注意：请不要在超过该数组长度的位置写入元素。
    要求：请对输入的数组 就地 进行上述修改，不要从函数返回任何东西。

    示例 1：
    输入：[1,0,2,3,0,4,5,0]
    输出：null
    解释：调用函数后，输入的数组将被修改为：[1,0,0,2,3,0,0,4]

    示例 2：
    输入：[1,2,3]
    输出：null
    解释：调用函数后，输入的数组将被修改为：[1,2,3]

    提示：

    1 <= arr.length <= 10000
    0 <= arr[i] <= 9
"""
from typing import List


class Solution:
    # 44ms, 14.8MB
    @staticmethod
    def duplicate_zeros(arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        i = 0
        while i < len(arr):
            if arr[i] == 0:
                arr.insert(i, 0)
                arr.pop()
                i += 2
            else:
                i += 1


if __name__ == '__main__':
    test_cases = [
        [1, 0, 2, 3, 0, 4, 5, 0],
        [1, 2, 3]
    ]
    for tc in test_cases:
        print(tc)
        Solution.duplicate_zeros(tc)
        print(tc)
