"""
  @Author       : Liujianhan
  @Date         : 20/4/4 19:40
  @FileName     : 003.无重复字符的最长子串(M).py
  @ProjectName  : leetcode_in_python
  @Description  : 给定一个字符串，请你找出其中不含有重复字符的最长子串的长度。
    输入: "abcabcbb"
    输出: 3
    解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
    输入: "bbbbb"
    输出: 1
    解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
    输入: "pwwkew"
    输出: 3
    解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
    请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。
 """


class Solution:
    # 96ms, 13.8MB
    @classmethod
    def length_of_longest_sub_string(cls, s: str) -> int:
        if not s:
            return 0
        lookup = list()
        max_len, cur_len = 0, 0
        for val in s:
            if val not in lookup:
                lookup.append(val)
                cur_len += 1
            else:
                lookup = lookup[lookup.index(val)+1:]
                lookup.append(val)
                cur_len = len(lookup)
            max_len = cur_len if cur_len > max_len else max_len

        return max_len

    # 528ms, 13.6MB
    @classmethod
    def length_of_longest_sub_string_v2(cls, s: str) -> int:
        if not s:
            return 0
        # 最大长度不会超过去重后的个数
        max_len = len(set(s))
        # 从最大长度逐渐缩小的长度索引去取子串，如果子串的集合长度和子串本身长度一样
        # 则是目标最大长度
        for width in range(max_len, 0, -1):
            for sub_index in range(len(s)):
                sub_string = s[sub_index: sub_index+width]
                # 子串的长度确保在width，少于这个长度就让width减小继续
                if len(sub_string) == len(set(sub_string)) and len(sub_string) == width:

                    return width


if __name__ == '__main__':
    test_cases = ['dvdf', 's', 'aab', 'abcabcbb', 'bbbbb', 'pwwkew', 'abcabcbbd']
    for tc in test_cases:
        print(tc, Solution.length_of_longest_sub_string(tc))
        print(tc, Solution.length_of_longest_sub_string_v2(tc))
        print()
