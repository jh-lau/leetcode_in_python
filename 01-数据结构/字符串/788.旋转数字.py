"""
  @Author       : liujianhan
  @Date         : 2020/4/8 下午6:59
  @Project      : leetcode_in_python
  @FileName     : 788.旋转数字.py
  @Description  : 我们称一个数 X 为好数, 如果它的每位数字逐个地被旋转 180 度后，我们仍可以得到一个有效的，且和 X 不同的数。
    要求每位数字都要被旋转。
    如果一个数的每位数字被旋转以后仍然还是一个数字， 则这个数是有效的。0, 1, 和 8 被旋转后仍然是它们自己；2 和 5 可以互相旋转成对方
    （在这种情况下，它们以不同的方向旋转，换句话说，2 和 5 互为镜像）；6 和 9 同理，除了这些以外其他的数字旋转以后都不再是有效的数字。
    现在我们有一个正整数 N, 计算从 1 到 N 中有多少个数 X 是好数？
    示例：

    输入: 10
    输出: 4
    解释:
    在[1, 10]中有四个好数： 2, 5, 6, 9。
    注意 1 和 10 不是好数, 因为他们在旋转之后不变。
     
    提示：
    N 的取值范围是 [1, 10000]。
"""


class Solution:
    # 88ms, 13.8MB
    @classmethod
    def rotate_digits(cls, n: int) -> int:
        ans, d = 0, [0] * (n + 1)
        d[:10] = [0, 0, 1, -1, -1, 1, 1, -1, 0, 1]
        for i in range(n + 1):
            d[i] = -1 in (d[i // 10], d[i % 10]) and -1 or d[i // 10] | d[i % 10]
            ans += d[i] == 1

        return ans

    # 44ms, 13.6MB
    @classmethod
    def rotate_digits_v2(cls, n: int) -> int:
        n_list = list(map(int, str(n)))

        memo = {}

        def dp(i, equality_flag, involution_flag):
            if i == len(n_list): return involution_flag
            if (i, equality_flag, involution_flag) not in memo:
                ans = 0
                for d in range(n_list[i] + 1 if equality_flag else 10):
                    if d in {3, 4, 7}: continue
                    ans += dp(i + 1, equality_flag and d == n_list[i],
                              involution_flag or d in {2, 5, 6, 9})
                memo[i, equality_flag, involution_flag] = ans
            return memo[i, equality_flag, involution_flag]

        return dp(0, True, False)


if __name__ == '__main__':
    test_cases = [10, 30, 51]
    for tc in test_cases:
        print(Solution.rotate_digits(tc))
        print(Solution.rotate_digits_v2(tc))
