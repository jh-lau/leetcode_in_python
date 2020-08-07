"""
  @Author       : liujianhan
  @Date         : 2020/8/7 上午9:38
  @Project      : leetcode_in_python
  @FileName     : 260.只出现一次的数字II(M).py
  @Description  : 给定一个整数数组 nums，其中恰好有两个元素只出现一次，其余所有元素均出现两次。 找出只出现一次的那两个元素。

    示例 :

    输入: [1,2,1,3,2,5]
    输出: [3,5]
    注意：

    结果输出的顺序并不重要，对于上面的例子， [5, 3] 也是正确答案。
    你的算法应该具有线性时间复杂度。你能否仅使用常数空间复杂度来实现？
"""
from typing import List


class Solution:
    # 48ms, 14.6MB
    @staticmethod
    def single_number(nums: List[int]) -> List[int]:
        bitmask = 0
        for num in nums:
            bitmask ^= num

        diff = bitmask & (-bitmask)

        x = 0
        for num in nums:
            if num & diff:
                x ^= num

        return [x, bitmask ^ x]


if __name__ == '__main__':
    test_cases = [
        [1, 2, 1, 3, 2, 5],
        [1, 2, 1, 3, 2, 5, 5, 7]
    ]
    for tc in test_cases:
        print(Solution.single_number(tc))
