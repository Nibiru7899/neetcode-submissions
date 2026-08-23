class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        countS = Counter(s)
        for n in t:
            if n in countS:
                countS[n] -=1
            else:
                return False
        for i in countS.values():
            if i != 0:
                return False
        return True