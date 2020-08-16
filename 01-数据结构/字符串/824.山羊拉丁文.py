"""
  @Author       : liujianhan
  @Date         : 2020/4/9 上午10:32
  @Project      : leetcode_in_python
  @FileName     : 824.山羊拉丁文.py
  @Description  : 给定一个由空格分割单词的句子 S。每个单词只包含大写或小写字母。
    我们要将句子转换为 “Goat Latin”（一种类似于 猪拉丁文 - Pig Latin 的虚构语言）。
    山羊拉丁文的规则如下：
    如果单词以元音开头（a, e, i, o, u），在单词后添加"ma"。
    例如，单词"apple"变为"applema"。
    如果单词以辅音字母开头（即非元音字母），移除第一个字符并将它放到末尾，之后再添加"ma"。
    例如，单词"goat"变为"oatgma"。
    根据单词在句子中的索引，在单词最后添加与索引相同数量的字母'a'，索引从1开始。
    例如，在第一个单词后添加"a"，在第二个单词后添加"aa"，以此类推。
    返回将 S 转换为山羊拉丁文后的句子。

    示例 1:

    输入: "I speak Goat Latin"
    输出: "Imaa peaksmaaa oatGmaaaa atinLmaaaaa"

    示例 2:

    输入: "The quick brown fox jumped over the lazy dog"
    输出: "heTmaa uickqmaaa rownbmaaaa oxfmaaaaa umpedjmaaaaaa overmaaaaaaa hetmaaaaaaaa azylmaaaaaaaaa ogdmaaaaaaaaaa"
    说明:
    S 中仅包含大小写字母和空格。单词间有且仅有一个空格。
    1 <= S.length <= 150。
"""


class Solution:
    # 44ms, 13.8MB
    @classmethod
    def to_goat_latin(cls, s: str) -> str:
        vowel_str = 'aeiouAEIOU'
        word_list = s.split()
        for i, word in enumerate(word_list):
            suffix = f'ma{(i + 1) * "a"}'
            if word[0] in vowel_str:
                word_list[i] = f'{word}{suffix}'
            else:
                word_list[i] = f'{word[1:]}{word[0]}{suffix}'

        return ' '.join(word_list)

    # 64ms, 13.7MB
    @classmethod
    def to_goat_latin_v2(cls, s: str) -> str:
        res = []
        vowel_str = 'aeiouAEIOU'
        for i, word in enumerate(s.split()):
            if word[0] not in vowel_str:
                word = (word + word[0])[1:]
            res.append(f'{word}ma{(i + 1) * "a"}')

        return ' '.join(res)


if __name__ == '__main__':
    test_cases = ["I speak Goat Latin", "The quick brown fox jumped over the lazy dog"]
    for tc in test_cases:
        print(Solution.to_goat_latin(tc))
        print(Solution.to_goat_latin_v2(tc))
