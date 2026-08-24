class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def dfs(openN, closeN):
            if closeN==openN==n:
                res.append("".join(curr))
                return
            if openN<n:
                curr.append("(")
                dfs(openN+1,closeN)
                curr.pop()
            if closeN<openN:
                curr.append(")")
                dfs(openN,closeN+1)
                curr.pop()
        curr=[]
        res= []
        dfs(0,0)
        return res