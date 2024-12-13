class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        i=0
        j=0
        
        while i < len(haystack):
            
            if haystack[i] == needle[j]:
                i+=1
                j+=1
                
                if j==len(needle):
                    return i - len(needle)
            else:
                i = i - j + 1
                j=0
        return -1
        