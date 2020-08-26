"""
  @Author       : liujianhan
  @Date         : 2020/8/26 19:51
  @Project      : leetcode_in_python
  @FileName     : 313.超级丑数(M).py
  @Description  : 编写一段程序来查找第 n 个超级丑数。

    超级丑数是指其所有质因数都是长度为 k 的质数列表 primes 中的正整数。

    示例:

    输入: n = 12, primes = [2,7,13,19]
    输出: 32
    解释: 给定长度为 4 的质数列表 primes = [2,7,13,19]，前 12 个超级丑数序列为：[1,2,4,7,8,13,14,16,19,26,28,32] 。
    说明:

    1 是任何给定 primes 的超级丑数。
     给定 primes 中的数字以升序排列。
    0 < k ≤ 100, 0 < n ≤ 106, 0 < primes[i] < 1000 。
    第 n 个超级丑数确保在 32 位有符整数范围内。
"""
from typing import List


class Solution:
    # 1084ms, 17.7MB
    @staticmethod
    def nth_super_ugly_number(n: int, primes: List[int]) -> int:
        dp = [1]  # 超级丑数列表
        idx = [0] * len(primes)  # 质数因子的指针列表，初始都指向0，即dp[0]
        plen = len(primes)  #
        while n > 1:  # 添加了n-1个超级丑数，停止
            # 取出质数列表中的每个质数与各自指针对应的超级丑数相乘的最小值
            min_ = min([dp[idx[i]] * primes[i] for i in range(plen)])
            for i in range(plen):
                # 若最小值等于该质数乘以dp[idx[i]]（第i个质数的指针所对应的超级丑数）
                # 则对应指针往后移动一步，i+1
                if min_ == dp[idx[i]] * primes[i]:
                    idx[i] += 1
            n -= 1
            dp.append(min_)
        return dp[-1]


if __name__ == '__main__':
    test_cases = [
        (12, [2,7,13,19])
    ]
    for tc in test_cases:
        print(Solution.nth_super_ugly_number(*tc))
