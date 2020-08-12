"""
  @Author       : liujianhan
  @Date         : 2020/8/12 下午7:04
  @Project      : leetcode_in_python
  @FileName     : 264.丑数II(M).py
  @Description  : 编写一个程序，找出第 n 个丑数。
    丑数就是质因数只包含 2, 3, 5 的正整数。
    示例:
    输入: n = 10
    输出: 12
    解释: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 是前 10 个丑数。
    说明:  

    1 是丑数。
    n 不超过1690。

"""
from heapq import heappush, heappop


class Ugly:
    def __init__(self):
        seen = {1, }
        self.nums = nums = []
        heap = []
        heappush(heap, 1)

        for _ in range(1690):
            curr_ugly = heappop(heap)
            nums.append(curr_ugly)
            for i in [2, 3, 5]:
                new_ugly = curr_ugly * i
                if new_ugly not in seen:
                    seen.add(new_ugly)
                    heappush(heap, new_ugly)


class Solution:
    # 48ms, 13.8MB
    u = Ugly()

    def nth_ugly_number(self, n: int) -> int:
        return self.u.nums[n - 1]


if __name__ == '__main__':
    print(Solution().nth_ugly_number(10))
