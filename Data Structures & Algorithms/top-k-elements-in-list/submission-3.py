class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        bucket = [[] for _ in range (len(nums)+1)]
        freq = {}
        res = []
        for n in nums:
            freq[n] = freq.get(n,0) +1
        for key,values in freq.items():
            bucket[values].append(key)
        for i in range (len(bucket)-1,-1,-1):
            if bucket[i]:
                for n in bucket[i]:
                    res.append(n)
                    if len(res)==k:
                        return res