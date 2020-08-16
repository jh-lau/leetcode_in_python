"""
  @Author       : Liujianhan
  @Date         : 20/5/1 16:52
  @FileName     : 041.缺失的第一个正数(H).py
  @ProjectName  : leetcode_in_python
  @Description  : 给你一个未排序的整数数组，请你找出其中没有出现的最小的正整数。
    示例 1:
    输入: [1,2,0]
    输出: 3
    示例 2:
    输入: [3,4,-1,1]
    输出: 2
    示例 3:
    输入: [7,8,9,11,12]
    输出: 1
    提示：
    你的算法的时间复杂度应为O(n)，并且只能使用常数级别的额外空间。
 """
from typing import List


class Solution:
    # 44ms, 13.7MB
    @classmethod
    def first_missing_positive(cls, nums: List[int]) -> int:
        n = len(nums)

        if 1 not in nums:
            return 1

        if n == 1:
            return 2

        for i in range(n):
            if nums[i] <= 0 or nums[i] > n:
                nums[i] = 1

        # 使用索引和数字符号作为检查器
        # 例如，如果 nums[1] 是负数表示在数组中出现了数字 `1`
        # 如果 nums[2] 是正数 表示数字 2 没有出现
        for i in range(n):
            a = abs(nums[i])
            # 如果发现了一个数字 a - 改变第 a 个元素的符号
            # 注意重复元素只需操作一次
            if a == n:
                nums[0] = -abs(nums[0])
            else:
                nums[a] = -abs(nums[a])

        # 现在第一个正数的下标
        # 就是第一个缺失的数
        for i in range(1, n):
            if nums[i] > 0:
                return i

        if nums[0] > 0:
            return n

        return n + 1

    # 52ms, 13.7MB
    @classmethod
    def first_missing_positive_v2(cls, nums: List[int]) -> int:
        pos, neg = {1}, set()
        for n in nums:
            if n > 0:
                neg.add(n)
                pos.add(n + 1)

        return min(pos - neg)


if __name__ == '__main__':
    test_cases = [
        [1, 2, 0], [3, 4, -1, 1], [7, 8, 9, 11, 12]
    ]
    for tc in test_cases:
        print(tc, Solution.first_missing_positive(tc))
        # print(tc, Solution.first_missing_positive_v2(tc))
