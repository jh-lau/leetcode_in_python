"""
  @Author       : Liujianhan
  @Date         : 20/4/16 22:05
  @FileName     : 441.排列硬币.py
  @ProjectName  : leetcode_in_python
  @Description  : 你总共有 n 枚硬币，你需要将它们摆成一个阶梯形状，第 k 行就必须正好有 k 枚硬币。
    给定一个数字 n，找出可形成完整阶梯行的总行数。
    n 是一个非负整数，并且在32位有符号整型的范围内。
    示例 1:
    n = 5
    硬币可排列成以下几行:
    ¤
    ¤ ¤
    ¤ ¤
    因为第三行不完整，所以返回2.
    示例 2:
    n = 8
    硬币可排列成以下几行:
    ¤
    ¤ ¤
    ¤ ¤ ¤
    ¤ ¤
    因为第四行不完整，所以返回3.
 """


class Solution:
    # 1860ms, 13.6MB
    @classmethod
    def arrange_coins(cls, n: int) -> int:
        if not n:
            return n
        rest, index = 0, 1
        while n >= index:
            rest = n - index - rest
            n -= index
            index += 1

        return index - 1 if index != 1 else 1

    # 44ms, 13.7MB
    @classmethod
    def arrange_coins_v2(cls, n: int) -> int:
        return int(((1+8*n)**0.5-1)/2)

    # 47ms, 13.7MB
    @classmethod
    def arrange_coins_v3(cls, n: int) -> int:
        l, r = 0, n // 2 + 1
        while l < r:
            m = l + (r - l) // 2
            target = m * (m + 1) / 2
            if target < n - m:
                l = m + 1
            else:
                r = m
        return l


if __name__ == '__main__':
    for tc in [0, 1, 3, 5, 8]:
        print(Solution.arrange_coins_v3(tc))

