"""
  @Author       : liujianhan
  @Date         : 2020/12/8 上午11:20
  @Project      : leetcode_in_python
  @FileName     : 842.将数组拆分成斐波那契序列(M).py
  @Description  : 给定一个数字字符串 S，比如 S = "123456579"，我们可以将它分成斐波那契式的序列 [123, 456, 579]。
    形式上，斐波那契式序列是一个非负整数列表 F，且满足：
    0 <= F[i] <= 2^31 - 1，（也就是说，每个整数都符合 32 位有符号整数类型）；
    F.length >= 3；
    对于所有的0 <= i < F.length - 2，都有 F[i] + F[i+1] = F[i+2] 成立。
    另外，请注意，将字符串拆分成小块时，每个块的数字一定不要以零开头，除非这个块是数字 0 本身。
    返回从 S 拆分出来的任意一组斐波那契式的序列块，如果不能拆分则返回 []。

    示例 1：
    输入："123456579"
    输出：[123,456,579]
    示例 2：

    输入: "11235813"
    输出: [1,1,2,3,5,8,13]
    示例 3：

    输入: "112358130"
    输出: []
    解释: 这项任务无法完成。
    示例 4：

    输入："0123"
    输出：[]
    解释：每个块的数字不能以零开头，因此 "01"，"2"，"3" 不是有效答案。
    示例 5：

    输入: "1101111"
    输出: [110, 1, 111]
    解释: 输出 [11,0,11,11] 也同样被接受。

    提示：

    1 <= S.length <= 200
    字符串 S 中只含有数字。
"""
from typing import List


class Solution:
    # 64ms, 13.5MB
    @staticmethod
    def split_into_fibonacci(S: str) -> List[int]:
        n, up = len(S), 2147483647

        def get_list(start):
            # 判断前面两个数会不会超过上限
            if max(li) > up:
                return False

            # 遍历后面所有的字符串看看能不能组成斐波那契，
            # 如果 数超上限 或 最后一个数超字符串长度 或 字符串并不是下一个数 则直接跳出
            while start < n:
                now = li[-1] + li[-2]
                c = len(str(now))
                if now > up or start + c > n or int(S[start:start + c]) != now:
                    return False
                li.append(now)
                start += c
            return True

        for i in range(1, 11):
            # 这里让j取不到字符串末尾最后一位，顺便如果两个字符串有个是0开始的，直接只跑0的情况
            for j in range(1, min(11, n - i)):
                li = [int(S[:i]), int(S[i:i + j])]
                if get_list(i + j):
                    return li
                if S[i] == '0':
                    break
            if S[0] == '0':
                break
        return []


if __name__ == '__main__':
    test_cases = [
        '123456579', '11235813', '112358130', '0123', '1101111'
    ]
    for tc in test_cases:
        print(Solution.split_into_fibonacci(tc))
