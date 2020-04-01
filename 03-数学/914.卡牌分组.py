"""
  @Author       : Liujianhan
  @Date         : 20/3/27 22:55
  @FileName     : 914.卡牌分组.py
  @ProjectName  : leetcode_in_python
  @Description  : 给定一副牌，每张牌上都写着一个整数。
    此时，你需要选定一个数字 X，使我们可以将整副牌按下述规则分成 1 组或更多组：
    每组都有 X 张牌。
    组内所有的牌上都写着相同的整数。
    仅当你可选的 X >= 2 时返回 true。
    输入：[1,2,3,4,4,3,2,1]
    输出：true
    解释：可行的分组是 [1,1]，[2,2]，[3,3]，[4,4]
    输入：[1,1,1,2,2,2,3,3]
    输出：false
    解释：没有满足要求的分组。
 """
from typing import List


class Solution:
    # 72ms, 14MB
    @classmethod
    def has_group_size_x(cls, deck: List[int]) -> bool:
        dic = {}
        for num in deck:
            dic[num] = dic.get(num, 0) + 1
        times = [value for key, value in dic.items()]
        if min(times) < 2:
            return False
        for x in range(2, min(times) + 1):
            success = 1
            for num in times:
                if num % x:
                    success = 0
            if success == 1:
                return True
        return False


if __name__ == '__main__':
    test_case = [
        [1, 2, 3, 4, 4, 3, 2, 1],
        [1, 1, 1, 2, 2, 2, 3, 3]
    ]
    for tc in test_case:
        print(Solution.has_group_size_x(tc))
