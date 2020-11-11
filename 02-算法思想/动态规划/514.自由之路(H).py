"""
  @Author       : liujianhan
  @Date         : 2020/11/11 9:59
  @Project      : leetcode_in_python
  @FileName     : 514.自由之路(H).py
  @Description  : 视频游戏“辐射4”中，任务“通向自由”要求玩家到达名为“Freedom Trail Ring”的金属表盘，并使用表盘拼写特定关键词才能开门。
    给定一个字符串 ring，表示刻在外环上的编码；给定另一个字符串 key，表示需要拼写的关键词。您需要算出能够拼写关键词中所有字符的最少步数。
    最初，ring 的第一个字符与12:00方向对齐。您需要顺时针或逆时针旋转 ring 以使 key 的一个字符在 12:00 方向对齐，然后按下中心按钮，
    以此逐个拼写完 key 中的所有字符。旋转 ring 拼出 key 字符 key[i] 的阶段中：

    您可以将 ring 顺时针或逆时针旋转一个位置，计为1步。旋转的最终目的是将字符串 ring 的一个字符与 12:00 方向对齐，
    并且这个字符必须等于字符 key[i] 。如果字符 key[i] 已经对齐到12:00方向，您需要按下中心按钮进行拼写，
    这也将算作 1 步。按完之后，您可以开始拼写 key 的下一个字符（下一阶段）, 直至完成所有拼写。
    示例：
     
    输入: ring = "godding", key = "gd"
    输出: 4
    解释:
     对于 key 的第一个字符 'g'，已经在正确的位置, 我们只需要1步来拼写这个字符。
     对于 key 的第二个字符 'd'，我们需要逆时针旋转 ring "godding" 2步使它变成 "ddinggo"。
     当然, 我们还需要1步进行拼写。
     因此最终的输出是 4。
    提示：

    ring 和 key 的字符串长度取值范围均为 1 至 100；
    两个字符串中都只有小写字符，并且均可能存在重复字符；
    字符串 key 一定可以由字符串 ring 旋转拼出。
"""
import sys
from functools import lru_cache


class Solution:
    # 216ms, 15.1MB
    @staticmethod
    def find_rotate_steps(ring: str, key: str) -> int:
        @lru_cache(None)
        def dfs(ring, key, index):
            if index >= len(key):
                return 0

            res = 0
            # 找到所有能旋转的位置
            l_index = ring.find(key[index])

            min_val = []
            while l_index != -1:
                # 如果当前位置在字符串左半边，使用逆时针旋转 + 1 是拼写操作
                if l_index <= len(ring) // 2:
                    min_val.append(l_index + 1)
                else:
                    # 否则使用顺时针旋转
                    min_val.append(len(ring) - l_index + 1)
                # 获得旋转后的新表盘
                new_ring = ring[l_index:] + ring[:l_index]

                # 寻找下一个旋转点
                min_val[-1] += dfs(new_ring, key, index + 1)
                l_index = ring.find(key[index], l_index + 1)

            res = res + min(min_val) if min_val else 0
            return res

        return dfs(ring, key, 0)

    # 104ms, 13.5MB
    @staticmethod
    def find_rotate_steps_v2(ring: str, key: str) -> int:
        num = len(ring)
        char_pos = {}
        for i, char in enumerate(ring):
            if char in char_pos.keys():
                char_pos[char].append(i)
            else:
                char_pos[char] = [i]
        cur = [(n, 1) for n in char_pos[key[-1]]]
        key = ring[0] + key
        for i in range(len(key) - 2, -1, -1):
            prev = cur
            cur = []

            for j in char_pos[key[i]]:
                tmp = sys.maxsize
                for k in prev:
                    step = min(j - k[0], num - j + k[0]) if j > k[0] else min(k[0] - j, num + j - k[0])
                    step += k[1] + 1
                    if step < tmp:
                        tmp = step
                cur.append((j, tmp))
                if i == 0:
                    break

        return min([item[1] for item in cur]) - 1


if __name__ == '__main__':
    test_cases = [
        ('godding', 'gd'),
        ('abcde', 'ade')
    ]
    for tc in test_cases:
        print(Solution.find_rotate_steps(*tc))
        print(Solution.find_rotate_steps_v2(*tc))
