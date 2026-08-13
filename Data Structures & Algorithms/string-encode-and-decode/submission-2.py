class Solution:

    def encode(self, strs: List[str]) -> str:
        stri = ""
        for s in strs:
            stri += str(len(s))+"#"+s
        return stri
    def decode(self, s: str) -> List[str]:
        i = 0
        res = []

        while i<len(s):
            j = i
            while s[j]!="#":
                j+=1
            length = int(s[i:j])
            stri = s[j+1:j+1+length]
            res.append(stri)
            i = j+1+length
        return res
