"""
  @Author       : liujianhan
  @Date         : 2020/3/30 上午9:29
  @Project      : leetcode_in_python
  @FileName     : 62.圆圈中最后剩下的数字.py
  @Description  : 0,1,,n-1这n个数字排成一个圆圈，从数字0开始，每次从这个圆圈里删除第m个数字。求出这个圆圈里剩下的最后一个数字。
例如，0、1、2、3、4这5个数字组成一个圆圈，从数字0开始每次删除第3个数字，则删除的前4个数字依次是2、0、4、1，因此最后剩下的数字是3。
输入: n = 5, m = 3
输出: 3
输入: n = 10, m = 17
输出: 2
"""


class Solution:
    # 2172ms, 17.4MB
    @classmethod
    def last_remaining(cls, n: int, m: int) -> int:
        target_list, index = list(range(n)), 0
        while len(target_list) > 1:
            index = (index+m-1) % len(target_list)
            target_list.pop(index)

        return target_list[0]

    # 92ms, 13.6MB
    @classmethod
    def last_remaining_v2(cls, n: int, m: int) -> int:
        res = 0
        for i in range(2, n+1):
            res = (res + m) % i
        return res


if __name__ == '__main__':
    assert Solution.last_remaining(5, 3) == 3
    assert Solution.last_remaining(10, 17) == 2
    assert Solution.last_remaining_v2(5, 3) == 3
    assert Solution.last_remaining_v2(10, 17) == 2
