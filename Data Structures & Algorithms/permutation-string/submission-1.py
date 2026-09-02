class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        hashmap1 = {}
        hashmap2 = {}
        for s in s1:
            hashmap1[s] = hashmap1.get(s,0) + 1
        l = 0
        for r in range (len(s2)):
            hashmap2[s2[r]] = hashmap2.get(s2[r],0) +1
            if r-l+1 > len(s1):
                hashmap2[s2[l]] -=1
                if hashmap2[s2[l]] == 0:
                    del hashmap2[s2[l]]
                l+=1
            if hashmap1==hashmap2:
                return True
        return False