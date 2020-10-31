"""
  @Author       : liujianhan
  @Date         : 2020/10/31 10:10
  @Project      : leetcode_in_python
  @FileName     : 697.数组的度.py
  @Description  : 给定一个非空且只包含非负数的整数数组 nums, 数组的度的定义是指数组里任一元素出现频数的最大值。
    你的任务是找到与 nums 拥有相同大小的度的最短连续子数组，返回其长度。
    示例 1:
    输入: [1, 2, 2, 3, 1]
    输出: 2
    解释:
    输入数组的度是2，因为元素1和2的出现频数最大，均为2.
    连续子数组里面拥有相同度的有如下所示:
    [1, 2, 2, 3, 1], [1, 2, 2, 3], [2, 2, 3, 1], [1, 2, 2], [2, 2, 3], [2, 2]
    最短连续子数组[2, 2]的长度为2，所以返回2.
    示例 2:

    输入: [1,2,2,3,1,4,2]
    输出: 6
    注意:
    nums.length 在1到50,000区间范围内。
    nums[i] 是一个在0到49,999范围内的整数。
"""
from typing import List


class Solution:
    # 1020ms, 14.8MB
    @staticmethod
    def find_shortest_subarray(nums: List[int]) -> int:
        lookup = {k: nums.count(k) for k in set(nums)}
        degree = max(lookup.values())
        candi_nums = [s for s in set(nums) if lookup[s] == degree]

        return min([len(nums) - nums[::-1].index(s) - nums.index(s) for s in candi_nums])

    # 64ms, 14.5MB
    @staticmethod
    def find_shortest_subarray_v2(nums: List[int]) -> int:
        if nums:
            left, right, num_dict = {}, {}, {}
            for i, num in enumerate(nums):
                if num not in num_dict:
                    num_dict[num] = 1
                    left[num] = i
                    right[num] = i
                else:
                    num_dict[num] += 1
                    right[num] = i

            degree = max(num_dict.values())

            ans = len(nums)
            for num in num_dict:
                if num_dict[num] == degree:
                    ans = min(ans, right[num] - left[num] + 1)
            return ans


if __name__ == '__main__':
    test_cases = [
        [1, 2, 2, 3, 1],
        [1, 2, 2, 3, 1, 4, 2]
    ]
    for tc in test_cases:
        print(Solution.find_shortest_subarray(tc))
        print(Solution.find_shortest_subarray_v2(tc))
