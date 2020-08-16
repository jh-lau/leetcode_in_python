"""
  @Author       : liujianhan
  @Date         : 2020/7/6 下午2:31
  @Project      : leetcode_in_python
  @FileName     : 239.滑动窗口最大值(H).py
  @Description  : 给定一个数组 nums，有一个大小为 k 的滑动窗口从数组的最左侧移动到数组的最右侧。你只可以看到在滑动窗口内的 k 个数字。滑动窗口每次只向右移动一位。
    返回滑动窗口中的最大值。
    进阶：
    你能在线性时间复杂度内解决此题吗？
    示例:
    输入: nums = [1,3,-1,-3,5,3,6,7], 和 k = 3
    输出: [3,3,5,5,6,7]
    解释:

      滑动窗口的位置                最大值
    ---------------               -----
    [1  3  -1] -3  5  3  6  7       3
     1 [3  -1  -3] 5  3  6  7       3
     1  3 [-1  -3  5] 3  6  7       5
     1  3  -1 [-3  5  3] 6  7       5
     1  3  -1  -3 [5  3  6] 7       6
     1  3  -1  -3  5 [3  6  7]      7

    提示：

    1 <= nums.length <= 10^5
    -10^4 <= nums[i] <= 10^4
    1 <= k <= nums.length
"""
import collections
from typing import List


class Solution:
    # 128ms, 23MB
    @staticmethod
    def max_sliding_window(nums: List[int], k: int) -> List[int]:
        deque = collections.deque()
        res = []
        for i, num in enumerate(nums):
            while deque and deque[0] <= i - k:
                deque.popleft()  # outdate indices
            while deque and num > nums[deque[-1]]:
                deque.pop()
            deque.append(i)
            if i >= k - 1:
                res.append(nums[deque[0]])
        return res

    # 超时
    @staticmethod
    def max_sliding_window_v2(nums: List[int], k: int) -> List[int]:
        left = 0
        right = left + k
        res = []
        while right <= len(nums):
            res.append(max(nums[left:right]))
            left += 1
            right = left + k

        return res


if __name__ == '__main__':
    print(Solution.max_sliding_window([1, 3, -1, -3, 5, 3, 6, 7], 3))
    print(Solution.max_sliding_window_v2([1, 3, -1, -3, 5, 3, 6, 7], 3))
