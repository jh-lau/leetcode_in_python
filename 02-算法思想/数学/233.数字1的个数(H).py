"""
  @Author       : Liujianhan
  @Date         : 20/7/5 17:39
  @FileName     : 233.数字1的个数(H).py
  @ProjectName  : leetcode_in_python
  @Description  : 给定一个整数 n，计算所有小于等于 n 的非负整数中数字 1 出现的个数。
    示例:
    输入: 13
    输出: 6
    解释: 数字 1 出现在以下数字中: 1, 10, 11, 12, 13 。
 """


class Solution:
    # 44ms, 13.7MB
    @staticmethod
    def count_digit_one(n: int) -> int:
        lens = len(str(n))
        count = 0
        for i in range(lens):
            digit = 10 ** i  # 当前位置所在的位(是十分位,百分位,还是千分位等)
            high = n // (digit * 10)  # 高于当前位的数字
            low = n % digit  # 低于当前位的数字
            cur = (n // digit) % 10  # 当前位置的数字
            if cur == 0:  # 当前位为0
                count += high * digit
            elif cur == 1:  # 当前为为1
                count += high * digit + low + 1
            else:  # 当前位大于1
                count += (high + 1) * digit
        return count


if __name__ == '__main__':
    print(Solution.count_digit_one(13))
