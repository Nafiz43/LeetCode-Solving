import heapq

class Solution:
    def kClosest(self, points, k):
        h = []
        for x, y in points:
            heapq.heappush(h, (-(x*x + y*y), [x,y]))
            if len(h) > k:
                heapq.heappop(h)
        return [pair[1] for pair in h]