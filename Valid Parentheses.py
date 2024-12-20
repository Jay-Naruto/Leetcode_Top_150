class Solution:
    def isValid(self, s: str) -> bool:
        arr=[]
        dict={
            "(" : ")",
            "{" : "}",
            "[" : "]"
        }
        for i in range(len(s)):
            if s[i] in dict:
                arr.append(s[i])
            else:
                if not arr or s[i] != dict[arr.pop()]:
                    return False
                    
        return  True if len(arr) == 0 else False
            
        