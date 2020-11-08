"""
  @Author       : liujianhan
  @Date         : 20/11/8 21:08
  @Project      : leetcode_in_python
  @FileName     : 409.最长回文串.py
  @Description  : 给定一个包含大写字母和小写字母的字符串，找到通过这些字母构造成的最长的回文串。
    在构造过程中，请注意区分大小写。比如 "Aa" 不能当做一个回文字符串。
    注意:
    假设字符串的长度不会超过 1010。
    示例 1:
    输入:
    "abccccdd"
    输出:
    7
    解释:
    我们可以构造的最长的回文串是"dccaccd", 它的长度是 7。
"""
from collections import defaultdict


class Solution:
    # 40ms, 13.4MB
    @staticmethod
    def longest_palindrome(s: str) -> int:
        lookup = defaultdict(int)
        for char in s:
            lookup[char] += 1

        result = 0
        odd_flag = False
        for k, v in lookup.items():
            if not v % 2:
                result += v
            else:
                odd_flag = True
                result += v - 1
        return result + int(odd_flag)


if __name__ == '__main__':
    test_cases = [
        'abccccdd',
        'bb',
        'civilwartestingwhetherthatnaptionoranynartionsoconceivedandsodedicatedcanlongendureWeareqmetonagreatbattlefiemldoftzhatwarWehavecometodedicpateaportionofthatfieldasafinalrestingplaceforthosewhoheregavetheirlivesthatthatnationmightliveItisaltogetherfangandproperthatweshoulddothisButinalargersensewecannotdedicatewecannotconsecratewecannothallowthisgroundThebravelmenlivinganddeadwhostruggledherehaveconsecrateditfaraboveourpoorponwertoaddordetractTgheworldadswfilllittlenotlenorlongrememberwhatwesayherebutitcanneverforgetwhattheydidhereItisforusthelivingrathertobededicatedheretotheulnfinishedworkwhichtheywhofoughtherehavethusfarsonoblyadvancedItisratherforustobeherededicatedtothegreattdafskremainingbeforeusthatfromthesehonoreddeadwetakeincreaseddevotiontothatcauseforwhichtheygavethelastpfullmeasureofdevotionthatweherehighlyresolvethatthesedeadshallnothavediedinvainthatthisnationunsderGodshallhaveanewbirthoffreedomandthatgovernmentofthepeoplebythepeopleforthepeopleshallnotperishfromtheearth'
    ]
    for tc in test_cases:
        print(Solution.longest_palindrome(tc))
