"""
  @Author       : liujianhan
  @Date         : 2020/6/24 下午5:41
  @Project      : leetcode_in_python
  @FileName     : 219.存在重复元素II.py
  @Description  : 给定一个整数数组和一个整数 k，判断数组中是否存在两个不同的索引 i 和 j，使得 nums [i] = nums [j]，并且 i 和 j 的差的 绝对值 至多为 k。
    示例 1:
    输入: nums = [1,2,3,1], k = 3
    输出: true
    示例 2:
    输入: nums = [1,0,1,1], k = 1
    输出: true
    示例 3:
    输入: nums = [1,2,3,1,2,3], k = 2
    输出: false
"""
from typing import List


class Solution:
    # 56ms, 21.5MB
    @classmethod
    def contains_nearby_duplicate(cls, nums: List[int], k: int) -> bool:
        dic = {}
        # 遍历nums
        for i in range(len(nums)):
            # 如果有相同元素，匹配成功
            if nums[i] in dic:
                # 判断索引差
                # 小于k符合条件
                if i - dic[nums[i]] <= k:
                    return True
                # 不小于k则将索引更新为更接近未来匹配的那一个
                else:
                    dic[nums[i]] = i
            else:
                dic[nums[i]] = i

        return False


if __name__ == '__main__':
    test_cases = [
        ([1, 2, 3, 1], 3),
        ([1, 0, 1, 1], 1),
        ([1, 2, 3, 1, 2, 3], 2),
    ]
    for tc in test_cases:
        print(Solution.contains_nearby_duplicate(*tc))

