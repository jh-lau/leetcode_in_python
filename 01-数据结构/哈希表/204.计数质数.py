"""
  @Author       : liujianhan
  @Date         : 2020/4/22 下午2:48
  @Project      : leetcode_in_python
  @FileName     : 204.计数质数.py
  @Description  : 统计所有小于非负整数 n 的质数的数量。
    示例:
    输入: 10
    输出: 4
    解释: 小于 10 的质数一共有 4 个, 它们是 2, 3, 5, 7 。
"""


class Solution:
    # 120ms, 36.8MB
    @classmethod
    def count_primes(cls, n: int) -> int:
        if n < 2:
            return 0
        is_prime = [1] * n
        is_prime[0] = is_prime[1] = 0

        for i in range(2, int(n ** .5) + 1):
            if is_prime[i]:
                is_prime[i * i:n:i] = [0] * ((n - 1 - i * i) // i + 1)

        return sum(is_prime)


if __name__ == '__main__':
    test_cases = [
        10, 13
    ]
    for tc in test_cases:
        print(Solution.count_primes(tc))
