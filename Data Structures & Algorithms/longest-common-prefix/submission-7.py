class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = strs[0]
        for s in strs:
            i= 0
            while i<len(s) and i<len(res) and s[i] == res[i]:
                i+=1
            res = res[:i]
        return res