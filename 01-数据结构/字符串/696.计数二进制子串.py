"""
  @Author       : Liujianhan
  @Date         : 20/4/6 0:20
  @FileName     : 696.计数二进制子串.py
  @ProjectName  : leetcode_in_python
  @Description  : 给定一个字符串 s，计算具有相同数量0和1的非空(连续)子字符串的数量，并且这些子字符串中的所有0和所有1都是组合在一起的。
    重复出现的子串要计算它们出现的次数。
    示例 1 :
    输入: "00110011"
    输出: 6
    解释: 有6个子串具有相同数量的连续1和0：“0011”，“01”，“1100”，“10”，“0011” 和 “01”。
    请注意，一些重复出现的子串要计算它们出现的次数。
    另外，“00110011”不是有效的子串，因为所有的0（和1）没有组合在一起。
    示例 2 :
    输入: "10101"
    输出: 4
    解释: 有4个子串：“10”，“01”，“10”，“01”，它们具有相同数量的连续1和0。
    注意：
    s.length 在1到50,000之间。
    s 只包含“0”或“1”字符。
 """


class Solution:
    # 288ms, 14.1MB
    @classmethod
    def count_binary_substrings(cls, s: str) -> int:
        i, count, n = 0, 0, len(s)
        while i < n - 1:
            j = i + 1
            while j < n and s[j] == s[i]:
                j += 1
            k = j + 1
            le = j - i
            while k < n and s[k] == s[j] and k - j <= le:
                k += 1
            if j < n:
                count += min(j - i, k - j)
            i = j
        return count

    # 116ms, 15.2MB
    @classmethod
    def count_binary_substrings_v2(cls, s: str) -> int:
        l = list(map(len, s.replace('01', '0 1').replace('10', '1 0').split()))
        return sum(min(a, b) for a, b in zip(l, l[1:]))


if __name__ == '__main__':
    test_cases = ['00110011', '10101']
    for tc in test_cases:
        print(tc, Solution.count_binary_substrings(tc))
