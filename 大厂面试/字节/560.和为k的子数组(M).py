"""
  @Author       : Liujianhan
  @Date         : 20/5/15 22:34
  @FileName     : 560.和为k的子数组(M).py
  @ProjectName  : leetcode_in_python
  @Description  : 给定一个整数数组和一个整数 k，你需要找到该数组中和为 k 的连续的子数组的个数。
    示例 1 :
    输入:nums = [1,1,1], k = 2
    输出: 2 , [1,1] 与 [1,1] 为两种不同的情况。
    说明 :
    数组的长度为 [1, 20,000]。
    数组中元素的范围是 [-1000, 1000] ，且整数 k 的范围是 [-1e7, 1e7]。
 """
from typing import List


class Solution:
    # 80ms, 16MB
    @classmethod
    def subarray_sum(cls, nums: List[int], k: int) -> int:
        if len(nums) == 0:
            return 0
        d = {0: 1}  # 初始化字典（哈希表），设置-1项的值为0
        pre_sum = 0
        cnt = 0
        for num in nums:
            pre_sum += num
            if d.get(pre_sum - k):
                cnt += d[pre_sum - k]
            if d.get(pre_sum):
                d[pre_sum] += 1
            else:
                d[pre_sum] = 1
        return cnt


if __name__ == '__main__':
    test_cases = [
        ([1,1,1], 2)
    ]
    for tc in test_cases:
        print(Solution.subarray_sum(*tc))
