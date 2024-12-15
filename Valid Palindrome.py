class Solution:
    def isPalindrome(self, s: str) -> bool:
        check=''
        check2=''
        
        for char in s:
            if char.isalnum():
                check+=char.lower()
        
        for i in range(len(s)-1,-1,-1):
            if s[i].isalnum():
                check2+=s[i].lower()
                
        if check == check2:
            return True
        else:
            return False