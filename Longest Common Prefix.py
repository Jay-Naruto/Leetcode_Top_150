class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort(key=len); 
        shortest=strs[0]
        for i in range(len(shortest)):
            check = shortest[i]
            for s in strs:
                if s[i] != check:
                    return shortest[:i]
        return shortest