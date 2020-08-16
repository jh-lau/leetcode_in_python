"""
  @Author       : liujianhan
  @Date         : 2020/4/13 上午11:30
  @Project      : leetcode_in_python
  @FileName     : 202.快乐数.py
  @Description  : 编写一个算法来判断一个数 n 是不是快乐数。
    「快乐数」定义为：对于一个正整数，每一次将该数替换为它每个位置上的数字的平方和，然后重复这个过程直到这个数变为 1，也可能是
    无限循环 但始终变不到 1。如果 可以变为  1，那么这个数就是快乐数。
    如果 n 是快乐数就返回 True ；不是，则返回 False 。
    示例：

    输入：19
    输出：true
    解释：
    1^2 + 9^2 = 82
    8^2 + 2^2 = 68
    6^2 + 8^2 = 100
    1^2 + 0^2 + 0^2 = 1
"""


class Solution:
    # 56ms, 13.7MB
    @classmethod
    def is_happy(cls, n: int) -> bool:
        def get_next(n):
            total_sum = 0
            while n > 0:
                n, digit = divmod(n, 10)
                total_sum += digit ** 2
            return total_sum

        seen = set()
        while n != 1 and n not in seen:
            seen.add(n)
            n = get_next(n)

        return n == 1

    # 44ms, 13.6MB
    @classmethod
    def is_happy_v2(cls, n: int) -> bool:
        seen = set()
        while n not in seen:
            seen.add(n)
            n = sum([int(x)**2 for x in str(n)])
            if n == 1:
                return True

        return False


if __name__ == '__main__':
    print(Solution.is_happy(19))
    print(Solution.is_happy_v2(19))
