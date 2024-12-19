class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False
        
        dict1={}
        
        for char in s:
            if char in dict1:
                dict1[char] += 1
            else:
                dict1[char] = 1

        for char in t:
            if char in dict1:
                if dict1[char] < 0:
                    return False
                dict1[char] -= 1
            else:
                return False
                
        
        for i in range(len(s)):
            if dict1[s[i]] != 0:
                return False
            else:
                return True
