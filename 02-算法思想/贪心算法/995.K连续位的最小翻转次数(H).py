"""
  @Author       : liujianhan
  @Date         : 21/2/18 11:51
  @Project      : leetcode_in_python
  @FileName     : 995.K连续位的最小翻转次数(H).py
  @Description  : 在仅包含 0 和 1 的数组 A 中，一次 K 位翻转包括选择一个长度为 K 的（连续）子数组，同时将子数组中的每个 0 更改为 1，
    而每个 1 更改为 0。返回所需的 K 位翻转的最小次数，以便数组没有值为 0 的元素。如果不可能，返回 -1。

    示例 1：
    输入：A = [0,1,0], K = 1
    输出：2
    解释：先翻转 A[0]，然后翻转 A[2]。

    示例 2：
    输入：A = [1,1,0], K = 2
    输出：-1
    解释：无论我们怎样翻转大小为 2 的子数组，我们都不能使数组变为 [1,1,1]。

    示例 3：
    输入：A = [0,0,0,1,0,1,1,0], K = 3
    输出：3
    解释：
    翻转 A[0],A[1],A[2]: A变成 [1,1,1,1,0,1,1,0]
    翻转 A[4],A[5],A[6]: A变成 [1,1,1,1,1,0,0,0]
    翻转 A[5],A[6],A[7]: A变成 [1,1,1,1,1,1,1,1]
     
    提示：
    1 <= A.length <= 30000
    1 <= K <= A.length
"""
import collections


class Solution(object):
    # 832ms, 15.9MB
    @staticmethod
    def min_K_bit_flips(A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        N = len(A)
        que = collections.deque()
        res = 0
        for i in range(N):
            if que and i >= que[0] + K:
                que.popleft()
            if len(que) % 2 == A[i]:
                if i + K > N:
                    return -1
                que.append(i)
                res += 1
        return res


if __name__ == '__main__':
    test_cases = [
        ([0, 1, 0], 1),
        ([1, 1, 0], 2),
        ([0, 0, 0, 1, 0, 1, 1, 0], 3),
    ]
    for test_case in test_cases:
        print(Solution.min_K_bit_flips(*test_case))
