class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        
        words=s.split()
        
        if len(words) != len(pattern):
            return False
        
        dict1={}
        dict2={}
        
        for i in range(len(words)):
            if pattern[i] in dict1:
                if words[i] != dict1[pattern[i]]:
                    return False
            else:
                if words[i] in dict2 and pattern[i] != dict2[words[i]]:
                    return False
                dict1[pattern[i]] = words[i]
                dict2[words[i]] = pattern[i]
        
        return True