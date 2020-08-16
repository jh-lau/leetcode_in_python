"""
  @Author       : Liujianhan
  @Date         : 20/6/2 22:40
  @FileName     : 64.求1+2+..+n(M).py
  @ProjectName  : leetcode_in_python
  @Description  : 求 1+2+...+n ，要求不能使用乘除法、for、while、if、else、switch、case等关键字及条件判断语句（A?B:C）。
    示例 1：
    输入: n = 3
    输出: 6
    示例 2：
    输入: n = 9
    输出: 45
    限制：
    1 <= n <= 10000
 """


class Solution:
    # 60ms, 21.4MB
    @classmethod
    def sum_nums(cls, n: int) -> int:
        if n > 1:
            return cls.sum_nums(n-1) + n
        return 1


if __name__ == '__main__':
    test_cases = [
        3, 9
    ]
    for tc in test_cases:
        print(Solution.sum_nums(tc))

