class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i,j=0,0
        count=0
        if len(s) == 0 and len(t) > 0:
            return True
        if len(t) == 0 and len(s) > 0:
            return False
        while j <= len(t)-1 and i<=len(s)-1:
            if s[i] == t[j]:
                i+=1
                j+=1
                count+=1
            else:
                j+=1
        if count == len(s):
            return True
        else:
            return False

