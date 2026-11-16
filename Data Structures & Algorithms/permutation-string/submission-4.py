class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        h1 = {}
        h2 = {}
        for s in s1:
            h1[s] = h1.get(s,0)+1
        l = 0
        for r in range (len(s2)):
            h2[s2[r]] = h2.get(s2[r],0)+1
            if r-l+1 > len(s1):
                h2[s2[l]]-=1
                if h2[s2[l]] == 0:
                    del h2[s2[l]]
                l+=1
            if h1 == h2:
                return True
        return False

