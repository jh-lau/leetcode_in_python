"""
  @Author       : Liujianhan
  @Date         : 20/5/4 20:51
  @FileName     : 075.颜色分类(M).py
  @ProjectName  : leetcode_in_python
  @Description  : 给定一个包含红色、白色和蓝色，一共 n 个元素的数组，原地对它们进行排序，使得相同颜色的元素相邻，并按照红色、白色、蓝色顺序排列。
    此题中，我们使用整数 0、 1 和 2 分别表示红色、白色和蓝色。
    注意:
    不能使用代码库中的排序函数来解决这道题。
    示例:
    输入: [2,0,2,1,1,0]
    输出: [0,0,1,1,2,2]
    进阶：
    一个直观的解决方案是使用计数排序的两趟扫描算法。
    首先，迭代计算出0、1 和 2 元素的个数，然后按照0、1、2的排序，重写当前数组。
    你能想出一个仅使用常数空间的一趟扫描算法吗
 """
from typing import List


class Solution:
    # 44ms, 13.7MB
    @classmethod
    def sort_colors(cls, nums: List[int]) -> None:
        """荷兰三色旗问题, O(N), O(1)"""
        p0 = curr = 0
        p2 = len(nums) - 1

        while curr <= p2:
            if not nums[curr]:
                nums[p0], nums[curr] = nums[curr], nums[p0]
                p0 += 1
                curr += 1
            elif nums[curr] == 2:
                nums[curr], nums[p2] = nums[p2], nums[curr]
                p2 -= 1
            else:
                curr += 1


if __name__ == '__main__':
    test_cases = [
        [2, 0, 2, 1, 1, 0]
    ]
    for tc in test_cases:
        Solution.sort_colors(tc)
        print(tc)
