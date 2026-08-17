class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        m=0
        for i in s:
            
            if i in t:
                m=t.find(i)
                t=t[:m]+t[m+1:]
            else:
                return False
            
        if t!="":
            return False
        return True