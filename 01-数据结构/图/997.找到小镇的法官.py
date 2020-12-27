"""
  @Author       : liujianhan
  @Date         : 2020/12/21 10:27
  @Project      : leetcode_in_python
  @FileName     : 997.找到小镇的法官.py
  @Description  : 在一个小镇里，按从 1 到 N 标记了 N 个人。传言称，这些人中有一个是小镇上的秘密法官。
    如果小镇的法官真的存在，那么：
    小镇的法官不相信任何人。
    每个人（除了小镇法官外）都信任小镇的法官。
    只有一个人同时满足属性 1 和属性 2 。
    给定数组 trust，该数组由信任对 trust[i] = [a, b] 组成，表示标记为 a 的人信任标记为 b 的人。
    如果小镇存在秘密法官并且可以确定他的身份，请返回该法官的标记。否则，返回 -1。

    示例 1：
    输入：N = 2, trust = [[1,2]]
    输出：2

    示例 2：
    输入：N = 3, trust = [[1,3],[2,3]]
    输出：3

    示例 3：
    输入：N = 3, trust = [[1,3],[2,3],[3,1]]
    输出：-1

    示例 4：
    输入：N = 3, trust = [[1,2],[2,3]]
    输出：-1

    示例 5：
    输入：N = 4, trust = [[1,3],[1,4],[2,3],[2,4],[4,3]]
    输出：3

    提示：
    1 <= N <= 1000
    trust.length <= 10000
    trust[i] 是完全不同的
    trust[i][0] != trust[i][1]
    1 <= trust[i][0], trust[i][1] <= N
"""
from typing import List
from collections import defaultdict, Counter


class Solution:
    # 868ms, 19.4MB
    @staticmethod
    def find_judge(N: int, trust: List[List[int]]) -> int:
        if N == 1 and not trust:
            return 1
        trusted = defaultdict(int)
        trust_ = defaultdict(list)
        for i, j in trust:
            trusted[j] += 1
            trust_[i].append(j)

        candidates = [k for k, v in trusted.items() if v == N - 1]
        if len(candidates) != 1:
            return -1
        else:
            judge = candidates[0]
            if judge in trust_:
                return -1
            return judge

    # 776ms, 19.5MB
    @staticmethod
    def find_judge_v2(N: int, trust: List[List[int]]) -> int:
        if N == 1:
            return 1
        trusted = [p[1] for p in trust]
        people = [p[0] for p in trust]
        trudic = Counter(trusted)
        for p, t in trudic.items():
            if t == N - 1 and p not in people:
                return p
        return -1


if __name__ == '__main__':
    test_cases = [
        (1, []),
        (2, [[1, 2]]),
        (3, [[1, 3], [2, 3]]),
        (3, [[1, 3], [2, 3], [3, 1]]),
        (3, [[1, 2], [2, 3]]),
        (4, [[1, 3], [1, 4], [2, 3], [2, 4], [4, 3]])
    ]
    for tc in test_cases:
        print(Solution.find_judge(*tc))
