"""
  @Author       : liujianhan
  @Date         : 2020/10/28 9:53
  @Project      : leetcode_in_python
  @FileName     : 1207.独一无二出现的次数.py
  @Description  : 给你一个整数数组 arr，请你帮忙统计数组中每个数的出现次数。
    如果每个数的出现次数都是独一无二的，就返回 true；否则返回 false。
    示例 1：
    输入：arr = [1,2,2,1,1,3]
    输出：true
    解释：在该数组中，1 出现了 3 次，2 出现了 2 次，3 只出现了 1 次。没有两个数的出现次数相同。
    示例 2：
    输入：arr = [1,2]
    输出：false
    示例 3：
    输入：arr = [-3,0,1,-3,1,1,1,-3,10,0]
    输出：true
    提示：
    1 <= arr.length <= 1000
    -1000 <= arr[i] <= 1000
"""
from typing import List
from collections import defaultdict


class Solution:
    # 84ms, 13.7MB
    @staticmethod
    def unique_occurrences(arr: List[int]) -> bool:
        count = {num: arr.count(num) for num in arr}
        return len(set(count.values())) == len(count)

    # 48ms, 13.7MB
    @staticmethod
    def unique_occurrences_v2(arr: List[int]) -> bool:
        count = defaultdict(int)
        for num in arr:
            count[num] += 1
        return len(set(count.values())) == len(count)


if __name__ == '__main__':
    test_cases = [
        [1, 2, 2, 1, 1, 3],
        [1, 2],
        [-3, 0, 1, -3, 1, 1, 1, -3, 10, 0]
    ]
    for tc in test_cases:
        print(Solution.unique_occurrences(tc))
        print(Solution.unique_occurrences_v2(tc))
