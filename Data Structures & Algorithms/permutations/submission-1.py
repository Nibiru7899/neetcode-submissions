class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def dfs(curr, i):
            if len(curr) == len(nums):
                res.append(curr.copy())
                return

            for i in range(len(nums)):
                if seen[i]:
                    continue
                seen[i] = True
                curr.append(nums[i])
                dfs(curr,i+1)
                curr.pop()
                seen[i] = False
        res = []
        seen = [False]*len(nums)
        dfs([],0)
        return res