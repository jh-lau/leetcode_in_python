"""
  @Author       : liujianhan
  @Date         : 21/2/26 10:11
  @Project      : leetcode_in_python
  @FileName     : 1178.猜字谜(H).py
  @Description  : 外国友人仿照中国字谜设计了一个英文版猜字谜小游戏，请你来猜猜看吧。
    字谜的迷面 puzzle 按字符串形式给出，如果一个单词 word 符合下面两个条件，那么它就可以算作谜底：
    单词 word 中包含谜面 puzzle 的第一个字母。
    单词 word 中的每一个字母都可以在谜面 puzzle 中找到。
    例如，如果字谜的谜面是 "abcdefg"，那么可以作为谜底的单词有 "faced", "cabbage", 和 "baggage"；而 "beefed"（不含字母 "a"）
    以及 "based"（其中的 "s" 没有出现在谜面中）。
    返回一个答案数组 answer，数组中的每个元素 answer[i] 是在给出的单词列表 words 中可以作为字谜迷面 puzzles[i] 所对应的谜底的单词数目。

    示例：
    输入：
    words = ["aaaa","asas","able","ability","actt","actor","access"],
    puzzles = ["aboveyz","abrodyz","abslute","absoryz","actresz","gaswxyz"]
    输出：[1,1,3,2,4,0]
    解释：
    1 个单词可以作为 "aboveyz" 的谜底 : "aaaa"
    1 个单词可以作为 "abrodyz" 的谜底 : "aaaa"
    3 个单词可以作为 "abslute" 的谜底 : "aaaa", "asas", "able"
    2 个单词可以作为 "absoryz" 的谜底 : "aaaa", "asas"
    4 个单词可以作为 "actresz" 的谜底 : "aaaa", "asas", "actt", "access"
    没有单词可以作为 "gaswxyz" 的谜底，因为列表中的单词都不含字母 'g'。
    提示：
    1 <= words.length <= 10^5
    4 <= words[i].length <= 50
    1 <= puzzles.length <= 10^4
    puzzles[i].length == 7
    words[i][j], puzzles[i][j] 都是小写英文字母。
    每个 puzzles[i] 所包含的字符都不重复。
"""
from typing import List


class Solution:
    @staticmethod
    def get_mask(word):
        mask = 0
        for c in word:
            mask |= 1 << (ord(c) - ord('a'))
        return mask

    # 520ms, 31MB
    def find_num_of_valid_words(self, words: List[str], puzzles: List[str]) -> List[int]:
        words = [self.get_mask(w) for w in words]
        d = {}
        for w in words:
            d[w] = d.get(w, 0) + 1

        ans = []
        for p in puzzles:
            mask = self.get_mask(p)
            sub_mask = mask
            head_mask = 1 << (ord(p[0]) - ord('a'))
            cnt = 0
            while sub_mask:
                if sub_mask & head_mask:
                    cnt += d.get(sub_mask, 0)
                sub_mask = (sub_mask - 1) & mask
            ans.append(cnt)
        return ans


if __name__ == '__main__':
    test_cases = [
        (["aaaa", "asas", "able", "ability", "actt", "actor", "access"],
         ["aboveyz", "abrodyz", "abslute", "absoryz", "actresz", "gaswxyz"])
    ]
    for test_case in test_cases:
        print(Solution().find_num_of_valid_words(*test_case))
