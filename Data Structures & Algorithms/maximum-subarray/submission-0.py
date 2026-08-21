class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = float("-inf")
        sum = 0
        for num in nums:
            if sum<=0:
                sum = 0
            sum+=num
            maxSum = max(maxSum, sum)
        return maxSum