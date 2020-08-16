"""
  @Author       : Liujianhan
  @Date         : 20/8/1 20:30
  @FileName     : 632.最小区间(H).py
  @ProjectName  : leetcode_in_python
  @Description  : 你有 k 个升序排列的整数数组。找到一个最小区间，使得 k 个列表中的每个列表至少有一个数包含在其中。

    我们定义如果 b-a < d-c 或者在 b-a == d-c 时 a < c，则区间 [a,b] 比 [c,d] 小。

    示例 1:

    输入:[[4,10,15,24,26], [0,9,12,20], [5,18,22,30]]
    输出: [20,24]
    解释:
    列表 1：[4, 10, 15, 24, 26]，24 在区间 [20,24] 中。
    列表 2：[0, 9, 12, 20]，20 在区间 [20,24] 中。
    列表 3：[5, 18, 22, 30]，22 在区间 [20,24] 中。
    注意:

    给定的列表可能包含重复元素，所以在这里升序表示 >= 。
    1 <= k <= 3500
    -105 <= 元素的值 <= 105
    对于使用Java的用户，请注意传入类型已修改为List<List<Integer>>。重置代码模板后可以看到这项改动。
 """
from collections import defaultdict
from typing import List


class Solution:
    # 996ms, 19.7MB
    @staticmethod
    def smallest_range(nums: List[List[int]]) -> List[int]:
        n = len(nums)
        indices = defaultdict(list)
        _min, _max = 10 ** 9, -10 ** 9
        for i, vec in enumerate(nums):
            for x in vec:
                indices[x].append(i)
            _min = min(_min, *vec)
            _max = max(_max, *vec)

        freq = [0] * n
        inside = 0
        left, right = _min, _min - 1
        best_left, best_right = _min, _max

        while right < _max:
            right += 1
            if right in indices:
                for x in indices[right]:
                    freq[x] += 1
                    if freq[x] == 1:
                        inside += 1
                while inside == n:
                    if right - left < best_right - best_left:
                        best_left, best_right = left, right
                    if left in indices:
                        for x in indices[left]:
                            freq[x] -= 1
                            if freq[x] == 0:
                                inside -= 1
                    left += 1

        return [best_left, best_right]

    # 248ms, 21MB
    @staticmethod
    def smallest_range_v2(nums: List[List[int]]) -> List[int]:
        L = sorted([(a, r) for r in range(len(nums)) for a in set(nums[r])])
        ans = [L[0][0], L[-1][0]]
        count0, count1 = [0] * len(nums), len(nums)
        i = 0
        for j in range(len(L)):
            if 0 == count0[L[j][1]]: count1 -= 1
            count0[L[j][1]] += 1
            if 0 == count1:
                while i < j:
                    count0[L[i][1]] -= 1
                    if 0 == count0[L[i][1]]:
                        count1 += 1
                        if (L[j][0] - L[i][0]) < (ans[1] - ans[0]):
                            ans = [L[i][0], L[j][0]]
                        i += 1
                        break
                    else:
                        i += 1
        return ans


if __name__ == '__main__':
    test_cases = [
        [[4, 10, 15, 24, 26], [0, 9, 12, 20], [5, 18, 22, 30]]
    ]
    for tc in test_cases:
        print(Solution.smallest_range(tc))
        print(Solution.smallest_range_v2(tc))
