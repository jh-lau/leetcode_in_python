"""
  @Author       : liujianhan
  @Date         : 2020/5/27 上午11:46
  @Project      : leetcode_in_python
  @FileName     : 174.地下城游戏(H).py
  @Description  : 一些恶魔抓住了公主（P）并将她关在了地下城的右下角。地下城是由 M x N 个房间组成的二维网格。
    我们英勇的骑士（K）最初被安置在左上角的房间里，他必须穿过地下城并通过对抗恶魔来拯救公主。
    骑士的初始健康点数为一个正整数。如果他的健康点数在某一时刻降至 0 或以下，他会立即死亡。
    有些房间由恶魔守卫，因此骑士在进入这些房间时会失去健康点数（若房间里的值为负整数，则表示骑士将损失健康点数）；
    其他房间要么是空的（房间里的值为 0），要么包含增加骑士健康点数的魔法球（若房间里的值为正整数，则表示骑士将增加健康点数）。
    为了尽快到达公主，骑士决定每次只向右或向下移动一步。
    编写一个函数来计算确保骑士能够拯救到公主所需的最低初始健康点数。
    例如，考虑到如下布局的地下城，如果骑士遵循最佳路径 右 -> 右 -> 下 -> 下，则骑士的初始健康点数至少为 7。
    -2 (K)	-3	3
    -5	-10	1
    10	30	-5 (P)
    说明:
    骑士的健康点数没有上限。
    任何房间都可能对骑士的健康点数造成威胁，也可能增加骑士的健康点数，包括骑士进入的左上角房间以及公主被监禁的右下角房间。
"""
from typing import List


class Solution:
    # 60ms, 14.3MB
    @classmethod
    def calculate_minimum_hp(cls, dungeon: List[List[int]]) -> int:
        m = len(dungeon)
        n = len(dungeon[0])
        if m == 1 and n == 1:  # 1x1的地牢
            return max(1, 1 - dungeon[0][0])
        elif m == 1 and n != 1:  # 1xn的地牢
            newlist = []
            for i in range(n):
                newlist.append(-1)
            newlist[-1] = max(1, 1 - dungeon[0][-1])
            for i in range(n - 1):
                tempindex = n - i - 2
                newlist[tempindex] = max(1, newlist[tempindex + 1] - dungeon[0][tempindex])
            return newlist[0]
        elif m != 1 and n == 1:  # nx1的地牢
            newlist = []
            for i in range(m):
                newlist.append(-1)
            newlist[-1] = max(1, 1 - dungeon[-1][0])
            for i in range(m - 1):
                tempindex = m - i - 2
                newlist[tempindex] = max(1, newlist[tempindex + 1] - dungeon[tempindex][0])
            return newlist[0]
        # 以下针对mxn的地牢，m和n都大于1
        # 初始化一个m行n列的dplist
        print('地牢的size为', m, n)
        newlist = []
        for i in range(m):
            templist = []
            for j in range(n):
                templist.append(-1)
            newlist.append(templist)
        # 我们先初始化最下面一行和最右边一列
        # 先初始化最右下角的
        newlist[m - 1][n - 1] = max(1, 1 - dungeon[-1][-1])
        # 最下面一行，共n-1个待补充的数字
        for i in range(n - 1):
            tempindex = n - i - 2
            newlist[-1][tempindex] = max(1, newlist[-1][tempindex + 1] - dungeon[-1][tempindex])
        # 最右边一列，共m-1个待补充的数字
        for j in range(m - 1):
            tempindex = m - j - 2
            newlist[tempindex][-1] = max(1, newlist[tempindex + 1][-1] - dungeon[tempindex][-1])
        # 从[m-2][n-2]开始填充,一直到[0][0],共(m-1)x(n-1)个
        # 先从倒数第二行倒数第二列开始，然后是倒数第二行倒数第三列，......
        for i in range(m - 1):
            tempi = m - i - 2
            for j in range(n - 1):
                tempj = n - j - 2
                newlist[tempi][tempj] = max(1,
                                            min(newlist[tempi + 1][tempj], newlist[tempi][tempj + 1]) - dungeon[tempi][
                                                tempj])
        print(newlist)
        return newlist[0][0]
