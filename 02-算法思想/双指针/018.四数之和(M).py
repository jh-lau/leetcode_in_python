"""
  @Author       : Liujianhan
  @Date         : 20/4/30 22:45
  @FileName     : 018.四数之和(M).py
  @ProjectName  : leetcode_in_python
  @Description  : 给定一个包含 n 个整数的数组 nums 和一个目标值 target，判断 nums 中是否存在四个元素 a，b，c 和 d ，使得 a + b + c + d 的值与 target 相等？找出所有满足条件且不重复的四元组。
    注意：
    答案中不可以包含重复的四元组。
    示例：
    给定数组 nums = [1, 0, -1, 0, -2, 2]，和 target = 0。
    满足要求的四元组集合为：
    [
      [-1,  0, 0, 1],
      [-2, -1, 1, 2],
      [-2,  0, 0, 2]
]
 """
from typing import List


class Solution:
    # 108ms, 18Mb
    @classmethod
    def four_sum(cls, nums: List[int], target: int) -> List[List[int]]:
        N = len(nums)
        if N < 4:
            return []
        res = set()
        nums.sort()
        table = {}

        for i in range(N - 1):
            for j in range(i + 1, N):
                s = nums[i] + nums[j]
                if target - s in table:
                    for tmp in table[target - s]:
                        if tmp[1] < i:
                            res.add((nums[tmp[0]], nums[tmp[1]], nums[i], nums[j]))
                if s not in table:
                    table[s] = []
                table[s].append((i, j))
        ans = []
        for r in res:
            ans.append(list(r))

        return ans


if __name__ == '__main__':
    print(Solution.four_sum([1, 0, -1, 0, -2, 2], 0))
