"""
  @Author       : Liujianhan
  @Date         : 20/4/28 22:53
  @FileName     : 56-II.数组中数字出现的数字(M).py
  @ProjectName  : leetcode_in_python
  @Description  : 在一个数组 nums 中除一个数字只出现一次之外，其他数字都出现了三次。请找出那个只出现一次的数字。
    示例 1：

    输入：nums = [3,4,3,3]
    输出：4
    示例 2：

    输入：nums = [9,1,7,9,7,9,7]
    输出：1
    限制：

    1 <= nums.length <= 10000
    1 <= nums[i] < 2^31
 """
from typing import List


class Solution:
    # 68ms, 14.8MB
    @classmethod
    def single_number(cls, nums: List[int]) -> int:
        ones, twos = 0, 0
        for num in nums:
            ones = ones ^ num & ~twos
            twos = twos ^ num & ~ones

        return ones


if __name__ == '__main__':
    test_cases = [
        [3, 4, 3, 3], [9, 1, 7, 9, 9, 7, 7]
    ]
    for tc in test_cases:
        print(Solution.single_number(tc))
