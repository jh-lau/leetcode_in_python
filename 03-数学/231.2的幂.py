"""
  @Author       : Liujianhan
  @Date         : 20/3/22 21:18
  @FileName     : 231.2的幂.py
  @ProjectName  : leetcode_in_python
  @Description  : 给定一个整数，编写一个函数来判断它是否是 2 的幂次方。
 """


class Solution:
    # 32ms, 13.5MB
    @classmethod
    def is_power_of_two(cls, n: int) -> bool:
        return n > 0 and n & (n - 1) == 0

    # 48ms, 13.5MB
    @classmethod
    def is_power_of_two_v2(cls, n: int) -> bool:
        if n < 0:
            return False
        if n == 1:
            return True
        temp = str(bin(n))
        return True if temp[2] == '1' and int(temp[3:]) == 0 else False


if __name__ == '__main__':
    test = [1, 16, 218, 1024]
    for t in test:
        # print(t, Solution.is_power_of_two(t))
        print(t, Solution.is_power_of_two_v2(t))
