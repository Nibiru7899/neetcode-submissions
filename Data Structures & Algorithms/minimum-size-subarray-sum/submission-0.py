class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        Sum = 0
        count = float("inf")
        l= 0
        for r in range (0,len(nums)):
            Sum +=nums[r]
            while Sum >= target:
                count = min(count, r-l+1)
                Sum -= nums[l]
                l+=1
        return count if count!=float("inf") else 0
             