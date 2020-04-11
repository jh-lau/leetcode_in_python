"""
  @Author       : liujianhan
  @Date         : 2020/4/10 上午9:22
  @Project      : leetcode_in_python
  @FileName     : 893.特殊等价字符串组.py
  @Description  : 你将得到一个字符串数组 A。
    如果经过任意次数的移动，S == T，那么两个字符串 S 和 T 是特殊等价的。
    一次移动包括选择两个索引 i 和 j，且 i ％ 2 == j ％ 2，交换 S[j] 和 S [i]。
    现在规定，A 中的特殊等价字符串组是 A 的非空子集 S，这样不在 S 中的任何字符串与 S 中的任何字符串都不是特殊等价的。
    返回 A 中特殊等价字符串组的数量。
    (有个数组, 元素是 字符串字符串中的字符 两两交换 , 交换的字符 索引 满足i ％ 2 == j ％ 2, 就是说 奇跟奇, 偶跟偶 交换
    不管交换多少次, 只要 字符串交换后 有和 另一个字符串交换 后 相同, 就为等价的把这些等价的字符串归为 一个数组中求有多少个这样的数组)
    示例 1：

    输入：["a","b","c","a","c","c"]
    输出：3
    解释：3 组 ["a","a"]，["b"]，["c","c","c"]
    示例 2：

    输入：["aa","bb","ab","ba"]
    输出：4
    解释：4 组 ["aa"]，["bb"]，["ab"]，["ba"]
    示例 3：

    输入：["abc","acb","bac","bca","cab","cba"]
    输出：3
    解释：3 组 ["abc","cba"]，["acb","bca"]，["bac","cab"]
    示例 4：

    输入：["abcd","cdab","adcb","cbad"]
    输出：1
    解释：1 组 ["abcd","cdab","adcb","cbad"]
    提示：

    1 <= A.length <= 1000
    1 <= A[i].length <= 20
    所有 A[i] 都具有相同的长度。
    所有 A[i] 都只由小写字母组成。
"""
from typing import List


class Solution:
    # 60ms, 13.8MB
    @classmethod
    def num_special_equiv_groups(cls, str_list: List[str]) -> int:
        res = set()
        for sub in str_list:
            sub = ''.join(sorted(sub[::2]) + sorted(sub[1::2]))
            res.add(sub)
        return len(res)


if __name__ == '__main__':
    test_cases = [
        ["abcd", "cdab", "adcb", "cbad"],
        ["abc", "acb", "bac", "bca", "cab", "cba"],
        ["aa", "bb", "ab", "ba"],
        ["a", "b", "c", "a", "c", "c"]
    ]
    for tc in test_cases:
        print(Solution.num_special_equiv_groups(tc))
