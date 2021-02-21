"""
  @Author       : liujianhan
  @Date         : 21/2/21 11:12
  @Project      : leetcode_in_python
  @FileName     : 1438.绝对值不超过限制的最长连续子数组(M).py
  @Description  : 给你一个整数数组 nums ，和一个表示限制的整数 limit，请你返回最长连续子数组的长度，该子数组中的任意两个元素之间的
    绝对差必须小于或者等于 limit 。
    如果不存在满足条件的子数组，则返回 0 。

    示例 1：
    输入：nums = [8,2,4,7], limit = 4
    输出：2
    解释：所有子数组如下：
    [8] 最大绝对差 |8-8| = 0 <= 4.
    [8,2] 最大绝对差 |8-2| = 6 > 4.
    [8,2,4] 最大绝对差 |8-2| = 6 > 4.
    [8,2,4,7] 最大绝对差 |8-2| = 6 > 4.
    [2] 最大绝对差 |2-2| = 0 <= 4.
    [2,4] 最大绝对差 |2-4| = 2 <= 4.
    [2,4,7] 最大绝对差 |2-7| = 5 > 4.
    [4] 最大绝对差 |4-4| = 0 <= 4.
    [4,7] 最大绝对差 |4-7| = 3 <= 4.
    [7] 最大绝对差 |7-7| = 0 <= 4.
    因此，满足题意的最长子数组的长度为 2 。

    示例 2：
    输入：nums = [10,1,2,4,7,2], limit = 5
    输出：4
    解释：满足题意的最长子数组是 [2,4,7,2]，其最大绝对差 |2-7| = 5 <= 5 。

    示例 3：
    输入：nums = [4,2,2,2,4,4,2,2], limit = 0
    输出：3

    提示：

    1 <= nums.length <= 10^5
    1 <= nums[i] <= 10^9
    0 <= limit <= 10^9
"""
from collections import deque
from typing import List


class Solution:
    # 320ms, 21.5MB
    @staticmethod
    def longest_subarray(nums: List[int], limit: int) -> int:
        n = len(nums)
        que_max, que_min = deque(), deque()
        left = right = ret = 0

        while right < n:
            while que_max and que_max[-1] < nums[right]:
                que_max.pop()
            while que_min and que_min[-1] > nums[right]:
                que_min.pop()

            que_max.append(nums[right])
            que_min.append(nums[right])

            while que_max and que_min and que_max[0] - que_min[0] > limit:
                if nums[left] == que_min[0]:
                    que_min.popleft()
                if nums[left] == que_max[0]:
                    que_max.popleft()
                left += 1

            ret = max(ret, right - left + 1)
            right += 1

        return ret


if __name__ == '__main__':
    test_cases = [
        ([8, 2, 4, 7], 4),
        ([10, 1, 2, 4, 7, 2], 5),
        ([4, 2, 2, 2, 4, 4, 2, 2], 0),
    ]
    for test_case in test_cases:
        print(Solution.longest_subarray(*test_case))
