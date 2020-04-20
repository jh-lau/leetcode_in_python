"""
  @Author       : liujianhan
  @Date         : 2020/4/20 下午1:54
  @Project      : leetcode_in_python
  @FileName     : 528.按权重随机选择(M).py
  @Description  : 给定一个正整数数组 w ，其中 w[i] 代表位置 i 的权重，请写一个函数 pickIndex ，它可以随机地获取位置 i，选取位置 i 的概率与 w[i] 成正比。
    说明:
    1 <= w.length <= 10000
    1 <= w[i] <= 10^5
    pickIndex 将被调用不超过 10000 次
    示例1:
    输入:
    ["Solution","pickIndex"]
    [[[1]],[]]
    输出: [null,0]
    示例2:
    输入:
    ["Solution","pickIndex","pickIndex","pickIndex","pickIndex","pickIndex"]
    [[[1,3]],[],[],[],[],[]]
    输出: [null,0,1,1,1,0]
    输入语法说明：
    输入是两个列表：调用成员函数名和调用的参数。Solution 的构造函数有一个参数，即数组 w。pickIndex 没有参数。输入参数是一个列表，即使参数为空，也会输入一个 [] 空列表。
"""
import bisect
import random
from typing import List


# 356ms, 18.3MB
class Solution:
    def __init__(self, w: List[int]):
        self.a = [0] * len(w)
        for i, j in enumerate(w):
            self.a[i] = self.a[i - 1] + j

    def pick_index(self) -> int:
        return bisect.bisect_left(self.a, random.randint(1, self.a[-1]))


if __name__ == '__main__':
    pass
