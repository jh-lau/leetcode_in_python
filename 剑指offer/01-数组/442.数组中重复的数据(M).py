"""
  User: Liujianhan
  Time: 21:10
  给定一个整数数组 a，其中1 ≤ a[i] ≤ n （n为数组长度）, 其中有些元素出现两次而其他元素出现一次。
  找到所有出现两次的元素。
  你可以不用到任何额外空间并在O(n)时间复杂度内解决这个问题吗？
  输入:
    [4,3,2,7,8,2,3,1]

  输出:
    [2,3]
 """
__author__ = 'liujianhan'

from typing import List


class Solution:
    result = []

    # 440ms, 21.2MB
    @classmethod
    def find_duplicates(cls, nums: List[int]) -> List[int]:
        for n in nums:
            if nums[abs(n) - 1] > 0:
                nums[abs(n) - 1] *= -1
            else:
                cls.result.append(abs(n))

        return cls.result

    # 低内存消耗 484ms, 20.6MB
    @classmethod
    def find_duplicates_v2(cls, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            while nums[i] != i + 1:
                if nums[i] == nums[nums[i] - 1]:
                    cls.result.append(nums[i])
                    break
                else:
                    tmp = nums[nums[i] - 1]
                    nums[nums[i] - 1] = nums[i]
                    nums[i] = tmp
        
        return list(set(cls.result))

    # 低运行时间 464ms, 21.2MB
    @classmethod
    def find_duplicates_v3(cls, nums: List[int]) -> List[int]:
        n = len(nums)
        temp_dict = [0] * n

        for num in nums:
            temp_dict[num - 1] += 1
        for i in range(n):
            if temp_dict[i] > 1:
                cls.result.append(i + 1)

        return cls.result


if __name__ == '__main__':
    test = [4, 3, 2, 7, 8, 2, 3, 1]
    # print(Solution.find_duplicates(test))
    print(Solution.find_duplicates_v2(test))
    # print(Solution.find_duplicates_v3(test))
