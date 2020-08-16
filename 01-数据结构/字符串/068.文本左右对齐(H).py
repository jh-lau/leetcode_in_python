"""
  @Author       : Liujianhan
  @Date         : 20/5/3 19:39
  @FileName     : 068.文本左右对齐(H).py
  @ProjectName  : leetcode_in_python
  @Description  : 给定一个单词数组和一个长度 maxWidth，重新排版单词，使其成为每行恰好有 maxWidth 个字符，且左右两端对齐的文本。
    你应该使用“贪心算法”来放置给定的单词；也就是说，尽可能多地往每行中放置单词。必要时可用空格 ' ' 填充，使得每行恰好有 maxWidth 个字符。
    要求尽可能均匀分配单词间的空格数量。如果某一行单词间的空格不能均匀分配，则左侧放置的空格数要多于右侧的空格数。
    文本的最后一行应为左对齐，且单词之间不插入额外的空格。
    说明:
    单词是指由非空格字符组成的字符序列。
    每个单词的长度大于 0，小于等于 maxWidth。
    输入单词数组 words 至少包含一个单词。
    示例:
    输入:
    words = ["This", "is", "an", "example", "of", "text", "justification."]
    maxWidth = 16
    输出:
    [
       "This    is    an",
       "example  of text",
       "justification.  "
    ]
    示例 2:
    输入:
    words = ["What","must","be","acknowledgment","shall","be"]
    maxWidth = 16
    输出:
    [
      "What   must   be",
      "acknowledgment  ",
      "shall be        "
    ]
    解释: 注意最后一行的格式应为 "shall be    " 而不是 "shall     be",
         因为最后一行应为左对齐，而不是左右两端对齐。
         第二行同样为左对齐，这是因为这行只包含一个单词。
    示例 3:
    输入:
    words = ["Science","is","what","we","understand","well","enough","to","explain",
             "to","a","computer.","Art","is","everything","else","we","do"]
    maxWidth = 20
    输出:
    [
      "Science  is  what we",
      "understand      well",
      "enough to explain to",
      "a  computer.  Art is",
      "everything  else  we",
      "do                  "
    ]
 """
from pprint import pprint
from typing import List


class Solution:
    # 36ms, 13.8MB
    @classmethod
    def full_justify(cls, words: List[str], max_width: int) -> List[str]:
        ans = []  # 最后的答案
        cur_c = 0  # 当前行的字母数
        cur_w = 0  # 当前行的单词数
        wl = []  # 当前行的单词列表
        for i, wd in enumerate(words):
            l = len(wd)
            if cur_c + l + cur_w > max_width:  # 加上这个单词是否会超过最大长度
                if cur_w == 1:  # 当前行仅有一个超长的单词，后面全部补空格
                    ans.append(wl[0] + ' ' * (max_width - cur_c))
                else:
                    left = max_width - cur_c  # 这行一共有几个空格
                    if left % (cur_w - 1) == 0:  # 空格刚好平均分配
                        ans.append((' ' * (left // (cur_w - 1))).join(wl))
                    else:  # 空格不能平均分配
                        x = left % (cur_w - 1)  # 多余的空格
                        b = left // (cur_w - 1)  # 平均每个间隔最少的空格数
                        cans = wl[0]
                        for i in range(x):  # 前 x 个间隔空 b + 1 个
                            cans += ' ' * (b + 1) + wl[i + 1]
                        for i in range(x + 1, len(wl)):  # 后面的都空 b 个
                            cans += ' ' * b + wl[i]
                        ans.append(cans)
                cur_c = l
                cur_w = 1
                wl = [wd]
            else:
                cur_c += l
                cur_w += 1
                wl.append(wd)

        if cur_w > 0:  # 所有单词过完了把余下的词放入最后一行
            cans = ' '.join(wl)
            cans += ' ' * (max_width - len(cans))
            ans.append(cans)
        return ans


if __name__ == '__main__':
    pprint(Solution.full_justify(
        *(["Science", "is", "what", "we", "understand", "well", "enough", "to", "explain", "to", "a", "computer.", "Art", "is", "everything", "else", "we", "do"], 20)
    ))
