"""
  @Author       : liujianhan
  @Date         : 2020/11/2 9:51
  @Project      : leetcode_in_python
  @FileName     : 605.种花问题.py
  @Description  : 假设你有一个很长的花坛，一部分地块种植了花，另一部分却没有。可是，花卉不能种植在相邻的地块上，它们会争夺水源，两者都会死去。
    给定一个花坛（表示为一个数组包含0和1，其中0表示没种植花，1表示种植了花），和一个数 n 。能否在不打破种植规则的情况下种入 n 朵花？
    能则返回True，不能则返回False。

    示例 1:

    输入: flowerbed = [1,0,0,0,1], n = 1
    输出: True
    示例 2:

    输入: flowerbed = [1,0,0,0,1], n = 2
    输出: False
    注意:

    数组内已种好的花不会违反种植规则。
    输入的数组长度范围为 [1, 20000]。
    n 是非负整数，且不会超过输入数组的大小。
"""
from typing import List


class Solution:
    # 188ms, 13.9MB
    @staticmethod
    def can_place_flowers(flowerbed: List[int], n: int) -> bool:
        available = 0
        index = 2
        size = len(flowerbed)
        if size < 3:
            return n == 0 if 1 in flowerbed else n <= 1
        if flowerbed[:2] == [0, 0]:
            available += 1
        if flowerbed[-2:] == [0, 0]:
            available += 1
        while index < size - 2:
            pre = index - 1
            fol = index + 1
            if flowerbed[index] == 0 and flowerbed[fol] == 0 and flowerbed[pre] == 0:
                available += 1
            index += 2

        return n <= available

    # 188ms, 14MB
    @staticmethod
    def can_place_flowers_v2(flowerbed: List[int], n: int) -> bool:
        flowerbed = [0] + flowerbed + [0]
        for i in range(1, len(flowerbed) - 1):
            if flowerbed[i] == 0 and flowerbed[i - 1] == 0 and flowerbed[i + 1] == 0:
                n -= 1
                flowerbed[i] = 1
        return n <= 0


if __name__ == '__main__':
    test_cases = [
        ([1, 0, 0, 0, 1], 1),
        ([1, 0, 0, 0, 1], 2),
        ([0, 0, 1, 0, 1], 1),
        ([1, 0, 0, 0, 1, 0, 0], 2),
        ([0, 0, 1, 0, 0], 2),
        ([0, 0, 1, 0, 0], 1),
        ([0], 1),
        ([1], 0),
        ([0, 1, 0], 1),
        ([0, 1, 0, 1, 0, 1, 0, 0], 1),
        ([0, 0], 2),
        ([0, 0, 0, 0], 3),
    ]
    for tc in test_cases:
        print(tc, Solution.can_place_flowers(*tc))
        print(tc, Solution.can_place_flowers_v2(*tc))
