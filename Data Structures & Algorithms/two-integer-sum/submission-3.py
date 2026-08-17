class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        req = {}

        for i,n in enumerate(nums):
            need = target-n
            if need in req:
                return [req[need], i]
            else:
                req[n] = i