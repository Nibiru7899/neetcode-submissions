class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def dfs(start, curr):
            if len(curr) == k:
                res.append(curr.copy())
            
            for j in range (start, n+1):
                curr.append(j)
                dfs(j+1, curr)
                curr.pop()
        res = []
        dfs(1,[])
        return res