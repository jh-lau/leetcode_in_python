"""
  @Author       : Liujianhan
  @Date         : 20/5/30 22:00
  @FileName     : 187.重复的DNA序列(M).py
  @ProjectName  : leetcode_in_python
  @Description  : 所有 DNA 都由一系列缩写为 A，C，G 和 T 的核苷酸组成，例如：“ACGAATTCCG”。在研究 DNA 时，识别 DNA 中的重复序列有时会对研究非常有帮助。
    编写一个函数来查找目标子串，目标子串的长度为 10，且在 DNA 字符串 s 中出现次数超过一次。
    示例：
    输入：s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
    输出：["AAAAACCCCC", "CCCCCAAAAA"]
 """
from typing import List


class Solution:
    # 68ms, 25.3MB
    @classmethod
    def find_repeated_dna_sequences(cls, s: str) -> List[str]:
        L, n = 10, len(s)
        seen, output = set(), set()

        for start in range(n - L + 1):
            tmp = s[start:start + L]
            if tmp in seen:
                output.add(tmp[:])
            seen.add(tmp)

        return list(output)

    # 88ms, 25.2MB
    @classmethod
    def find_repeated_dna_sequences_v2(cls, s: str) -> List[str]:
        if len(s) < 10:
            return []
        tDict = {"A":0,"C":1,"G":2,"T":3}
        hash_map = {}
        h = 0
        sh = [tDict[s[i]] for i in range(len(s))]
        r = []
        for i in range(len(s)):
            if i < 10:
                h = h << 2 | sh[i]
                if i == 9:
                    hash_map[h] = 1
            else:
                h = h << 2 & 0xfffff | sh[i]
                hash_map[h] = hash_map.get(h,0) + 1
                if hash_map[h] > 1:
                    r.append(s[i - 9:i + 1])
                    hash_map[h] = -float('inf')
        return r


if __name__ == '__main__':
    print(Solution.find_repeated_dna_sequences('AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT'))
    print(Solution.find_repeated_dna_sequences_v2('AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT'))

