"""
  @Author       : Liujianhan
  @Date         : 20/4/25 16:41
  @FileName     : 050.Pow(x,n)(M).py
  @ProjectName  : leetcode_in_python
  @Description  : 实现 pow(x, n) ，即计算 x 的 n 次幂函数。

示例 1:

输入: 2.00000, 10
输出: 1024.00000
示例 2:

输入: 2.10000, 3
输出: 9.26100
示例 3:

输入: 2.00000, -2
输出: 0.25000
解释: 2-2 = 1/22 = 1/4 = 0.25
说明:

-100.0 < x < 100.0
n 是 32 位有符号整数，其数值范围是 [−231, 231 − 1] 。
 """


class Solution:
    # 40ms, 13.7MB
    @classmethod
    def my_pow(cls, x: float, n: int) -> float:
        def re_binary_search(x, n):  # 逆向二分查找
            # 递归出口
            if n < 1:
                return 1
            count, sum = 1, x  # 初始化
            # 二分查找
            while count * 2 <= n:
                count += count  # 计数器翻倍
                sum *= sum  # 累乘
            return re_binary_search(x, n - count) * sum  # 返回累乘结果

        res = re_binary_search(abs(x), abs(n))  # 调用二分查找，传入绝对值
        # 符号处理
        res = -res if x < 0 and n % 2 != 0 else res
        res = 1 / res if n < 0 else res

        return res


if __name__ == '__main__':
    test_cases = [
        (2.10000, 3),
        (2.00000, -2),
        (2.00000, 10)
    ]
    for tc in test_cases:
        print(Solution.my_pow(*tc))
