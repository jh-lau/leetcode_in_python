"""
  @Author       : liujianhan
  @Date         : 2020/7/8 上午11:22
  @Project      : leetcode_in_python
  @FileName     : 16.11.跳水板.py
  @Description  : 你正在使用一堆木板建造跳水板。有两种类型的木板，其中长度较短的木板长度为shorter，长度较长的木板长度为longer。你必须正好使用k块木板。编写一个方法，生成跳水板所有可能的长度。
    返回的长度需要从小到大排列。
    示例：
    输入：
    shorter = 1
    longer = 2
    k = 3
    输出： {3,4,5,6}
    提示：
    0 < shorter <= longer
    0 <= k <= 100000
"""
from typing import List


class Solution:
    # 76ms, 17.6MB
    @staticmethod
    def diving_board(shorter: int, longer: int, k: int) -> List[int]:
        if not k:
            return []
        if shorter == longer:
            return [shorter * k]
        res = [0] * (k + 1)
        for i in range(k + 1):
            res[i] = shorter * (k - i) + longer * i
        return res


if __name__ == '__main__':
    print(Solution.diving_board(1, 2, 3))
