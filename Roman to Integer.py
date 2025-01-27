class Solution:
    def romanToInt(self, s: str) -> int:
        map={
            'I':1,
            'V':5,
            'X':10,
            'L':50,
            'C':100,
            'D':500,
            'M':1000,
        }
        map2={
            'IV':4,
            'IX':9,
            'XL':40,
            'XC':90,
            'CD':400,
            'CM':900
        }
        ans = 0
        skip = False  
        
        for i in range(len(s)):
            if skip:  
                skip = False
                continue
            if i < len(s) - 1 and s[i] + s[i + 1] in map2:
                ans += map2[s[i] + s[i + 1]]
                skip = True
            else:
                ans += map[s[i]]
        return ans
            