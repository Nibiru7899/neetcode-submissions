class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash = {}
        for i in range (len(s)):
            if s[i] in hash:
                hash[s[i]]+=1
            else:
                hash[s[i]]=1
        count = {}
        for i in range (len(t)):
            if t[i] in count:
                count[t[i]]+=1
            else:
                count[t[i]]=1
        print(hash)
        return hash == count
