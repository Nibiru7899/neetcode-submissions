class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashMap = {}
        res = []
        count = [[] for _ in range (len(nums)+1)]
        for n in nums:
            hashMap[n] = hashMap.get(n,0) +1
        for key,value in hashMap.items():
            count[value].append(key)
        for i in range (len(count)-1,-1,-1):
                for n in count[i]:
                    res.append(n)
                    if len(res)==k:
                        return res
