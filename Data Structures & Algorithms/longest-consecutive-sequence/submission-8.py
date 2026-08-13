class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashSet = set(nums)
        res = 0

        for n in hashSet:
            if n-1 not in hashSet:
                start = n
                length = 0
                while start+length in hashSet:
                    length+=1
                res = max(res,length)
        return res