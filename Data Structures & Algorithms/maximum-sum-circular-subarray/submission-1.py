class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        globmax = nums[0]
        globmin = nums[0]
        currmax, currmin = 0,0
        total = 0
        for n in nums:
            currmax= max(currmax+n, n)
            currmin= min(currmin+n,n)

            globmax = max(globmax, currmax)
            globmin = min(globmin, currmin)
            total+=n

        return max(globmax, total-globmin) if globmax>0 else globmax