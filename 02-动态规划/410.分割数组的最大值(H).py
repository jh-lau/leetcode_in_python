"""
  @Author       : liujianhan
  @Date         : 2020/7/25 上午10:28
  @Project      : leetcode_in_python
  @FileName     : 410.分割数组的最大值(H).py
  @Description  : 给定一个非负整数数组和一个整数 m，你需要将这个数组分成 m 个非空的连续子数组。设计一个算法使得这 m 个子数组各自和的最大值最小。

    注意:
    数组长度 n 满足以下条件:

    1 ≤ n ≤ 1000
    1 ≤ m ≤ min(50, n)
    示例:

    输入:
    nums = [7,2,5,10,8]
    m = 2

    输出:
    18

    解释:
    一共有四种方法将nums分割为2个子数组。
    其中最好的方式是将其分为[7,2,5] 和 [10,8]，
    因为此时这两个子数组各自的和的最大值为18，在所有情况中最小。
"""
from typing import List


class Solution:
    # 6280m,s 13.7MB
    @staticmethod
    def split_array(nums: List[int], m: int) -> int:
        n = len(nums)
        f = [[10 ** 18] * (m + 1) for _ in range(n + 1)]
        sub = [0]
        for elem in nums:
            sub.append(sub[-1] + elem)

        f[0][0] = 0
        for i in range(1, n + 1):
            for j in range(1, min(i, m) + 1):
                for k in range(i):
                    f[i][j] = min(f[i][j], max(f[k][j - 1], sub[i] - sub[k]))

        return f[n][m]

    # 48ms, 13.7MB
    @staticmethod
    def split_array_v2(nums: List[int], m: int) -> int:
        def check(x: int) -> bool:
            total, cnt = 0, 1
            for num in nums:
                if total + num > x:
                    cnt += 1
                    total = num
                else:
                    total += num
            return cnt <= m

        left = max(nums)
        right = sum(nums)
        while left < right:
            mid = (left + right) // 2
            if check(mid):
                right = mid
            else:
                left = mid + 1

        return left


if __name__ == '__main__':
    test_cases = [
        ([7, 2, 5, 10, 8], 2)
    ]
    for tc in test_cases:
        print(Solution.split_array(*tc))
        print(Solution.split_array_v2(*tc))
