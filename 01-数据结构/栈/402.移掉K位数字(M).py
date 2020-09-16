"""
  @Author       : liujianhan
  @Date         : 2020/9/16 9:37
  @Project      : leetcode_in_python
  @FileName     : 402.移掉K位数字(M).py
  @Description  : 给定一个以字符串表示的非负整数 num，移除这个数中的 k 位数字，使得剩下的数字最小。
    注意:
    num 的长度小于 10002 且 ≥ k。
    num 不会包含任何前导零。
    示例 1 :

    输入: num = "1432219", k = 3
    输出: "1219"
    解释: 移除掉三个数字 4, 3, 和 2 形成一个新的最小的数字 1219。
    示例 2 :

    输入: num = "10200", k = 1
    输出: "200"
    解释: 移掉首位的 1 剩下的数字为 200. 注意输出不能有任何前导零。
    示例 3 :

    输入: num = "10", k = 2
    输出: "0"
    解释: 从原数字移除所有的数字，剩余为空就是0。

    解析：https://leetcode-cn.com/problems/remove-k-digits/solution/yi-zhao-chi-bian-li-kou-si-dao-ti-ma-ma-zai-ye-b-5/
    核心：遍历逐个数字与其左边的数相比，如果左边数更大，则移除该左边的数
"""


class Solution:
    # 44ms, 13.5MB
    @staticmethod
    def remove_k_digits(num: str, k: int) -> str:
        stack = []
        remain = len(num) - k
        for d in num:
            while k and stack and stack[-1] > d:
                stack.pop()
                k -= 1
            stack.append(d)
        return ''.join(stack[:remain]).lstrip('0') or '0'


if __name__ == '__main__':
    test_cases = [
        ('1432219', 3),
        ('10200', 1),
        ('10', 2)
    ]
    for tc in test_cases:
        print(Solution.remove_k_digits(*tc))
