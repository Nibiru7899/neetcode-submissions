class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        countS = {}
        countT = {}

        for ch in s:
            countS[ch] = 1+ countS.get(ch,0)
        for ch in t:
            countS[ch] = countS.get(ch,0)-1
        for key,value in countS.items():
            if value!=0:
                return False
        return True
