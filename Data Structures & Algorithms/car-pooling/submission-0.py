class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key = lambda x:x[1])
        currPass = 0
        minHeap = []
        for t in trips:
            numPass, start, end = t
            while minHeap and minHeap[0][0]<=start: #end,num of passengers will be store
                currPass -=minHeap[0][1]
                heapq.heappop(minHeap)
            currPass +=numPass
            if currPass>capacity:
                return False
            heapq.heappush(minHeap,[end,numPass])
        return True
                
