class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(r,c, i):
            if i==len(word):
                return True
            if r<0 or c<0 or r>=rows or c>=columns or word[i]!=board[r][c] or (r,c) in curr:
                return
            curr.add((r,c))
            res = dfs(r+1,c,i+1)or dfs(r,c+1,i+1)or dfs(r-1,c,i+1)or dfs(r,c-1,i+1)
            curr.remove((r,c))
            return res

        rows = len(board)
        columns = len(board[0])
        res = []
        curr = set()
        for r in range (rows):
            for c in range (columns):
                if dfs(r,c,0):
                    return True
        return False