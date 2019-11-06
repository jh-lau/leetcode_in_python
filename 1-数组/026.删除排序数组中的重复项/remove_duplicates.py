"""
  User: Liujianhan
  Time: 20:58
 """
__author__ = 'liujianhan'


class Solution:
    @staticmethod
    def remove_duplicates(nums) -> int:
        k = 0
        for index, num in enumerate(nums):
            if k < 1 or num != nums[k - 1]:
                if index != k:
                    nums[k] = num
                    k += 1
                else:
                    k += 1
        return k


if __name__ == '__main__':
    test = [1, 1, 2, 3, 4, 5, 5, 6]
    print(Solution.remove_duplicates(test))
    print(test)
