class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs=sorted(strs)
        print(strs)
        count = ""
        first = strs[0]
        last = strs[-1]
        for i in range (min(len(strs[0]),len(strs[-1]))):
            if first[i]==last[i]:
                count= count+first[i]
            else:
                break
        return count