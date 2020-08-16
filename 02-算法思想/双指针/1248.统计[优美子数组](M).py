"""
  @Author       : liujianhan
  @Date         : 2020/4/21 上午11:52
  @Project      : leetcode_in_python
  @FileName     : 1248.统计[优美子数组](M).py
  @Description  : 给你一个整数数组 nums 和一个整数 k。
    如果某个 连续 子数组中恰好有 k 个奇数数字，我们就认为这个子数组是「优美子数组」。
    请返回这个数组中「优美子数组」的数目。
    示例 1：
    输入：nums = [1,1,2,1,1], k = 3
    输出：2
    解释：包含 3 个奇数的子数组是 [1,1,2,1] 和 [1,2,1,1] 。
    示例 2：
    输入：nums = [2,4,6], k = 1
    输出：0
    解释：数列中不包含任何奇数，所以不存在优美子数组。
    示例 3：
    输入：nums = [2,2,2,1,2,2,1,2,2,2], k = 2
    输出：16
    提示：
    1 <= nums.length <= 50000
    1 <= nums[i] <= 10^5
    1 <= k <= nums.length
"""
from typing import List


class Solution:
    # 944ms, 20.4MB
    @classmethod
    def number_of_sub_arrays(cls, nums: List[int], k: int) -> int:
        """数学"""
        n = len(nums)
        odd = [-1]
        ans = 0
        for i in range(n):
            if nums[i] % 2 == 1:
                odd.append(i)
        odd.append(n)
        for i in range(1, len(odd) - k):
            ans += (odd[i] - odd[i - 1]) * (odd[i + k] - odd[i + k - 1])

        return ans

    # 964ms, 20.3MB
    @classmethod
    def number_of_sub_arrays_v2(cls, nums: List[int], k: int) -> int:
        """前缀和+差分"""
        cnt = [0] * (len(nums) + 1)
        cnt[0] = 1
        odd, ans = 0, 0
        for num in nums:
            if num % 2 == 1:
                odd += 1
            if odd >= k:
                ans += cnt[odd - k]
            cnt[odd] += 1

        return ans

    # 1320ms, 20.1MB
    @classmethod
    def number_of_sub_arrays_v3(cls, nums: List[int], k: int) -> int:
        """双指针"""
        l, r, cnt, ans = 0, -1, 0, 0
        while r + 1 < len(nums):
            r += 1
            cnt += nums[r] & 1

            while r + 1 < len(nums) and cnt < k:
                r += 1
                cnt += nums[r] & 1
            if r >= len(nums):
                break
            k_cnt_right_begin = r

            while r + 1 < len(nums) and not nums[r + 1] & 1:
                r += 1

            while l <= r and cnt == k:
                ans += r - k_cnt_right_begin + 1
                cnt -= nums[l] & 1
                l += 1
                
        return ans


if __name__ == '__main__':
    test_cases = [
        ([1, 1, 2, 1, 1], 3),
        ([2, 4, 6], 1),
        ([2, 2, 2, 1, 2, 2, 1, 2, 2, 2], 2)
    ]
    for tc in test_cases:
        print(Solution.number_of_sub_arrays(*tc))
        print(Solution.number_of_sub_arrays_v2(*tc))
        print(Solution.number_of_sub_arrays_v3(*tc))
