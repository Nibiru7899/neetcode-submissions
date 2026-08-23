class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def dfs(openN, closeN):
            if openN==closeN==n:
                res.append("".join(stack))
                return
            if openN < n:
                stack.append("(")
                dfs(openN+1, closeN)
                stack.pop()
            if closeN<openN:
                stack.append(")")
                dfs(openN, closeN+1)
                stack.pop()

        stack = []
        res = []
        dfs(0,0)

        return res