"""
  @Author       : liujianhan
  @Date         : 2020/9/10 10:50
  @Project      : leetcode_in_python
  @FileName     : 352.将数据流变为多个不相交区间(H).py
  @Description  : 给定一个非负整数的数据流输入 a1，a2，…，an，…，将到目前为止看到的数字总结为不相交的区间列表。
    例如，假设数据流中的整数为 1，3，7，2，6，…，每次的总结为：
    [1, 1]
    [1, 1], [3, 3]
    [1, 1], [3, 3], [7, 7]
    [1, 3], [7, 7]
    [1, 3], [6, 7]

    进阶：
    如果有很多合并，并且与数据流的大小相比，不相交区间的数量很小，该怎么办?
"""
import bisect


# 160ms, 18.2MB
class SummaryRanges:
    def __init__(self):
        self.d = []

    def addNum(self, val: int) -> None:
        m = bisect.bisect(self.d, val)  # 二分查找插入坐标
        if m % 2 == 0:
            if m < len(self.d) and self.d[m] - val == 1:  # 如果跟右侧区间差值为1时就直接更新右侧区间，为0时不会插入在这里，所以只判断1
                self.d[m] = val
            else:
                self.d.insert(m, val)  # 如果跟区间不相邻就插入区间
                self.d.insert(m, val)
            if m > 0 and self.d[m] - self.d[m - 1] <= 1:  # 根据现有情况选择是否区间合并
                self.d.pop(m)
                self.d.pop(m - 1)

    def getIntervals(self):
        return zip(self.d[:: 2], self.d[1:: 2])  # 按奇偶顺序打包输出
