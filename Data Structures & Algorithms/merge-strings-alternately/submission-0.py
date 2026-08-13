class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        l = 0
        r = 0
        s = ""
        while l+r < len(word1+word2):
            if l<len(word1):
                s+=word1[l]
                l+=1
            if r<len(word2):
                s+=word2[r]
                r+=1
            
            elif l==len(word1):
                s+=word2[r:]
                break
            else:
                s+=word1[l:]
                break
        return s
