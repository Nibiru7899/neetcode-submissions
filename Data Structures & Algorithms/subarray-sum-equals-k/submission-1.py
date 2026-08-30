class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        freq = {0:1}
        currsum = 0
        for n in nums:
            currsum +=n
            diff = currsum-k
            res += freq.get(diff,0)
            freq[currsum] = freq.get(currsum,0)+1
        return res