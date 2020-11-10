"""
  @Author       : liujianhan
  @Date         : 2020/11/10 11:05
  @Project      : leetcode_in_python
  @FileName     : 506.相对名次.py
  @Description  : 给出 N 名运动员的成绩，找出他们的相对名次并授予前三名对应的奖牌。
    前三名运动员将会被分别授予 “金牌”，“银牌” 和“ 铜牌”（"Gold Medal", "Silver Medal", "Bronze Medal"）。
    (注：分数越高的选手，排名越靠前。)
    示例 1:
    输入: [5, 4, 3, 2, 1]
    输出: ["Gold Medal", "Silver Medal", "Bronze Medal", "4", "5"]
    解释: 前三名运动员的成绩为前三高的，因此将会分别被授予 “金牌”，“银牌”和“铜牌” ("Gold Medal", "Silver Medal" and "Bronze Medal").
    余下的两名运动员，我们只需要通过他们的成绩计算将其相对名次即可。
    提示:
    N 是一个正整数并且不会超过 10000。
    所有运动员的成绩都不相同。
"""
from typing import List


class Solution:
    # 104ms, 14.9MB
    @staticmethod
    def find_relative_ranks(nums: List[int]) -> List[str]:
        rank_dic = {score: rank for rank, score in enumerate(sorted(nums, reverse=True))}
        rank_map = {1: "Gold Medal", 2: 'Silver Medal', 3: 'Bronze Medal'}
        return [rank_map.get(rank_dic[num] + 1, str(rank_dic[num] + 1)) for num in nums]


if __name__ == '__main__':
    test_cases = [
        [5, 4, 3, 2, 1],
        [10, 3, 8, 9, 4]
    ]
    for tc in test_cases:
        print(Solution.find_relative_ranks(tc))
