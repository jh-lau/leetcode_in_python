"""
  @Author       : Liujianhan
  @Date         : 20/4/19 21:07
  @FileName     : 466.统计重复个数(H).py
  @ProjectName  : leetcode_in_python
  @Description  : 由 n 个连接的字符串 s 组成字符串 S，记作 S = [s,n]。例如，["abc",3]=“abcabcabc”。
    如果我们可以从 s2 中删除某些字符使其变为 s1，则称字符串 s1 可以从字符串 s2 获得。例如，根据定义，"abc" 可以从 “abdbec” 获得，但不能从 “acbbe” 获得。
    现在给你两个非空字符串 s1 和 s2（每个最多 100 个字符长）和两个整数 0 ≤ n1 ≤ 106 和 1 ≤ n2 ≤ 106。现在考虑字符串 S1 和 S2，其中 S1=[s1,n1] 、S2=[s2,n2] 。
    请你找出一个可以满足使[S2,M] 从 S1 获得的最大整数 M 。
    示例：

    输入：
    s1 ="acb",n1 = 4
    s2 ="ab",n2 = 2

    返回：
    2
 """


class Solution:
    # 44ms, 13.7MB
    @classmethod
    def get_max_repetitions(cls, s1: str, n1: int, s2: str, n2: int) -> int:
        if n1 == 0:
            return 0
        s1cnt, index, s2cnt = 0, 0, 0
        recall = dict()
        while True:
            s1cnt += 1
            for ch in s1:
                if ch == s2[index]:
                    index += 1
                    if index == len(s2):
                        s2cnt, index = s2cnt + 1, 0
            if s1cnt == n1:
                return s2cnt // n2
            if index in recall:
                s1cnt_prime, s2cnt_prime = recall[index]
                pre_loop = (s1cnt_prime, s2cnt_prime)
                in_loop = (s1cnt - s1cnt_prime, s2cnt - s2cnt_prime)
                break
            else:
                recall[index] = (s1cnt, s2cnt)

        ans = pre_loop[1] + (n1 - pre_loop[0]) // in_loop[0] * in_loop[1]
        rest = (n1 - pre_loop[0]) % in_loop[0]
        for i in range(rest):
            for ch in s1:
                if ch == s2[index]:
                    index += 1
                    if index == len(s2):
                        ans, index = ans + 1, 0
        return ans // n2


if __name__ == '__main__':
    test_cases = [
        ('acb', 4, 'ab', 2)
    ]
    for tc in test_cases:
        print(Solution.get_max_repetitions(*tc))