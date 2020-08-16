"""
  @Author       : Liujianhan
  @Date         : 20/8/15 17:18
  @FileName     : 546.移除盒子(H).py
  @ProjectName  : leetcode_in_python
  @Description  : 给出一些不同颜色的盒子，盒子的颜色由数字表示，即不同的数字表示不同的颜色。
    你将经过若干轮操作去去掉盒子，直到所有的盒子都去掉为止。每一轮你可以移除具有相同颜色的连续 k 个盒子（k >= 1），这样一轮之后你将得到 k*k 个积分。
    当你将所有盒子都去掉之后，求你能获得的最大积分和。
    示例：
    输入：boxes = [1,3,2,2,2,3,4,3,1]
    输出：23
    解释：
    [1, 3, 2, 2, 2, 3, 4, 3, 1]
    ----> [1, 3, 3, 4, 3, 1] (3*3=9 分)
    ----> [1, 3, 3, 3, 1] (1*1=1 分)
    ----> [1, 1] (3*3=9 分)
    ----> [] (2*2=4 分)
    提示：

    1 <= boxes.length <= 100
    1 <= boxes[i] <= 100
 """
from typing import List


class Solution:
    # 1224ms, 23.6MB
    @staticmethod
    def remove_boxes(boxes: List[int]) -> int:
        memo = {}
        # 已知boxes[l]有n个的情况下，boxes[l:r]能获得的最大积分
        def dp(l, r, n):
            nonlocal memo, boxes
            if memo.get((l, r, n)):
                return memo[(l, r, n)]

            # 只剩最后一个数字，直接结算
            if l == r - 1:
                return (n + 1) * (n + 1)

            # 发现邻居和自己相同，和他加一起结算
            if boxes[l] == boxes[l + 1]:
                return dp(l + 1, r, n + 1)

            # 先直接结算，之后再看有没有和自己一样的
            res = (n + 1) * (n + 1) + dp(l + 1, r, 0)

            # 已知下一个和自己不一样，从下下个开始找和自己一样的兄弟
            for l2 in range(l + 2, r):
                # 找到兄弟了
                if boxes[l2] == boxes[l]:
                    res = max(
                        res,
                        # 让自己的下一个到这个兄弟之前结算,
                        # 然后让自己和兄弟加起来结算，
                        # 然后取最大值
                        dp(l + 1, l2, 0) + dp(l2, r, n + 1)
                    )
            memo[(l, r, n)] = res
            return res

        # 初始状态为 已知boxes[0]有0个的情况下， boxes[0:]能获得的最大积分
        return dp(0, len(boxes), 0)


if __name__ == '__main__':
    test_cases = [
        [1, 3, 2, 2, 2, 3, 4, 3, 1]
    ]
    for tc in test_cases:
        print(Solution.remove_boxes(tc))
