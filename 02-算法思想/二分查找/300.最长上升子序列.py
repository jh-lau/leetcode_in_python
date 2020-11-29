"""
  User: Liujianhan
  https://leetcode-cn.com/problems/longest-increasing-subsequence/solution/zui-chang-shang-sheng-zi-xu-lie-by-leetcode-soluti/
 """
__author__ = 'liujianhan'


class Solution:
    @staticmethod
    def length_of_LIS(nums):
        mem = []
        len_nums = len(nums)
        for i in range(len_nums):
            low, high = 0, len(mem)
            while low < high:
                mid = low + (high-low) // 2
                if mem[mid] < nums[i]:
                    low = mid + 1
                else:
                    high = mid

            if high == len(mem):
                mem.append(nums[i])
            else:
                mem[high] = nums[i]
        return len(mem), mem
    
    @staticmethod
    def dp_method(nums):
        if not nums:
            return 0
        mem = [1] * len(nums)
        for j in range(1, len(nums)):
            for i in range(j):
                if nums[i] < nums[j]:
                    mem[j] = max(mem[j], mem[i] + 1)
        return max(mem)


if __name__ == '__main__':
    nums = [10, 9, 2, 5, 3, 7, 101]
    print(Solution().length_of_LIS(nums))
    print(Solution().dp_method(nums))
