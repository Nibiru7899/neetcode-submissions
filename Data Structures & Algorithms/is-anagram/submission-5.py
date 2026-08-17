class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        countS= {}
        countT = {}

        for n in s:
            countS[n] = countS.get(n,0)+1
        
        for n in t:
            countS[n] = countS.get(n,0)-1

        for i in (countS.values()):
            if i!=0:
                return False
        return True

