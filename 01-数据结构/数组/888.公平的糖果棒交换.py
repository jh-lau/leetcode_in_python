"""
  @Author       : liujianhan
  @Date         : 2021/2/1 10:05
  @Project      : leetcode_in_python
  @FileName     : 888.公平的糖果棒交换.py
  @Description  : 爱丽丝和鲍勃有不同大小的糖果棒：A[i] 是爱丽丝拥有的第 i 根糖果棒的大小，B[j] 是鲍勃拥有的第 j 根糖果棒的大小。
    因为他们是朋友，所以他们想交换一根糖果棒，这样交换后，他们都有相同的糖果总量。（一个人拥有的糖果总量是他们拥有的糖果棒大小的总和。）
    返回一个整数数组 ans，其中 ans[0] 是爱丽丝必须交换的糖果棒的大小，ans[1] 是 Bob 必须交换的糖果棒的大小。
    如果有多个答案，你可以返回其中任何一个。保证答案存在。

    示例 1：
    输入：A = [1,1], B = [2,2]
    输出：[1,2]

    示例 2：
    输入：A = [1,2], B = [2,3]
    输出：[1,2]

    示例 3：
    输入：A = [2], B = [1,3]
    输出：[2,3]

    示例 4：
    输入：A = [1,2,5], B = [2,4]
    输出：[5,4]

    提示：
    1 <= A.length <= 10000
    1 <= B.length <= 10000
    1 <= A[i] <= 100000
    1 <= B[i] <= 100000
    保证爱丽丝与鲍勃的糖果总量不同。
    答案肯定存在。
"""
from collections import defaultdict
from typing import List


class Solution:
    # 384ms, 17.6MB
    @staticmethod
    def fair_candy_swap(A: List[int], B: List[int]) -> List[int]:
        diff = (sum(B) - sum(A)) // 2
        b_dict = {i: True for i in B}
        b_dict = defaultdict(bool, b_dict)
        for a in A:
            if b_dict[a + diff]:
                return [a, a + diff]

    # 5296ms, 17MB
    @staticmethod
    def fair_candy_swap_slow_version(A: List[int], B: List[int]) -> List[int]:
        sa, sb = sum(A), sum(B)
        temp = int((sa - sb) / 2)
        for b in B:
            if temp + b in set(A):
                return [temp+b, b]


if __name__ == '__main__':
    test_cases = [
        ([1, 1], [2, 2]),
        ([1, 2], [2, 3]),
        ([2], [1, 3]),
        ([1, 2, 5], [2, 4]),
    ]
    for tc in test_cases:
        print(Solution.fair_candy_swap(*tc))
