"""
  @Author       : liujianhan
  @Date         : 21/2/24 10:34
  @Project      : leetcode_in_python
  @FileName     : 832.翻转图像.py
  @Description  : 给定一个二进制矩阵 A，我们想先水平翻转图像，然后反转图像并返回结果。

水平翻转图片就是将图片的每一行都进行翻转，即逆序。例如，水平翻转 [1, 1, 0] 的结果是 [0, 1, 1]。

反转图片的意思是图片中的 0 全部被 1 替换， 1 全部被 0 替换。例如，反转 [0, 1, 1] 的结果是 [1, 0, 0]。

 

示例 1：

输入：[[1,1,0],[1,0,1],[0,0,0]]
输出：[[1,0,0],[0,1,0],[1,1,1]]
解释：首先翻转每一行: [[0,1,1],[1,0,1],[0,0,0]]；
     然后反转图片: [[1,0,0],[0,1,0],[1,1,1]]
示例 2：

输入：[[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]
输出：[[1,1,0,0],[0,1,1,0],[0,0,0,1],[1,0,1,0]]
解释：首先翻转每一行: [[0,0,1,1],[1,0,0,1],[1,1,1,0],[0,1,0,1]]；
     然后反转图片: [[1,1,0,0],[0,1,1,0],[0,0,0,1],[1,0,1,0]]
 

提示：

1 <= A.length = A[0].length <= 20
0 <= A[i][j] <= 1
"""
from typing import List


class Solution:
    # 56ms, 14.8MB
    @staticmethod
    def flip_and_invert_image(A: List[List[int]]) -> List[List[int]]:
        for i in range(len(A)):
            for j in range((len(A) + 1) // 2):
                if A[i][j] == A[i][-1 - j]:
                    t = 1 - A[i][j]
                    A[i][j] = A[i][-1 - j] = t
        return A


if __name__ == '__main__':
    test_cases = [
        [[1, 1, 0], [1, 0, 1], [0, 0, 0]],
        [[1, 1, 0, 0], [1, 0, 0, 1], [0, 1, 1, 1], [1, 0, 1, 0]]
    ]
    for test_case in test_cases:
        print(Solution.flip_and_invert_image(test_case))
