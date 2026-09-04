class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashMap = {}
        if len(t) != len(s):
            return False
        for i in range (len(s)):
            hashMap[s[i]] = hashMap.get(s[i], 0) +1
            hashMap[t[i]] = hashMap.get(t[i], 0)-1

        for key,values in hashMap.items():
            if values!=0:
                return False
        return True