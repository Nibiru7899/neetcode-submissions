class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash = {}
        for i in range (len(nums)):
            if nums[i] in hash:
                hash[nums[i]]+=1
            else:
                hash[nums[i]]=1
            

        keys = sorted(hash.values(),reverse = True)[:k]

        res = []

        for key,values in hash.items():
            if values in keys:
                res.append(key)
        return res