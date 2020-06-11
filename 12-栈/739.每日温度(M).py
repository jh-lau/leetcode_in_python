"""
  @Author       : Liujianhan
  @Date         : 20/6/11 21:37
  @FileName     : 739.每日温度(M).py
  @ProjectName  : leetcode_in_python
  @Description  : 请根据每日 气温 列表，重新生成一个列表。对应位置的输出为：要想观测到更高的气温，至少需要等待的天数。如果气温在这之后都不会升高，请在该位置用 0 来代替。
    例如，给定一个列表 temperatures = [73, 74, 75, 71, 69, 72, 76, 73]，你的输出应该是 [1, 1, 4, 2, 1, 1, 0, 0]。
    提示：气温 列表长度的范围是 [1, 30000]。每个气温的值的均为华氏度，都是在 [30, 100] 范围内的整数。
 """
from typing import List


class Solution:
    # 1128ms, 17.4MB
    @classmethod
    def daily_temperatures(cls, T: List[int]) -> List[int]:
        d = {}
        ans = [0] * len(T)
        for i in range(len(T) - 1, -1, -1):
            d[T[i]] = i
            tmp = [d[t] - i for t in range(T[i] + 1, 101) if t in d]
            ans[i] = (min(tmp) if tmp else 0)
        return ans

    # 684ms, 17.2MB
    @classmethod
    def daily_temperatures_v2(cls, T: List[int]) -> List[int]:
        res = [0] * len(T)
        stack = []
        for i, t in enumerate(T):
            while stack and t > T[stack[-1]]:
                res[stack.pop()] = i - stack[-1]
            stack.append(i)
        return res


if __name__ == '__main__':
    print(Solution.daily_temperatures([73, 74, 75, 71, 69, 72, 76, 73]))
    print(Solution.daily_temperatures_v2([73, 74, 75, 71, 69, 72, 76, 73]))
