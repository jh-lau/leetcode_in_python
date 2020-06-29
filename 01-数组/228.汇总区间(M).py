"""
  @Author       : liujianhan
  @Date         : 2020/6/29 下午7:44
  @Project      : leetcode_in_python
  @FileName     : 228.汇总区间(M).py
  @Description  : 给定一个无重复元素的有序整数数组，返回数组区间范围的汇总。
    示例 1:
    输入: [0,1,2,4,5,7]
    输出: ["0->2","4->5","7"]
    解释: 0,1,2 可组成一个连续的区间; 4,5 可组成一个连续的区间。
    示例 2:
    输入: [0,2,3,4,6,8,9]
    输出: ["0","2->4","6","8->9"]
    解释: 2,3,4 可组成一个连续的区间; 8,9 可组成一个连续的区间。
"""
from typing import List


class Solution:
    # 48ms(19.24%), 13.4MB(100.00%)
    @staticmethod
    def summary_ranges(nums: List[int]) -> List[str]:
        n = len(nums)
        if n == 1:
            return [str(nums[0])]
        res = []
        l = 0
        r = 0
        cur = 0
        while cur < n:
            while cur < n and nums[cur] - nums[r] <= 1:
                r = cur
                cur += 1
            if l == r:
                res.append(str(nums[l]))
            else:
                res.append(str(nums[l]) + "->" + str(nums[r]))
            l = cur
            r = cur
        return res


if __name__ == '__main__':
    test_cases = [
        [0, 1, 2, 4, 5, 7],
        [0, 2, 3, 4, 6, 8, 9]
    ]
    for tc in test_cases:
        print(Solution.summary_ranges(tc))