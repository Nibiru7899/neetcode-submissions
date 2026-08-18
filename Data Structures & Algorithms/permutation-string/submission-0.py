class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        countS1 = {}
        countS2 = {}
        for s in s1:
            countS1[s] = countS1.get(s,0) +1
        l = 0
        for r in range (len(s2)):
            countS2[s2[r]] = countS2.get(s2[r],0) +1
            if r-l+1 > len(s1):
                countS2[s2[l]] -=1
                if countS2[s2[l]] == 0:
                    del countS2[s2[l]]
                l+=1
            if countS1 == countS2:
                return True
        return False