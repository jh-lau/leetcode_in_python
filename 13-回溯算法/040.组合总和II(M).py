"""
  @Author       : Liujianhan
  @Date         : 20/4/27 22:24
  @FileName     : 040.组合总和II(M).py
  @ProjectName  : leetcode_in_python
  @Description  : 给定一个数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。
    candidates 中的每个数字在每个组合中只能使用一次。
    说明：
    所有数字（包括目标数）都是正整数。
    解集不能包含重复的组合。 
    示例 1:
    输入: candidates = [10,1,2,7,6,1,5], target = 8,
    所求解集为:
    [
      [1, 7],
      [1, 2, 5],
      [2, 6],
      [1, 1, 6]
    ]
    示例 2:
    输入: candidates = [2,5,2,1,2], target = 5,
    所求解集为:
    [
      [1,2,2],
      [5]
    ]
 """
from typing import List


class Solution:
    # 44ms, 13.6MB
    def combination_sum2(self, candidates: List[int], target: int) -> List[List[int]]:
        if len(candidates) == 0:
            return []
        path = []
        res = []
        candidates.sort()
        self.__DFS(candidates, target, 0, path, res)
        return res

    def __DFS(self, candidates, target, begin, path, res):
        # 回朔点(递归出口
        path = path.copy()  # 如果不先copy，那么append到res中到path也会随着path的变换而变化
        if target == 0:
            res.append(path)
            return

        if begin > len(candidates) - 1:
            return

        # 回朔入口
        for cur in range(begin, len(candidates)):
            if cur > begin and candidates[cur - 1] == candidates[cur]:  # 数组常见去重复的方法，对于重复的数值，我们只让第一个进入循环，后面的就不要再进入循环了
                continue
            temp = target - candidates[cur]
            # 剪枝
            if temp < 0:
                return
            else:
                path.append(candidates[cur])
                self.__DFS(candidates, temp, cur + 1, path, res)  # 一定是cur+1，
                path.pop()


if __name__ == '__main__':
    test_cases = [
        ([2, 5, 2, 1, 2], 5),
        ([10, 1, 2, 7, 6, 1, 5], 8)
    ]
    for tc in test_cases:
        print(Solution().combination_sum2(*tc))
