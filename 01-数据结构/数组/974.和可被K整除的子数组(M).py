"""
  @Author       : liujianhan
  @Date         : 2020/5/27 上午11:34
  @Project      : leetcode_in_python
  @FileName     : 974.和可被K整除的子数组(M).py
  @Description  : 给定一个整数数组 A，返回其中元素之和可被 K 整除的（连续、非空）子数组的数目。
    示例：
    输入：A = [4,5,0,-2,-3,1], K = 5
    输出：7
    解释：
    有 7 个子数组满足其元素之和可被 K = 5 整除：
    [4, 5, 0, -2, -3, 1], [5], [5, 0], [5, 0, -2, -3], [0], [0, -2, -3], [-2, -3]
    提示：

    1 <= A.length <= 30000
    -10000 <= A[i] <= 10000
    2 <= K <= 10000
"""
from typing import List


class Solution:
    # 372ms, 17.6MB
    @classmethod
    def subarrays_div_by_K(cls, A: List[int], K: int) -> int:
        record = {0: 1}
        total = ans = 0
        for elem in A:
            total += elem
            modulus = total % K
            same = record.get(modulus, 0)
            ans += same
            record[modulus] = same + 1

        return ans


if __name__ == '__main__':
    test_cases = [
        ([4, 5, 0, -2, -3, 1], 5)
    ]
    for tc in test_cases:
        print(Solution.subarrays_div_by_K(*tc))
