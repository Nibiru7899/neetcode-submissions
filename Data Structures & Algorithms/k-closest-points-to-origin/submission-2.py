class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []
        res = []
        for pt in points:
            point = (pt[0]**2+pt[1]**2)
            minHeap.append([point,pt[0],pt[1]])
        heapq.heapify(minHeap)
        while k>0:
            pt, x, y = heapq.heappop(minHeap)
            res.append([x,y])
            k-=1
        return res
