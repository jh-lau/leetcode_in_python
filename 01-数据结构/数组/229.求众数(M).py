"""
  @Author       : liujianhan
  @Date         : 2020/7/3 下午8:01
  @Project      : leetcode_in_python
  @FileName     : 229.求众数(M).py
  @Description  : 给定一个大小为 n 的数组，找出其中所有出现超过 ⌊ n/3 ⌋ 次的元素。
    说明: 要求算法的时间复杂度为 O(n)，空间复杂度为 O(1)。
    示例 1:
    输入: [3,2,3]
    输出: [3]
    示例 2:
    输入: [1,1,1,3,3,2,2,2]
    输出: [1,2]
"""
from typing import List


class Solution:
    #
    @staticmethod
    def majority_element(nums: List[int]) -> List[int]:
        res = []  # 返回数组
        majorityO = -1  # 候选人1
        majorityT = -1  # 候选人2
        countO = 0  # 候选人1 票数
        countT = 0  # 候选人2 票数
        for num in nums:
            if countO == 0 and num != majorityT:
                majorityO = num
                countO += 1
                continue
            elif countT == 0 and num != majorityO:
                majorityT = num
                countT += 1
                continue
            else:
                if majorityO == num:
                    countO += 1
                elif majorityT == num:
                    countT += 1
                else:
                    countO -= 1
                    countT -= 1
        counterO = 0
        counterT = 0

        if countO > 0:
            for num in nums:
                if num == majorityO:
                    counterO += 1
        if counterO > len(nums) // 3:
            res.append(majorityO)
        if countT > 0:
            for num in nums:
                if num == majorityT:
                    counterT += 1
        if counterT > len(nums) // 3:
            res.append(majorityT)

        return res


if __name__ == '__main__':
    test_cases = [
        [3, 2, 3],
        [1, 1, 1, 3, 3, 2, 2, 2]
    ]
    for tc in test_cases:
        print(Solution.majority_element(tc))
