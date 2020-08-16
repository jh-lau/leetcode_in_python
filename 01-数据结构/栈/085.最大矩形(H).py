"""
  @Author       : Liujianhan
  @Date         : 20/5/5 16:19
  @FileName     : 085.最大矩形(H).py
  @ProjectName  : leetcode_in_python
  @Description  : 给定一个仅包含 0 和 1 的二维二进制矩阵，找出只包含 1 的最大矩形，并返回其面积。
    示例:
    输入:
    [
      ["1","0","1","0","0"],
      ["1","0","1","1","1"],
      ["1","1","1","1","1"],
      ["1","0","0","1","0"]
    ]
    输出: 6
 """
from typing import List


class Solution:
    # 116ms, 14.4MB
    @classmethod
    def maximal_rectangle(cls, matrix: List[List[str]]) -> int:
        """栈"""
        if not matrix or not matrix[0]:
            return 0
        row = len(matrix)
        col = len(matrix[0])
        heights = [0] * (col + 2)
        res = 0
        for i in range(row):
            stack = []
            for j in range(col):
                if matrix[i][j] == '1':
                    heights[j+1] += 1
                else:
                    heights[j+1] = 0
            for j in range(col + 2):
                while stack and heights[stack[-1]] > heights[j]:
                    tmp = stack.pop()
                    res = max(res, (j - stack[-1] - 1) * heights[tmp])
                stack.append(j)
        return res

    # 128ms, 14.4MB
    @classmethod
    def maximal_rectangle_v2(cls, matrix: List[List[str]]) -> int:
        """动态规划"""
        if not matrix or not matrix[0]:
            return 0
        row = len(matrix)
        col = len(matrix[0])
        left_j = [-1] * col
        right_j = [col] * col
        height_j = [0] * col
        res = 0
        for i in range(row):
            cur_left = -1
            cur_right = col

            for j in range(col):
                if matrix[i][j] == "1":
                    height_j[j] += 1
                else:
                    height_j[j] = 0

            for j in range(col):
                if matrix[i][j] == "1":
                    left_j[j] = max(left_j[j], cur_left)
                else:
                    left_j[j] = -1
                    cur_left = j

            for j in range(col - 1, -1, -1):
                if matrix[i][j] == "1":
                    right_j[j] = min(right_j[j], cur_right)
                else:
                    right_j[j] = col
                    cur_right = j
            for j in range(col):
                res = max(res, (right_j[j] - left_j[j] - 1) * height_j[j])
        return res

    # 56ms, 14.3MB
    @classmethod
    def maximal_rectangle_v3(cls, matrix: List[List[str]]) -> int:
        """位运算"""
        if not matrix or not matrix[0]:
            return 0
        # 将每一行看作一个二进制数，然后转化为一个整数
        nums = [int(''.join(row), base=2) for row in matrix]
        ans, N = 0, len(nums)
        # 遍历所有行
        for i in range(N):
            j, num = i, nums[i]
            # 将第i行，连续的，和接下来的所有行，做与运算
            while j < N:
                # 经过与运算后，num转化为二进制中的1，表示从i到j行，可以组成一个矩形的那几列
                num = num & nums[j]
                if not num:
                    break
                l, curnum = 0, num
                # 这个循环最精彩
                # 每次循环将curnum和其左移一位的数做与运算
                # 最终的循环次数l表示，最宽的有效宽度，
                while curnum:
                    l += 1
                    curnum = curnum & (curnum << 1)
                ans = max(ans, l * (j - i + 1))
                j += 1
        return ans


if __name__ == '__main__':
    test_case = [
        ["1", "0", "1", "0", "0"],
        ["1", "0", "1", "1", "1"],
        ["1", "1", "1", "1", "1"],
        ["1", "0", "0", "1", "0"]
    ]
    print(Solution.maximal_rectangle(test_case))
    print(Solution.maximal_rectangle_v2(test_case))
    print(Solution.maximal_rectangle_v3(test_case))
