"""
  @Author       : liujianhan
  @Date         : 20/8/29 15:54
  @Project      : leetcode_in_python
  @FileName     : 275.H指数II(M).py
  @Description  : 给定一位研究者论文被引用次数的数组（被引用次数是非负整数），数组已经按照 升序排列 。编写一个方法，计算出研究者的 h 指数。
    h 指数的定义: “h 代表“高引用次数”（high citations），一名科研人员的 h 指数是指他（她）的 （N 篇论文中）总共有 h 篇论文分别被引用了至少 h 次。（其余的 N - h 篇论文每篇被引用次数不多于 h 次。）"
    示例:
    输入: citations = [0,1,3,5,6]
    输出: 3
    解释: 给定数组表示研究者总共有 5 篇论文，每篇论文相应的被引用了 0, 1, 3, 5, 6 次。
         由于研究者有 3 篇论文每篇至少被引用了 3 次，其余两篇论文每篇被引用不多于 3 次，所以她的 h 指数是 3。
    说明:
    如果 h 有多有种可能的值 ，h 指数是其中最大的那个。
"""
from typing import List


class Solution:
    # 48ms, 17.9MB
    @staticmethod
    def h_index(citations: List[int]) -> int:
        n = len(citations)
        left, right = 0, n - 1
        while left <= right:
            pivot = left + (right - left) // 2
            if citations[pivot] == n - pivot:
                return n - pivot
            elif citations[pivot] < n - pivot:
                left = pivot + 1
            else:
                right = pivot - 1

        return n - left


if __name__ == '__main__':
    test_cases = [
        [0, 1, 3, 5, 6]
    ]
    for tc in test_cases:
        print(Solution.h_index(tc))