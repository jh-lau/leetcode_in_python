"""
  @Author       : liujianhan
  @Date         : 2020/8/22 18:58
  @Project      : leetcode_in_python
  @FileName     : 679.24点游戏(H).py
  @Description  : 你有 4 张写有 1 到 9 数字的牌。你需要判断是否能通过 *，/，+，-，(，) 的运算得到 24。
    示例 1:
    输入: [4, 1, 8, 7]
    输出: True
    解释: (8-4) * (7-1) = 24
    示例 2:
    输入: [1, 2, 1, 2]
    输出: False
    注意:
    除法运算符 / 表示实数除法，而不是整数除法。例如 4 / (1 - 2/3) = 12 。
    每个运算符对两个数进行运算。特别是我们不能用 - 作为一元运算符。例如，[1, 1, 1, 1] 作为输入时，表达式 -1 - 1 - 1 - 1 是不允许的。
    你不能将数字连接在一起。例如，输入为 [1, 2, 1, 2] 时，不能写成 12 + 12 。
"""
from typing import List


class Solution:
    # 168ms, 13.7MB
    @staticmethod
    def judge_point24(nums: List[int]) -> bool:
        if not nums:
            return False

        def helper(nums):
            if len(nums) == 1:
                return abs(nums[0] - 24) < 1e-6
            for i in range(len(nums)):
                for j in range(len(nums)):
                    if i != j:
                        new_nums = [nums[k] for k in range(len(nums)) if i != k != j]
                        if helper(new_nums + [nums[i] + nums[j]]):
                            return True
                        if helper(new_nums + [nums[i] - nums[j]]):
                            return True
                        if helper(new_nums + [nums[i] * nums[j]]):
                            return True
                        if nums[j] != 0 and helper(new_nums + [nums[i] / nums[j]]):
                            return True
            return False

        return helper(nums)


if __name__ == '__main__':
    test_cases = [
        [4, 1, 8, 7],
        [1, 2, 1, 2]
    ]
    for tc in test_cases:
        print(Solution.judge_point24(tc))
