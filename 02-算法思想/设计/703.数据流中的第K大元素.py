"""
  @Author       : liujianhan
  @Date         : 21/2/11 0:40
  @Project      : leetcode_in_python
  @FileName     : 703.数据流中的第K大元素.py
  @Description  : 设计一个找到数据流中第 k 大元素的类（class）。注意是排序后的第 k 大元素，不是第 k 个不同的元素。

    请实现 KthLargest 类：

    KthLargest(int k, int[] nums) 使用整数 k 和整数流 nums 初始化对象。
    int add(int val) 将 val 插入数据流 nums 后，返回当前数据流中第 k 大的元素。
     

    示例：

    输入：
    ["KthLargest", "add", "add", "add", "add", "add"]
    [[3, [4, 5, 8, 2]], [3], [5], [10], [9], [4]]
    输出：
    [null, 4, 5, 5, 8, 8]

    解释：
    KthLargest kthLargest = new KthLargest(3, [4, 5, 8, 2]);
    kthLargest.add(3);   // return 4
    kthLargest.add(5);   // return 5
    kthLargest.add(10);  // return 5
    kthLargest.add(9);   // return 8
    kthLargest.add(4);   // return 8
     

    提示：
    1 <= k <= 104
    0 <= nums.length <= 104
    -104 <= nums[i] <= 104
    -104 <= val <= 104
    最多调用 add 方法 104 次
    题目数据保证，在查找第 k 大元素时，数组中至少有 k 个元素
    """
import heapq


class KthLargest(object):

    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        # self k
        self.k = k
        self.heap = nums
        # heap其实就是个list
        heapq.heapify(self.heap)
        # 减小到k
        while len(self.heap) > k:
            heapq.heappop(self.heap)

    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        # 不过堆不够，则直接添加进去
        if len(self.heap) < self.k:
            heapq.heappush(self.heap, val)
        elif self.heap[0] < val:
            # 新的值更大，更新
            heapq.heapreplace(self.heap, val)

        return self.heap[0]


if __name__ == '__main__':
    pass