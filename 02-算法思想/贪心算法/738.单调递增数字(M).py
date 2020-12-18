"""
  @Author       : liujianhan
  @Date         : 2020/12/15 13:58
  @Project      : leetcode_in_python
  @FileName     : 738.单调递增数字(M).py
  @Description  : 给定一个非负整数 N，找出小于或等于 N 的最大的整数，同时这个整数需要满足其各个位数上的数字是单调递增。
    （当且仅当每个相邻位数上的数字 x 和 y 满足 x <= y 时，我们称这个整数是单调递增的。）

    示例 1:
    输入: N = 10
    输出: 9

    示例 2:
    输入: N = 1234
    输出: 1234

    示例 3:
    输入: N = 332
    输出: 299
    说明: N 是在 [0, 10^9] 范围内的一个整数。
"""


class Solution:
    # 28ms, 14.5MB
    @staticmethod
    def monotone_increasing_digits(N: int) -> int:
        nums = list(str(N))
        length = len(nums)
        begin = 0
        is_result = True
        max_num = float('-inf')

        for i, num in enumerate(nums[1:], start=1):
            num = int(num)
            pre = int(nums[i-1])
            if pre > max_num:
                begin = i - 1
                max_num = pre
            if pre > num:
                is_result = False
                break

        nums[begin] = str(int(nums[begin]) - 1)
        for i in range(begin+1, length):
            nums[i] = '9'

        return N if is_result else int(''.join(nums))


if __name__ == '__main__':
    test_cases = [
        10, 1234, 332, 333
    ]
    for tc in test_cases:
        print(tc, Solution.monotone_increasing_digits(tc))
