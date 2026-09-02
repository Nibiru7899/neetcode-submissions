class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0]*len(temperatures)
        for ind, temp in enumerate(temperatures):
            while stack and stack[-1][0] < temp:
                t,i = stack.pop()
                res[i] = ind-i
            stack.append([temp,ind])
        return res