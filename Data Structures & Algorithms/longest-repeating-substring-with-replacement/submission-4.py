class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hashMap = {}
        l = 0
        res = 0
        for r in range (len(s)):
            hashMap[s[r]] = hashMap.get(s[r],0)+1
            while (r-l+1)-(max(hashMap.values()))>k:
                hashMap[s[l]] = hashMap.get(s[l],0)-1
                l+=1
            res = max(res,r-l+1)
        return res