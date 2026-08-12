class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        check  = {}
        for i,n in enumerate(nums):
            need = target-n
            if need in check:
                return [check[need], i ]
            else:
                check[n] = i