class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        thresh = len(nums)//3
        hash = {}
        count = []
        for i in range (len(nums)):
            if nums[i] in hash:
                hash[nums[i]]+=1
            else:
                hash[nums[i]]=1
        
        for key,vals in hash.items():
            if vals>thresh:
                count.append(key)
        return count