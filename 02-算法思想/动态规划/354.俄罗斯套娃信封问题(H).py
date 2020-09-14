"""
  @Author       : liujianhan
  @Date         : 2020/9/14 10:18
  @Project      : leetcode_in_python
  @FileName     : 354.俄罗斯套娃信封问题(H).py
  @Description  : 给定一些标记了宽度和高度的信封，宽度和高度以整数对形式 (w, h) 出现。当另一个信封的宽度和高度都比这个信封大的时候，
    这个信封就可以放进另一个信封里，如同俄罗斯套娃一样。
    请计算最多能有多少个信封能组成一组“俄罗斯套娃”信封（即可以把一个信封放到另一个信封里面）。
    说明:
    不允许旋转信封。

    示例:

    输入: envelopes = [[5,4],[6,4],[6,7],[2,3]]
    输出: 3
    解释: 最多信封的个数为 3, 组合为: [2,3] => [5,4] => [6,7]。
"""
from bisect import bisect_left
from typing import List


class Solution:
    # 192ms, 16MB
    @staticmethod
    def max_envelopes(envelopes: List[List[int]]) -> int:
        envelopes.sort(key=lambda x: (x[0], -x[1]))

        def lis(nums):
            dp = []
            for i in range(len(nums)):
                idx = bisect_left(dp, nums[i])
                if idx == len(dp):
                    dp.append(nums[i])
                else:
                    dp[idx] = nums[i]
            return len(dp)

        return lis([i[1] for i in envelopes])

    # 204ms, 15.9MB
    @staticmethod
    def max_envelopes_v2(envelopes: List[List[int]]) -> int:
        size = len(envelopes)
        if size == 0:
            return 0

        # sort, 对w升序, 对h降序
        envelopes.sort(key=lambda x: [x[0], -x[1]])

        b = [0 for _ in range(size)]
        res = 0
        # binary search by h
        for env in envelopes:
            start, end = 0, res
            while start < end:
                mid = start + ((end - start) // 2)
                if b[mid] < env[1]:
                    start = mid + 1
                else:
                    end = mid

            b[start] = env[1]
            if end == res:
                b[res] = env[1]
                res += 1
        return res


if __name__ == '__main__':
    test_cases = [
        [[5, 4], [6, 4], [6, 7], [2, 3]]
    ]
    for tc in test_cases:
        print(Solution.max_envelopes(tc))
        print(Solution.max_envelopes_v2(tc))
