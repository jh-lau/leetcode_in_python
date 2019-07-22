"""
  Created by PyCharm.
  User: Liujianhan
  Date: 2019/5/7
  Time: 16:24
 """
__author__ = 'liujianhan'


class KMP:
    @staticmethod
    def get_next(p):
        """
        从模式字符串的第一位（不包括第0位）开始对自身进行匹配运算
        :param p: 模式字符串
        :return: 部分匹配表
        """
        nex = [0] * len(p)
        nex[0] = -1
        i = 0
        j = -1
        while i < len(p) - 1:
            if -1 == j or p[i] == p[j]:
                i += 1
                j += 1
                # 改进版
                # if p[i] == p[j]:
                #     nex[i] = nex[j]
                # else:
                #     nex[i] = j
                nex[i] = j
            else:
                j = nex[j]
        return nex

    @staticmethod
    def kmp(s, p):
        """
        :param s: 被匹配字符串
        :param p: 模式串
        :return:
        """
        nex = KMP.get_next(p)
        i = j = 0
        while i < len(s) and j < len(p):
            if -1 == j or s[i] == p[j]:
                i += 1
                j += 1
            else:
                j = nex[j]

        # j移动到模式串最末，说明匹配成功
        if j == len(p):
            return i - j
        else:
            return -1


p1 = 'abababca'
p2 = 'aba'
p3 = 'ababaaababaa'
s = 'absaf3adfabababca'
print(KMP.get_next(p1))
print(KMP.kmp(s, p1))
