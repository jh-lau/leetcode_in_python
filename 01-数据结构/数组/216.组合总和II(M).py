"""
  @Author       : Liujianhan
  @Date         : 20/6/20 21:32
  @FileName     : 216.组合总和II(M).py
  @ProjectName  : leetcode_in_python
  @Description  : 找出所有相加之和为 n 的 k 个数的组合。组合中只允许含有 1 - 9 的正整数，并且每种组合中不存在重复的数字。
    说明：
    所有数字都是正整数。
    解集不能包含重复的组合。 
    示例 1:
    输入: k = 3, n = 7
    输出: [[1,2,4]]
    示例 2:
    输入: k = 3, n = 9
    输出: [[1,2,6], [1,3,5], [2,3,4]]
 """
from typing import List


class Solution:
    # 40ms, 13.6MB
    @classmethod
    def combination_sum3(cls, k: int, n: int) -> List[List[int]]:
        def back(candidates, cur, target, length):
            if len(cur) == length and target == 0:  # 回溯的退出条件
                res.append(cur.copy())
            for i in range(len(candidates)):
                if len(cur) > 0 and candidates[i] < cur[-1]:  # 若出现逆序，则剪枝，防止出现重复的情况例如 [1,2] [2,1]是一种
                    continue
                cur.append(candidates[i])
                back(candidates[:i] + candidates[i + 1:], cur, target - candidates[i], length)
                cur.pop()  # 记得恢复之前的状态

        res = []
        nums = [i for i in range(1, 10)]
        back(nums, [], n, k)
        return res


if __name__ == '__main__':
    test_cases = [
        (3, 7),
        (3, 9),
    ]
    for tc in test_cases:
        print(Solution.combination_sum3(*tc))
