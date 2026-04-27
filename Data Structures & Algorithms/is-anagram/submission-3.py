class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash = {}
        for i in range (len(s)):
            if s[i] in hash:
                hash[s[i]]+=1
            else:
                hash[s[i]]=1
        for i in range (len(t)):
            if t[i] in hash:
                hash[t[i]]-=1
            else:
                return False

        for key,values in hash.items():
            if values != 0:
                return False
        return True
        