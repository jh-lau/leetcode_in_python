"""
  User: Liujianhan
 """
__author__ = 'liujianhan'


class Solution:
    @staticmethod
    def top_k_frequent(nums, k):
        from collections import defaultdict
        if not nums or len(nums) == 1:
            return nums
        dic = defaultdict(int)
        for num in nums:
            dic[num] += 1
        return [x[0] for x in sorted(dic.items(), key=lambda x: x[1], reverse=True)][:k]

    @staticmethod
    def heap_method(nums, k):
        import heapq
        dic = {}
        for v in nums:
            dic[v] = dic.get(v, 0) + 1
        heap = []
        for key, value in dic.items():
            if len(heap) < k:
                heapq.heappush(heap, (value, key))
                continue
            if value > heap[0][0]:
                heapq.heapreplace(heap, (value, key))
        res = []
        while heap:
            res.insert(0, heapq.heappop(heap)[1])
        return res


if __name__ == '__main__':
    print(Solution().top_k_frequent([1, 1, 1, 2, 2, 3], 2))
