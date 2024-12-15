class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:

        k=0
        
        if s != "":
            for i in range(len(t)):
                if k <=len(s)-1:
                    if  t[i] == s[k]:
                        k+=1
        if k == len(s):
            return True
        else:
            return False