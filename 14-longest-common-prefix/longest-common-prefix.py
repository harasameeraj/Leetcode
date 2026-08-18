class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        n=strs[0]
        prfix=""
        m=""
        for i in range(len(n)):
            for j in strs[1:]:
                if i>=len(j)  or n[i]!=j[i]:
                    return prfix
                
            prfix=prfix+n[i]
        return prfix