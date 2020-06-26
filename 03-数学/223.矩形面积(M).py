"""
  @Author       : Liujianhan
  @Date         : 20/6/26 20:39
  @FileName     : 223.矩形面积(M).py
  @ProjectName  : leetcode_in_python
  @Description  : 在二维平面上计算出两个由直线构成的矩形重叠后形成的总面积。
    每个矩形由其左下顶点和右上顶点坐标表示，如图所示。
    示例:
    输入: -3, 0, 3, 4, 0, -1, 9, 2
    输出: 45
    说明: 假设矩形面积不会超出 int 的范围。
 """


class Solution:
    # 68ms, 13.8MB
    @staticmethod
    def compute_area(A: int, B: int, C: int, D: int, E: int, F: int, G: int, H: int) -> int:
        if D <= F or E >= C or B >= H or G <= A:
            return (D - B) * (C - A) + (H - F) * (G - E)

        left = max(E, A)
        right = min(C, G)
        up = min(H, D)
        down = max(F, B)
        return (D - B) * (C - A) + (H - F) * (G - E) - (up - down) * (right - left)


if __name__ == '__main__':
    test_cases = [
        [-3, 0, 3, 4, 0, -1, 9, 2],
        [0, 0, 0, 0, -1, -1, 1, 1]
    ]
    for tc in test_cases:
        print(Solution.compute_area(*tc))
