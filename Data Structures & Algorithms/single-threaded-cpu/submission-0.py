class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        for i,t in enumerate(tasks):
            t.append(i)

        res =[]
        minHeap = []
        tasks.sort(key = lambda x:x[0])
        i = 0
        time = tasks[0][0]


        while minHeap or i<len(tasks):
            while i<len(tasks) and time>=tasks[i][0]:
                heapq.heappush(minHeap, [tasks[i][1],tasks[i][2]])
                i+=1
            if not minHeap:
                time = tasks[i][0]
            else:
                proc, index = heapq.heappop(minHeap)
                time += proc
                res.append(index)
        return res